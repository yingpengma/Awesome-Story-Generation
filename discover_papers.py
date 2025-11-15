import json
import os
import re
import subprocess
import requests
import configparser
from datetime import datetime, timedelta

# --- Configuration ---
CITATIONS_FILE = 'citations.json'
README_FILE = 'README.md'
CONFIG_FILE = 'config.ini'
SEMANTIC_SCHOLAR_API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
NEW_PAPER_SECTION_HEADER = "### Newly Discovered"
PAPERS_SECTION_HEADER = "## Papers"

def run_command(command):
    """Runs a shell command and logs its output."""
    print(f"🔩 Running command: {' '.join(command)}")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=60)
        print(f"✅ Command successful:\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with error:\n{e.stderr}")
        return False
    except subprocess.TimeoutExpired as e:
        print(f"⌛ Command timed out: {e}")
        return False

def load_existing_papers():
    """Loads paper titles from the citations.json file."""
    try:
        with open(CITATIONS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return {title.lower() for title in data.get('papers', {})}
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"⚠️ Could not load or parse {CITATIONS_FILE}. Starting with an empty set.")
        return set()

def search_semantic_scholar(keywords, days_to_search, existing_titles):
    """Searches Semantic Scholar for new papers."""
    print(f"🔍 Searching Semantic Scholar for new papers...")
    query = " OR ".join(f'"{k}"' for k in keywords)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_to_search)

    params = {
        "query": query,
        "fields": "title,authors,abstract,url,year,venue",
        "publicationDate": f"{start_date.strftime('%Y/%m/%d')}-{end_date.strftime('%Y/%m/%d')}",
        "limit": 100
    }
    headers = {"User-Agent": "Awesome-Story-Generation-Discovery-Bot/1.0"}

    try:
        response = requests.get(SEMANTIC_SCHOLAR_API_URL, params=params, headers=headers)
        if response.status_code == 429:
            print("⌛ Rate limited by Semantic Scholar API. Skipping this run.")
            return []
        response.raise_for_status()
        results = response.json()

        new_papers = []
        for paper in results.get('data', []):
            title = paper.get('title')
            if title and title.lower() not in existing_titles:
                new_papers.append({
                    "title": title,
                    "authors": [author['name'] for author in paper.get('authors', [])],
                    "year": paper.get('year', 'N/A'),
                    "venue": paper.get('venue', 'ArXiv'),
                    "url": paper.get('url', '#'),
                    "abstract": paper.get('abstract', 'No abstract available.')
                })
                existing_titles.add(title.lower())
        return new_papers
    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        return []

def add_paper_to_readme(content, paper):
    """Adds a new paper entry to the README content."""
    new_entry = (
        f"- `{paper['venue']}-{paper['year']}` **{paper['title']}** "
        f"[[paper]]({paper['url']}) "
        f"[{', '.join(paper['authors'])}] "
        f"[![](https://img.shields.io/badge/citation-0-blue)]()"
    )

    if NEW_PAPER_SECTION_HEADER in content:
        return re.sub(f"({re.escape(NEW_PAPER_SECTION_HEADER)})", f"\\1\n{new_entry}", content)
    else:
        return re.sub(f"({re.escape(PAPERS_SECTION_HEADER)})", f"\\1\n\n{NEW_PAPER_SECTION_HEADER}\n{new_entry}", content)

def add_paper_to_citations(data, paper):
    """Adds a new paper to the citations data."""
    data['papers'][paper['title']] = {
        "title": paper['title'], "citations": 0, "last_updated": "1970-01-01-00:00:00"
    }
    return data

def create_pull_request(paper):
    """Creates a branch and pull request for a single paper."""
    slug = re.sub(r'[^a-z0-9]+', '-', paper['title'].lower()).strip('-')
    branch_name = f"paper/add-{slug[:50]}"

    try:
        run_command(["git", "checkout", "-b", branch_name])

        with open(README_FILE, 'r', encoding='utf-8') as f:
            readme = f.read()
        with open(CITATIONS_FILE, 'r', encoding='utf-8') as f:
            citations = json.load(f)

        new_readme = add_paper_to_readme(readme, paper)
        new_citations = add_paper_to_citations(citations, paper)

        with open(README_FILE, 'w', encoding='utf-8') as f:
            f.write(new_readme)
        with open(CITATIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(new_citations, f, indent=2, ensure_ascii=False)

        run_command(["git", "add", README_FILE, CITATIONS_FILE])
        run_command(["git", "commit", "-m", f"feat(papers): add '{paper['title']}'"])
        run_command(["git", "push", "--set-upstream", "origin", branch_name])

        if os.environ.get("CI"):
            pr_title = f"Add new paper: {paper['title']}"
            pr_body = (
                f"This PR was automatically opened by the Paper Discovery Bot.\n\n"
                f"**Title:** {paper['title']}\n"
                f"**Authors:** {', '.join(paper['authors'])}\n"
                f"**URL:** {paper['url']}\n\n"
                f"**Abstract:**\n> {paper.get('abstract')}"
            )
            run_command(["gh", "pr", "create", "--title", pr_title, "--body", pr_body, "--base", "main"])
        else:
            print("✅ Skipping PR creation in local environment.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        # Return to the main branch to ensure a clean state for the next run or iteration.
        # The temporary branch will be cleaned up automatically when the PR is merged.
        print("Returning to main branch...")
        run_command(["git", "checkout", "main"])

def main():
    """Main function."""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    keywords = config.get('discovery', 'keywords').strip().split('\n')
    days_to_search = config.getint('discovery', 'days_to_search')

    # Configure git only if in CI
    if os.environ.get("CI"):
        run_command(["git", "config", "--global", "user.name", "Paper Discovery Bot"])
        run_command(["git", "config", "--global", "user.email", "discovery-bot@users.noreply.github.com"])

    existing_titles = load_existing_papers()
    print(f"📚 Found {len(existing_titles)} existing papers.")

    new_papers = search_semantic_scholar(keywords, days_to_search, existing_titles)

    if not new_papers:
        print("\n✅ No new papers found.")
    else:
        print(f"\n✨ Found {len(new_papers)} new paper(s) to process.")
        for paper in new_papers:
            print(f"\n---\n🤖 Processing paper: {paper['title']}\n---")
            create_pull_request(paper)

    print("✅ Discovery process finished.")

if __name__ == "__main__":
    main()