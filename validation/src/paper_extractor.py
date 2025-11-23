"""
Paper Technique Extractor
Extracts story generation techniques from research papers
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional
from openai import OpenAI
from rich.console import Console
from rich.progress import Progress

console = Console()


class PaperExtractor:
    """Extract techniques and metadata from research papers"""

    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.extraction_prompt = """
You are a research paper analyzer specializing in story generation techniques.

Analyze this section from a research paper and extract:

1. **Core Methodology** (2-3 sentences): The main approach or technique
2. **Key Techniques**: List of specific techniques mentioned
3. **Applicable Genres**: Which story genres this works best for
4. **Prompts/Instructions**: Any specific prompts or instructions mentioned
5. **Architecture**: Type of system (e.g., multi-agent, iterative, RAG, fine-tuning)
6. **Complexity**: Implementation difficulty (1-5, where 5 is most complex)
7. **Key Insights**: 2-3 actionable insights for story generation

Paper Title: {title}
Section: {section_name}

Content:
{content}

Respond in valid JSON format:
{{
    "methodology": "...",
    "techniques": ["...", "..."],
    "genres": ["...", "..."],
    "prompts": ["...", "..."],
    "architecture": "...",
    "complexity": 3,
    "insights": ["...", "..."]
}}
"""

    def extract_from_text(
        self,
        title: str,
        content: str,
        section_name: str = "full_paper"
    ) -> Dict:
        """Extract techniques from paper text"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Using cheaper model for extraction
                messages=[
                    {
                        "role": "system",
                        "content": "You are a research paper analysis expert. Extract information in valid JSON format."
                    },
                    {
                        "role": "user",
                        "content": self.extraction_prompt.format(
                            title=title,
                            section_name=section_name,
                            content=content[:4000]  # Limit content length
                        )
                    }
                ],
                response_format={"type": "json_object"},
                temperature=0.3
            )

            extracted = json.loads(response.choices[0].message.content)

            # Add metadata
            extracted["title"] = title
            extracted["section"] = section_name
            extracted["content_preview"] = content[:500]

            return extracted

        except Exception as e:
            console.print(f"[red]Error extracting from {title}: {e}[/red]")
            return {
                "title": title,
                "error": str(e),
                "methodology": "",
                "techniques": [],
                "genres": [],
                "prompts": [],
                "architecture": "unknown",
                "complexity": 0,
                "insights": []
            }

    def create_manual_extraction(
        self,
        title: str,
        methodology: str,
        techniques: List[str],
        genres: List[str],
        prompts: List[str],
        architecture: str,
        complexity: int,
        insights: List[str]
    ) -> Dict:
        """Manually create an extraction (for human curation)"""

        return {
            "title": title,
            "methodology": methodology,
            "techniques": techniques,
            "genres": genres,
            "prompts": prompts,
            "architecture": architecture,
            "complexity": complexity,
            "insights": insights,
            "manually_curated": True
        }


def create_sample_extractions() -> List[Dict]:
    """
    Create sample manually-curated extractions for top papers
    This is the Phase 1 approach: human curation of top 10 papers
    """

    extractions = []

    # Paper 1: Creating Suspenseful Stories
    extractions.append({
        "title": "Creating Suspenseful Stories: Iterative Planning with Large Language Models",
        "methodology": "Iterative planning approach where the system creates a high-level outline first, then progressively refines each section while maintaining suspense through strategic information withholding and foreshadowing.",
        "techniques": [
            "iterative_planning",
            "information_withholding",
            "strategic_foreshadowing",
            "outline_refinement"
        ],
        "genres": ["mystery", "thriller", "suspense", "horror"],
        "prompts": [
            "Create a 5-point outline for a suspenseful {genre} story about {topic}. For each point, specify: (1) plot event, (2) information revealed, (3) information withheld, (4) foreshadowing elements.",
            "Expand outline point {N} into a full scene. Ensure you reveal {revealed_info} while withholding {withheld_info}. Include subtle hints about {foreshadowed_elements}.",
            "Review the story so far for suspense continuity. Identify any information revealed too early or foreshadowing that's too obvious."
        ],
        "architecture": "iterative_planning",
        "complexity": 3,
        "insights": [
            "Suspense comes from controlling information flow - what readers know vs don't know",
            "Outline should specify both reveals and withholds for each plot point",
            "Iterative refinement allows maintaining suspense across long narratives"
        ],
        "manually_curated": True
    })

    # Paper 2: Agents' Room
    extractions.append({
        "title": "Agents' Room: Narrative Generation through Multi-step Collaboration",
        "methodology": "Multiple specialized agents collaborate in steps: story planning, character development, scene writing, and editing. Each agent has a specific role and expertise, working together to produce higher quality narratives.",
        "techniques": [
            "multi_agent_collaboration",
            "role_specialization",
            "iterative_refinement",
            "collaborative_editing"
        ],
        "genres": ["general", "drama", "literary_fiction", "complex_narratives"],
        "prompts": [
            "As the Planning Agent, create a story structure for {topic} with {num_acts} acts.",
            "As the Character Agent, develop detailed profiles for the main characters including personality, motivations, and arcs.",
            "As the Scene Writer, write scene {N} following the plan and character profiles. Stay consistent with previous scenes.",
            "As the Editor Agent, review the complete story for consistency, pacing, and quality. Suggest specific improvements."
        ],
        "architecture": "multi_agent",
        "complexity": 4,
        "insights": [
            "Specialized agents produce better results than single generalist agent",
            "Character consistency improved through dedicated character agent",
            "Iterative collaboration catches errors and improves quality"
        ],
        "manually_curated": True
    })

    # Paper 3: Measuring Psychological Depth
    extractions.append({
        "title": "Measuring Psychological Depth in Language Models",
        "methodology": "Framework for creating psychologically complex characters through explicit modeling of internal states, motivations, beliefs, and emotional arcs. Uses theory-of-mind prompting to develop realistic character psychology.",
        "techniques": [
            "psychological_profiling",
            "theory_of_mind_prompting",
            "internal_state_tracking",
            "motivation_modeling",
            "belief_systems"
        ],
        "genres": ["literary_fiction", "character_driven", "drama", "romance"],
        "prompts": [
            "Create a psychological profile for {character}: core beliefs, fears, desires, defense mechanisms, and attachment style.",
            "Write a scene from {character}'s perspective showing their internal conflict between {desire} and {fear}.",
            "How would {character} react to {situation} given their psychological profile? Consider their beliefs about {relevant_belief}.",
            "Show {character}'s emotional arc from {starting_state} to {ending_state}, making the transition believable and grounded in their psychology."
        ],
        "architecture": "prompt_engineering",
        "complexity": 3,
        "insights": [
            "Explicit psychological profiles create more consistent, believable characters",
            "Internal conflicts drive compelling character-driven narratives",
            "Theory-of-mind prompting helps LLMs model complex psychology"
        ],
        "manually_curated": True
    })

    # Paper 4: Improving Pacing
    extractions.append({
        "title": "Improving Pacing in Long-Form Story Planning",
        "methodology": "Explicit pacing structure that varies tension, action, and reflection across the narrative. Uses pacing curves to plan when to accelerate, decelerate, and maintain story momentum.",
        "techniques": [
            "pacing_curves",
            "tension_management",
            "action_variation",
            "reflection_beats",
            "momentum_control"
        ],
        "genres": ["thriller", "action", "adventure", "epic_fantasy"],
        "prompts": [
            "Plan the pacing for this {length}-chapter story. Specify tension level (1-10) for each chapter.",
            "Write chapter {N} with {tension_level} tension. This is a {pacing_type} section (fast/medium/slow paced).",
            "Insert a reflection beat here where {character} processes recent events. Keep it brief but meaningful.",
            "This is the climax section - write with maximum tension and fast pacing. Short paragraphs, active verbs, urgent tone."
        ],
        "architecture": "plan_and_write",
        "complexity": 2,
        "insights": [
            "Explicit pacing structure prevents stories from feeling monotonous",
            "Vary between action, dialogue, and reflection to maintain engagement",
            "Tension should build in waves, not linearly"
        ],
        "manually_curated": True
    })

    # Paper 5: IBSEN (Director-Actor)
    extractions.append({
        "title": "IBSEN: Director-Actor Agent Collaboration for Controllable and Interactive Drama Script Generation",
        "methodology": "Two-tier agent system with a Director agent managing overall story structure and Actor agents performing characters. Director provides guidance and constraints, Actors improvise dialogue and actions within those constraints.",
        "techniques": [
            "director_actor_model",
            "hierarchical_control",
            "improvisational_dialogue",
            "constraint_based_generation"
        ],
        "genres": ["drama", "screenplay", "dialogue_heavy", "interactive"],
        "prompts": [
            "As Director: Set up scene {N} - location, characters present, objective, emotional tone, and key plot points to cover.",
            "As {character} Actor: Improvise your dialogue and actions in this scene. Stay in character and work toward the scene objective: {objective}.",
            "As Director: Review the scene. Does it accomplish {objectives}? Suggest adjustments to pacing or character actions.",
            "As {character} Actor: Revise your performance based on Director feedback: {feedback}."
        ],
        "architecture": "hierarchical_multi_agent",
        "complexity": 4,
        "insights": [
            "Separation of high-level control (Director) and execution (Actors) improves controllability",
            "Actors improvising within constraints creates natural dialogue",
            "Useful for interactive stories where user can influence Director instructions"
        ],
        "manually_curated": True
    })

    return extractions


if __name__ == "__main__":
    # Create sample extractions
    console.print("[bold green]Creating sample paper extractions...[/bold green]")

    extractions = create_sample_extractions()

    # Save to JSON
    output_dir = Path("validation/data")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "paper_extractions.json"

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(extractions, f, indent=2, ensure_ascii=False)

    console.print(f"[green]✓[/green] Saved {len(extractions)} paper extractions to {output_file}")
    console.print(f"\nExtracted techniques from:")
    for ext in extractions:
        console.print(f"  • {ext['title']}")
