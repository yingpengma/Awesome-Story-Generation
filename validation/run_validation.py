#!/usr/bin/env python3
"""
RAG Story Generation - Full Validation Phase
Runs complete validation experiment: extract papers → generate stories → evaluate
"""

import os
import json
import yaml
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

# Import validation modules
import sys
sys.path.append(str(Path(__file__).parent / "src"))

from paper_extractor import create_sample_extractions
from rag_retrieval import RAGRetriever
from story_generator import StoryGenerator, generate_story_pair
from evaluator import StoryEvaluator, evaluate_story_pair

console = Console()


def load_config() -> dict:
    """Load configuration"""
    config_path = Path("validation/configs/config.yaml")

    with open(config_path) as f:
        return yaml.safe_load(f)


def run_full_validation():
    """Run complete validation experiment"""

    console.print("\n" + "="*70)
    console.print("[bold cyan]RAG STORY GENERATION - VALIDATION PHASE[/bold cyan]")
    console.print("="*70 + "\n")

    # Load environment and config
    load_dotenv()
    config = load_config()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        console.print("[red]Error: OPENAI_API_KEY not found in environment[/red]")
        console.print("Create a .env file with: OPENAI_API_KEY=your-key-here")
        return

    # Results directory
    results_dir = Path("validation/results")
    results_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # ========== PHASE 1: Paper Extraction ==========
    console.print("[bold]PHASE 1: Paper Technique Extraction[/bold]")
    console.print("-" * 70)

    extractions_file = Path("validation/data/paper_extractions.json")

    if not extractions_file.exists():
        console.print("[yellow]Creating manual paper extractions...[/yellow]")
        extractions = create_sample_extractions()

        extractions_file.parent.mkdir(parents=True, exist_ok=True)

        with open(extractions_file, 'w') as f:
            json.dump(extractions, f, indent=2)

        console.print(f"[green]✓[/green] Extracted {len(extractions)} papers")
    else:
        console.print("[green]✓[/green] Loading existing extractions")

        with open(extractions_file) as f:
            extractions = json.load(f)

    for ext in extractions:
        console.print(f"  • {ext['title']}")

    # ========== PHASE 2: RAG Setup ==========
    console.print(f"\n[bold]PHASE 2: RAG Retrieval Setup[/bold]")
    console.print("-" * 70)

    console.print("[yellow]Initializing vector database...[/yellow]")
    retriever = RAGRetriever(api_key, collection_name=f"validation_{timestamp}")
    retriever.create_collection(extractions)

    console.print("[green]✓[/green] RAG system ready")

    # ========== PHASE 3: Story Generation ==========
    console.print(f"\n[bold]PHASE 3: Story Generation[/bold]")
    console.print("-" * 70)

    generator = StoryGenerator(api_key)

    test_prompts = config['generation']['test_prompts']
    num_comparisons = config['evaluation'].get('num_comparisons', len(test_prompts))

    # Limit to configured number
    test_prompts = test_prompts[:num_comparisons]

    console.print(f"Generating {len(test_prompts)} story pairs...\n")

    story_pairs = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:

        for i, prompt_config in enumerate(test_prompts, 1):
            task = progress.add_task(
                f"[cyan]Pair {i}/{len(test_prompts)}: {prompt_config['genre']}...",
                total=None
            )

            pair = generate_story_pair(
                generator=generator,
                retriever=retriever,
                genre=prompt_config['genre'],
                topic=prompt_config['topic'],
                requirements=prompt_config['requirements']
            )

            story_pairs.append(pair)

            progress.update(task, completed=True)

            # Save individual pair
            pair_file = results_dir / f"pair_{i}_{timestamp}.json"

            with open(pair_file, 'w') as f:
                json.dump(pair, f, indent=2)

    console.print(f"\n[green]✓[/green] Generated {len(story_pairs)} story pairs")

    # ========== PHASE 4: Evaluation ==========
    console.print(f"\n[bold]PHASE 4: Story Evaluation[/bold]")
    console.print("-" * 70)

    evaluator = StoryEvaluator(api_key)

    evaluations = []
    rag_wins = 0
    total_baseline_score = 0
    total_rag_score = 0

    for i, pair in enumerate(story_pairs, 1):
        console.print(f"\n[cyan]Evaluating pair {i}/{len(story_pairs)}...[/cyan]")

        eval_result = evaluate_story_pair(evaluator, pair)
        evaluations.append(eval_result)

        # Track statistics
        if eval_result['blind_comparison']['rag_won']:
            rag_wins += 1

        total_baseline_score += eval_result['summary']['baseline_overall_score']
        total_rag_score += eval_result['summary']['rag_overall_score']

    # ========== PHASE 5: Final Analysis ==========
    console.print("\n" + "="*70)
    console.print("[bold green]VALIDATION RESULTS[/bold green]")
    console.print("="*70 + "\n")

    # Calculate statistics
    rag_win_rate = rag_wins / len(story_pairs)
    avg_baseline_score = total_baseline_score / len(story_pairs)
    avg_rag_score = total_rag_score / len(story_pairs)
    score_improvement = avg_rag_score - avg_baseline_score

    # Display results
    console.print(f"[bold]Total Comparisons:[/bold] {len(story_pairs)}")
    console.print(f"[bold]RAG Wins:[/bold] {rag_wins}/{len(story_pairs)} ({rag_win_rate:.1%})")
    console.print(f"[bold]Baseline Wins:[/bold] {len(story_pairs) - rag_wins}/{len(story_pairs)} ({1-rag_win_rate:.1%})")

    console.print(f"\n[bold]Average Scores:[/bold]")
    console.print(f"  Baseline: {avg_baseline_score:.2f}/10")
    console.print(f"  RAG: {avg_rag_score:.2f}/10")

    if score_improvement > 0:
        console.print(f"  [green]Improvement: +{score_improvement:.2f} points ({score_improvement/avg_baseline_score:.1%})[/green]")
    else:
        console.print(f"  [red]Difference: {score_improvement:.2f} points ({score_improvement/avg_baseline_score:.1%})[/red]")

    # Success criteria
    success_threshold = config['validation']['success_threshold']
    min_quality = config['validation']['min_quality_score']

    console.print(f"\n[bold]Validation Criteria:[/bold]")

    criteria_met = []

    # Criterion 1: Win rate
    win_rate_met = rag_win_rate >= success_threshold
    criteria_met.append(win_rate_met)

    if win_rate_met:
        console.print(f"  [green]✓[/green] Win rate {rag_win_rate:.1%} >= {success_threshold:.1%} threshold")
    else:
        console.print(f"  [red]✗[/red] Win rate {rag_win_rate:.1%} < {success_threshold:.1%} threshold")

    # Criterion 2: Quality score
    quality_met = avg_rag_score >= min_quality
    criteria_met.append(quality_met)

    if quality_met:
        console.print(f"  [green]✓[/green] RAG score {avg_rag_score:.2f} >= {min_quality} minimum")
    else:
        console.print(f"  [red]✗[/red] RAG score {avg_rag_score:.2f} < {min_quality} minimum")

    # Criterion 3: Improvement
    improvement_met = score_improvement > 0
    criteria_met.append(improvement_met)

    if improvement_met:
        console.print(f"  [green]✓[/green] RAG shows positive improvement")
    else:
        console.print(f"  [red]✗[/red] RAG does not show improvement")

    # Overall verdict
    console.print("\n" + "="*70)

    if all(criteria_met):
        console.print("[bold green]✓ VALIDATION SUCCESSFUL - PROCEED TO MVP[/bold green]")
        console.print("RAG approach demonstrates clear quality improvement.")
        console.print("Recommendation: Proceed with MVP development.")
    elif any(criteria_met):
        console.print("[bold yellow]⚠ VALIDATION MIXED - ITERATE AND RETEST[/bold yellow]")
        console.print("RAG shows promise but doesn't meet all criteria.")
        console.print("Recommendation: Refine approach and run additional tests.")
    else:
        console.print("[bold red]✗ VALIDATION FAILED - RECONSIDER APPROACH[/bold red]")
        console.print("RAG does not demonstrate improvement over baseline.")
        console.print("Recommendation: Pivot to alternative strategy.")

    console.print("="*70 + "\n")

    # Save final report
    final_report = {
        "timestamp": timestamp,
        "configuration": config,
        "results": {
            "num_comparisons": len(story_pairs),
            "rag_wins": rag_wins,
            "rag_win_rate": rag_win_rate,
            "avg_baseline_score": avg_baseline_score,
            "avg_rag_score": avg_rag_score,
            "score_improvement": score_improvement,
            "criteria_met": {
                "win_rate": win_rate_met,
                "quality_threshold": quality_met,
                "positive_improvement": improvement_met
            },
            "validation_passed": all(criteria_met)
        },
        "evaluations": evaluations
    }

    report_file = results_dir / f"validation_report_{timestamp}.json"

    with open(report_file, 'w') as f:
        json.dump(final_report, f, indent=2)

    console.print(f"[green]✓[/green] Full report saved to: {report_file}\n")

    return final_report


if __name__ == "__main__":
    try:
        report = run_full_validation()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Validation interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"\n\n[red]Error during validation: {e}[/red]")
        raise
