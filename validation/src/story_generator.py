"""
Story Generator
Generates stories with and without RAG techniques
"""

import json
from typing import Dict, List, Optional
from openai import OpenAI
from rich.console import Console
from rag_retrieval import RAGRetriever, analyze_story_request

console = Console()


class StoryGenerator:
    """Generate stories using different approaches"""

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate_baseline(
        self,
        genre: str,
        topic: str,
        requirements: str,
        max_length: int = 2000
    ) -> Dict:
        """Generate story using baseline GPT-4 (no RAG)"""

        prompt = f"""Write a {genre} story about: {topic}

Requirements: {requirements}

Target length: approximately {max_length} words

Write an engaging, well-structured story that fulfills the requirements."""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a creative writing assistant. Write engaging, well-crafted stories."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=3000
        )

        story = response.choices[0].message.content

        return {
            "story": story,
            "method": "baseline",
            "genre": genre,
            "topic": topic,
            "requirements": requirements,
            "prompt_used": prompt
        }

    def generate_with_rag(
        self,
        genre: str,
        topic: str,
        requirements: str,
        retriever: RAGRetriever,
        max_length: int = 2000
    ) -> Dict:
        """Generate story using RAG-retrieved techniques"""

        # Step 1: Analyze request
        request = f"Genre: {genre}, Topic: {topic}, Requirements: {requirements}"

        analysis = analyze_story_request(request, self.client)

        console.print(f"[blue]Request Analysis:[/blue]")
        console.print(f"  Primary genre: {analysis['primary_genre']}")
        console.print(f"  Needed techniques: {', '.join(analysis['needed_techniques'][:3])}")

        # Step 2: Retrieve relevant papers
        console.print(f"[blue]Retrieving relevant papers...[/blue]")

        retrieved_papers = retriever.retrieve(
            query=request,
            genre=genre,
            top_k=3
        )

        console.print(f"[green]Retrieved papers:[/green]")
        for paper in retrieved_papers:
            console.print(f"  • {paper['title']}")

        # Step 3: Extract techniques from papers
        techniques_context = self._build_techniques_context(retrieved_papers)

        # Step 4: Generate story using techniques
        rag_prompt = f"""You are a creative writing assistant with access to research-backed story generation techniques.

RETRIEVED TECHNIQUES:
{techniques_context}

TASK:
Write a {genre} story about: {topic}

Requirements: {requirements}

Target length: approximately {max_length} words

INSTRUCTIONS:
1. Review the retrieved techniques above
2. Select the most relevant techniques for this story
3. Apply those techniques while writing
4. Create an engaging, well-structured story that fulfills the requirements

Focus on using the research-backed approaches to improve quality."""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a creative writing assistant who applies research-backed techniques to generate high-quality stories."
                },
                {
                    "role": "user",
                    "content": rag_prompt
                }
            ],
            temperature=0.7,
            max_tokens=3000
        )

        story = response.choices[0].message.content

        return {
            "story": story,
            "method": "rag",
            "genre": genre,
            "topic": topic,
            "requirements": requirements,
            "retrieved_papers": [p['title'] for p in retrieved_papers],
            "techniques_used": analysis['needed_techniques'],
            "prompt_used": rag_prompt
        }

    def _build_techniques_context(self, papers: List[Dict]) -> str:
        """Build context string from retrieved papers"""

        context_parts = []

        for i, paper in enumerate(papers, 1):
            # Extract key information from paper content
            context_parts.append(f"""
═══════════════════════════════════════════
PAPER {i}: {paper['title']}
═══════════════════════════════════════════

{paper['content']}
""")

        return "\n".join(context_parts)


def generate_story_pair(
    generator: StoryGenerator,
    retriever: RAGRetriever,
    genre: str,
    topic: str,
    requirements: str
) -> Dict:
    """Generate both baseline and RAG versions for comparison"""

    console.print(f"\n[bold cyan]Generating story pair:[/bold cyan]")
    console.print(f"  Genre: {genre}")
    console.print(f"  Topic: {topic}")
    console.print(f"  Requirements: {requirements}")
    console.print()

    # Generate baseline
    console.print("[yellow]Generating baseline story...[/yellow]")
    baseline = generator.generate_baseline(genre, topic, requirements)

    console.print("[green]✓[/green] Baseline complete")
    console.print(f"  Length: {len(baseline['story'].split())} words\n")

    # Generate RAG version
    console.print("[yellow]Generating RAG story...[/yellow]")
    rag = generator.generate_with_rag(
        genre, topic, requirements, retriever
    )

    console.print("[green]✓[/green] RAG complete")
    console.print(f"  Length: {len(rag['story'].split())} words")
    console.print(f"  Papers used: {len(rag['retrieved_papers'])}\n")

    return {
        "baseline": baseline,
        "rag": rag,
        "metadata": {
            "genre": genre,
            "topic": topic,
            "requirements": requirements
        }
    }


if __name__ == "__main__":
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    load_dotenv()

    # Load extractions and setup RAG
    extractions_file = Path("validation/data/paper_extractions.json")

    if not extractions_file.exists():
        console.print("[red]Error: Run paper_extractor.py first[/red]")
        exit(1)

    with open(extractions_file) as f:
        extractions = json.load(f)

    api_key = os.getenv("OPENAI_API_KEY")

    retriever = RAGRetriever(api_key)
    retriever.create_collection(extractions)

    generator = StoryGenerator(api_key)

    # Test generation
    pair = generate_story_pair(
        generator=generator,
        retriever=retriever,
        genre="mystery",
        topic="A detective investigates a disappearance in a small coastal town",
        requirements="suspenseful, plot twists, complex character psychology"
    )

    # Save results
    output_file = Path("validation/results/test_generation.json")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(pair, f, indent=2)

    console.print(f"\n[green]✓[/green] Saved results to {output_file}")

    # Display preview
    console.print("\n[bold]Baseline Story Preview:[/bold]")
    console.print(pair['baseline']['story'][:500] + "...\n")

    console.print("[bold]RAG Story Preview:[/bold]")
    console.print(pair['rag']['story'][:500] + "...\n")

    console.print(f"[cyan]Papers used in RAG version:[/cyan]")
    for paper in pair['rag']['retrieved_papers']:
        console.print(f"  • {paper}")
