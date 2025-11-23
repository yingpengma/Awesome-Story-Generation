"""
Story Evaluator
Evaluates and compares stories using LLM-as-judge
"""

import json
from typing import Dict, List
from openai import OpenAI
from rich.console import Console
from rich.table import Table

console = Console()


class StoryEvaluator:
    """Evaluate stories using LLM-as-judge approach"""

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

        self.evaluation_prompt = """You are an expert story critic and creative writing teacher. Evaluate this story on the following criteria:

STORY TO EVALUATE:
{story}

EVALUATION CRITERIA:
1. **Coherence** (1-10): Is the plot logical and easy to follow?
2. **Creativity** (1-10): Are the ideas original and imaginative?
3. **Character Depth** (1-10): Are characters well-developed and believable?
4. **Plot Structure** (1-10): Is the story well-paced with clear beginning, middle, end?
5. **Engagement** (1-10): Is the story compelling and entertaining?
6. **Genre Appropriateness** (1-10): Does it effectively deliver on the {genre} genre?

For each criterion, provide:
- A score (1-10)
- A brief justification (1-2 sentences)

Also provide an overall assessment and the story's main strengths and weaknesses.

Respond in JSON format:
{{
    "scores": {{
        "coherence": {{"score": 8, "justification": "..."}},
        "creativity": {{"score": 7, "justification": "..."}},
        "character_depth": {{"score": 6, "justification": "..."}},
        "plot_structure": {{"score": 8, "justification": "..."}},
        "engagement": {{"score": 7, "justification": "..."}},
        "genre_appropriateness": {{"score": 9, "justification": "..."}}
    }},
    "overall_score": 7.5,
    "strengths": ["...", "...", "..."],
    "weaknesses": ["...", "..."],
    "overall_assessment": "..."
}}
"""

        self.comparison_prompt = """You are an expert story critic. Compare these two stories written for the same prompt.

STORY A:
{story_a}

STORY B:
{story_b}

PROMPT: {genre} story about "{topic}" with requirements: {requirements}

Which story is better overall? Consider:
- Quality of writing
- Effectiveness in meeting requirements
- Creativity and originality
- Character development
- Plot structure and pacing
- Reader engagement

Respond in JSON:
{{
    "winner": "A" or "B",
    "confidence": 0.0-1.0,
    "reasoning": "Detailed explanation of why this story is better",
    "key_differences": ["...", "...", "..."],
    "score_a": 7.5,
    "score_b": 8.2
}}
"""

    def evaluate_single(self, story: str, genre: str) -> Dict:
        """Evaluate a single story"""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert creative writing critic. Provide detailed, constructive evaluations."
                },
                {
                    "role": "user",
                    "content": self.evaluation_prompt.format(
                        story=story[:4000],  # Limit length
                        genre=genre
                    )
                }
            ],
            response_format={"type": "json_object"},
            temperature=0.3
        )

        return json.loads(response.choices[0].message.content)

    def compare_stories(
        self,
        story_a: str,
        story_b: str,
        genre: str,
        topic: str,
        requirements: str
    ) -> Dict:
        """Compare two stories head-to-head"""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert creative writing critic. Provide fair, detailed comparisons."
                },
                {
                    "role": "user",
                    "content": self.comparison_prompt.format(
                        story_a=story_a[:4000],
                        story_b=story_b[:4000],
                        genre=genre,
                        topic=topic,
                        requirements=requirements
                    )
                }
            ],
            response_format={"type": "json_object"},
            temperature=0.3
        )

        return json.loads(response.choices[0].message.content)

    def blind_comparison(
        self,
        baseline_story: str,
        rag_story: str,
        genre: str,
        topic: str,
        requirements: str
    ) -> Dict:
        """
        Blind comparison: randomly assign A/B labels to hide which is RAG vs baseline
        """

        import random

        # Randomly assign positions
        if random.random() > 0.5:
            story_a, story_b = baseline_story, rag_story
            a_method, b_method = "baseline", "rag"
        else:
            story_a, story_b = rag_story, baseline_story
            a_method, b_method = "rag", "baseline"

        comparison = self.compare_stories(
            story_a, story_b, genre, topic, requirements
        )

        # Determine actual winner
        if comparison['winner'] == 'A':
            actual_winner = a_method
        else:
            actual_winner = b_method

        return {
            "comparison": comparison,
            "actual_winner": actual_winner,
            "rag_won": actual_winner == "rag",
            "position_mapping": {
                "A": a_method,
                "B": b_method
            }
        }


def evaluate_story_pair(
    evaluator: StoryEvaluator,
    pair: Dict
) -> Dict:
    """Evaluate a baseline/RAG story pair"""

    baseline = pair['baseline']
    rag = pair['rag']
    metadata = pair['metadata']

    console.print("\n[bold cyan]Evaluating story pair...[/bold cyan]")

    # Individual evaluations
    console.print("[yellow]Evaluating baseline story...[/yellow]")
    baseline_eval = evaluator.evaluate_single(
        baseline['story'],
        metadata['genre']
    )

    console.print("[yellow]Evaluating RAG story...[/yellow]")
    rag_eval = evaluator.evaluate_single(
        rag['story'],
        metadata['genre']
    )

    # Blind comparison
    console.print("[yellow]Running blind comparison...[/yellow]")
    comparison = evaluator.blind_comparison(
        baseline['story'],
        rag['story'],
        metadata['genre'],
        metadata['topic'],
        metadata['requirements']
    )

    results = {
        "baseline_evaluation": baseline_eval,
        "rag_evaluation": rag_eval,
        "blind_comparison": comparison,
        "metadata": metadata,
        "summary": {
            "baseline_overall_score": baseline_eval['overall_score'],
            "rag_overall_score": rag_eval['overall_score'],
            "rag_won_comparison": comparison['rag_won'],
            "rag_score_advantage": rag_eval['overall_score'] - baseline_eval['overall_score']
        }
    }

    # Display results
    _display_evaluation_results(results)

    return results


def _display_evaluation_results(results: Dict):
    """Display evaluation results in a nice format"""

    console.print("\n" + "="*70)
    console.print("[bold]EVALUATION RESULTS[/bold]")
    console.print("="*70)

    # Scores table
    table = Table(title="Scores Comparison")
    table.add_column("Metric", style="cyan")
    table.add_column("Baseline", justify="right")
    table.add_column("RAG", justify="right")
    table.add_column("Difference", justify="right")

    baseline_eval = results['baseline_evaluation']
    rag_eval = results['rag_evaluation']

    for criterion in ['coherence', 'creativity', 'character_depth',
                      'plot_structure', 'engagement', 'genre_appropriateness']:
        b_score = baseline_eval['scores'][criterion]['score']
        r_score = rag_eval['scores'][criterion]['score']
        diff = r_score - b_score

        diff_color = "green" if diff > 0 else "red" if diff < 0 else "yellow"

        table.add_row(
            criterion.replace('_', ' ').title(),
            f"{b_score}/10",
            f"{r_score}/10",
            f"[{diff_color}]{diff:+.1f}[/{diff_color}]"
        )

    # Overall scores
    b_overall = baseline_eval['overall_score']
    r_overall = rag_eval['overall_score']
    diff_overall = r_overall - b_overall

    diff_color = "green" if diff_overall > 0 else "red" if diff_overall < 0 else "yellow"

    table.add_row(
        "[bold]OVERALL[/bold]",
        f"[bold]{b_overall}/10[/bold]",
        f"[bold]{r_overall}/10[/bold]",
        f"[bold {diff_color}]{diff_overall:+.1f}[/bold {diff_color}]"
    )

    console.print(table)

    # Blind comparison result
    comparison = results['blind_comparison']

    console.print(f"\n[bold]Blind Comparison Winner:[/bold]", end=" ")

    if comparison['rag_won']:
        console.print("[bold green]RAG ✓[/bold green]")
    else:
        console.print("[bold red]Baseline[/bold red]")

    console.print(f"Confidence: {comparison['comparison']['confidence']:.1%}")

    console.print(f"\n[bold]Reasoning:[/bold]")
    console.print(comparison['comparison']['reasoning'])

    console.print(f"\n[bold]RAG Strengths:[/bold]")
    for strength in rag_eval['strengths']:
        console.print(f"  [green]✓[/green] {strength}")

    console.print(f"\n[bold]RAG Weaknesses:[/bold]")
    for weakness in rag_eval['weaknesses']:
        console.print(f"  [red]✗[/red] {weakness}")

    console.print("="*70 + "\n")


if __name__ == "__main__":
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    load_dotenv()

    # Load a test generation
    test_file = Path("validation/results/test_generation.json")

    if not test_file.exists():
        console.print("[red]Error: Run story_generator.py first to create test generation[/red]")
        exit(1)

    with open(test_file) as f:
        pair = json.load(f)

    # Evaluate
    api_key = os.getenv("OPENAI_API_KEY")
    evaluator = StoryEvaluator(api_key)

    results = evaluate_story_pair(evaluator, pair)

    # Save evaluation results
    output_file = Path("validation/results/test_evaluation.json")

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    console.print(f"[green]✓[/green] Saved evaluation to {output_file}")
