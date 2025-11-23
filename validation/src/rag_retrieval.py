"""
RAG Retrieval System
Retrieves relevant papers and techniques based on story requirements
"""

import json
import chromadb
from pathlib import Path
from typing import List, Dict, Optional
from openai import OpenAI
from rich.console import Console

console = Console()


class RAGRetriever:
    """Retrieves relevant papers using RAG"""

    def __init__(self, api_key: str, collection_name: str = "story_papers"):
        self.client = OpenAI(api_key=api_key)
        self.chroma_client = chromadb.Client()
        self.collection_name = collection_name
        self.collection = None

    def create_collection(self, extractions: List[Dict]):
        """Create vector database from paper extractions"""

        console.print(f"[blue]Creating ChromaDB collection: {self.collection_name}[/blue]")

        # Delete existing collection if it exists
        try:
            self.chroma_client.delete_collection(self.collection_name)
        except:
            pass

        # Create new collection
        self.collection = self.chroma_client.create_collection(
            name=self.collection_name,
            metadata={"description": "Story generation research papers"}
        )

        # Prepare documents and metadata
        documents = []
        metadatas = []
        ids = []

        for idx, ext in enumerate(extractions):
            # Create rich text representation for embedding
            doc_text = f"""
Title: {ext['title']}

Methodology: {ext['methodology']}

Techniques: {', '.join(ext['techniques'])}

Best for genres: {', '.join(ext['genres'])}

Architecture: {ext['architecture']}

Key Insights:
{chr(10).join(f'- {insight}' for insight in ext['insights'])}

Example Prompts:
{chr(10).join(f'- {prompt}' for prompt in ext.get('prompts', [])[:2])}
            """.strip()

            documents.append(doc_text)

            # Metadata for filtering
            metadatas.append({
                "title": ext['title'],
                "architecture": ext['architecture'],
                "complexity": ext.get('complexity', 0),
                "genres": json.dumps(ext['genres']),
                "techniques": json.dumps(ext['techniques'])
            })

            ids.append(f"paper_{idx}")

        # Get embeddings from OpenAI
        console.print("[blue]Generating embeddings...[/blue]")
        embeddings = self._get_embeddings(documents)

        # Add to collection
        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

        console.print(f"[green]✓[/green] Added {len(documents)} papers to vector database")

    def _get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Get embeddings from OpenAI"""

        embeddings = []

        for text in texts:
            response = self.client.embeddings.create(
                model="text-embedding-3-large",
                input=text[:8000]  # Limit length
            )
            embeddings.append(response.data[0].embedding)

        return embeddings

    def retrieve(
        self,
        query: str,
        genre: Optional[str] = None,
        top_k: int = 3
    ) -> List[Dict]:
        """Retrieve relevant papers for a query"""

        if self.collection is None:
            raise ValueError("Collection not initialized. Call create_collection() first.")

        # Get query embedding
        query_embedding = self._get_embeddings([query])[0]

        # Build where clause for metadata filtering
        where_clause = None
        if genre:
            # This is a simple approach - in production we'd use more sophisticated filtering
            where_clause = {"genres": {"$contains": genre}}

        # Query collection
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            # where=where_clause  # Uncomment when metadata filtering is needed
        )

        # Format results
        retrieved_papers = []

        for i in range(len(results['ids'][0])):
            paper = {
                "id": results['ids'][0][i],
                "title": results['metadatas'][0][i]['title'],
                "content": results['documents'][0][i],
                "distance": results['distances'][0][i] if 'distances' in results else None,
                "metadata": results['metadatas'][0][i]
            }
            retrieved_papers.append(paper)

        return retrieved_papers

    def load_existing_collection(self):
        """Load existing collection"""
        try:
            self.collection = self.chroma_client.get_collection(self.collection_name)
            console.print(f"[green]✓[/green] Loaded existing collection: {self.collection_name}")
        except:
            console.print(f"[yellow]Collection {self.collection_name} not found[/yellow]")


def analyze_story_request(request: str, client: OpenAI) -> Dict:
    """Analyze story request to extract genre, requirements, etc."""

    analysis_prompt = f"""
Analyze this story generation request and extract:

1. Primary genre
2. Secondary genres (if any)
3. Key requirements or constraints
4. Techniques that would be useful

Request: {request}

Respond in JSON:
{{
    "primary_genre": "...",
    "secondary_genres": ["...", "..."],
    "requirements": ["...", "..."],
    "needed_techniques": ["...", "..."]
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a story analysis expert."},
            {"role": "user", "content": analysis_prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.3
    )

    return json.loads(response.choices[0].message.content)


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    # Load paper extractions
    extractions_file = Path("validation/data/paper_extractions.json")

    if not extractions_file.exists():
        console.print("[red]Error: Run paper_extractor.py first to create extractions[/red]")
        exit(1)

    with open(extractions_file) as f:
        extractions = json.load(f)

    # Initialize retriever
    api_key = os.getenv("OPENAI_API_KEY")
    retriever = RAGRetriever(api_key)

    # Create collection
    retriever.create_collection(extractions)

    # Test retrieval
    console.print("\n[bold]Testing RAG Retrieval[/bold]\n")

    test_queries = [
        "Write a suspenseful mystery story with plot twists",
        "Create a character-driven drama with psychological depth",
        "Generate a fast-paced thriller with good pacing"
    ]

    for query in test_queries:
        console.print(f"[cyan]Query:[/cyan] {query}")

        results = retriever.retrieve(query, top_k=3)

        console.print(f"[green]Retrieved {len(results)} papers:[/green]")
        for i, paper in enumerate(results, 1):
            console.print(f"  {i}. {paper['title']}")
            if paper['distance']:
                console.print(f"     Distance: {paper['distance']:.3f}")

        console.print()
