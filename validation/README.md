# RAG Story Generation - Validation Phase

This directory contains code to **validate whether RAG improves story generation quality** using research papers as knowledge sources.

## Overview

**Goal:** Prove that retrieving and applying research techniques via RAG produces better stories than baseline GPT-4.

**Success Criteria:**
- RAG wins ≥60% of blind comparisons
- Average quality score ≥6.0/10
- Shows positive improvement over baseline
- Cost per story <$5

**Timeline:** 30 days | **Budget:** $5,000

---

## Quick Start

### 1. Install Dependencies

```bash
cd validation
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file:

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

```.env
OPENAI_API_KEY=your-key-here
```

### 3. Run Full Validation

```bash
python run_validation.py
```

This will:
1. Extract techniques from 5 research papers
2. Build RAG vector database
3. Generate 5 story pairs (RAG vs baseline)
4. Evaluate using LLM-as-judge
5. Produce final validation report

**Expected Runtime:** ~15-20 minutes
**Expected Cost:** ~$3-5 in OpenAI API calls

---

## Directory Structure

```
validation/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── run_validation.py         # Main orchestrator script
│
├── configs/
│   └── config.yaml          # Configuration settings
│
├── src/
│   ├── paper_extractor.py   # Extract techniques from papers
│   ├── rag_retrieval.py     # RAG retrieval system
│   ├── story_generator.py   # Generate stories (with/without RAG)
│   └── evaluator.py         # Evaluate and compare stories
│
├── data/
│   └── paper_extractions.json  # Extracted paper techniques (generated)
│
└── results/
    ├── pair_*.json          # Individual story pairs
    └── validation_report_*.json  # Final validation reports
```

---

## How It Works

### Phase 1: Paper Technique Extraction

Manually curate techniques from top 5 research papers:

1. **"Creating Suspenseful Stories"** - Iterative planning, information withholding
2. **"Agents' Room"** - Multi-agent collaboration
3. **"Measuring Psychological Depth"** - Character psychology techniques
4. **"Improving Pacing"** - Pacing curves, tension management
5. **"IBSEN"** - Director-actor model

**Output:** `data/paper_extractions.json`

### Phase 2: RAG Setup

Build vector database with ChromaDB:
- Each paper → Multiple embeddings (methodology, insights, prompts)
- Hybrid search: semantic similarity + metadata filtering
- Retrieves top 3 most relevant papers for each story request

### Phase 3: Story Generation

For each test prompt, generate TWO versions:

**Baseline:**
```
User prompt → GPT-4 → Story
```

**RAG-Enhanced:**
```
User prompt → Analyze requirements → RAG retrieves papers →
Extract techniques → GPT-4 with techniques → Story
```

### Phase 4: Evaluation

**LLM-as-Judge Evaluation:**
- Score both stories on 6 criteria (coherence, creativity, character depth, plot structure, engagement, genre appropriateness)
- Blind comparison (stories labeled A/B randomly)
- Track which method wins

**Criteria:**
- Coherence (1-10)
- Creativity (1-10)
- Character Depth (1-10)
- Plot Structure (1-10)
- Engagement (1-10)
- Genre Appropriateness (1-10)

### Phase 5: Analysis

Calculate:
- RAG win rate (target: ≥60%)
- Average quality scores
- Score improvement
- Cost per story

**Decision Point:**
- ✅ If validation passes → Proceed to MVP
- ⚠️ If mixed results → Iterate and refine
- ❌ If validation fails → Pivot to alternative approach

---

## Running Individual Components

### Just Extract Papers

```bash
cd validation
python src/paper_extractor.py
```

### Test RAG Retrieval

```bash
python src/rag_retrieval.py
```

### Generate One Story Pair

```bash
python src/story_generator.py
```

### Evaluate Existing Pair

```bash
python src/evaluator.py
```

---

## Configuration

Edit `configs/config.yaml` to customize:

### Models
```yaml
models:
  embedding: "text-embedding-3-large"
  generation: "gpt-4o"
  generation_fast: "gpt-4o-mini"  # For testing
  evaluation: "gpt-4o"
```

### RAG Settings
```yaml
rag:
  vector_db: "chromadb"
  chunk_size: 1000
  chunk_overlap: 200
  top_k: 3  # Papers to retrieve per query
```

### Test Prompts
```yaml
generation:
  test_prompts:
    - genre: "mystery"
      topic: "A detective investigates a disappearance"
      requirements: "suspenseful, plot twists"
```

### Success Thresholds
```yaml
validation:
  success_threshold: 0.60  # 60% win rate required
  min_quality_score: 6.0   # Minimum average score
  max_cost_per_story: 5.00
```

---

## Expected Results

Based on similar RAG applications, we expect:

**Optimistic Case:**
- RAG win rate: 70-80%
- Average score improvement: +1.0-1.5 points
- Clear quality advantage

**Base Case:**
- RAG win rate: 60-70%
- Average score improvement: +0.5-1.0 points
- Moderate quality advantage

**Pessimistic Case:**
- RAG win rate: 50-60%
- Average score improvement: +0.0-0.5 points
- Marginal or no advantage

---

## Cost Estimation

**Per Story Pair:**
- Embeddings: $0.10
- Story generation (2x): $0.50
- Evaluation: $0.30
- **Total: ~$1.00 per pair**

**Full Validation (5 pairs):**
- **Total: ~$5.00**

**Extended Testing (20 pairs):**
- **Total: ~$20.00**

---

## Troubleshooting

### "OPENAI_API_KEY not found"

Create `.env` file with your API key:
```bash
echo "OPENAI_API_KEY=sk-..." > .env
```

### "ChromaDB collection not found"

Delete existing collection:
```python
retriever.chroma_client.delete_collection("validation_*")
```

Then re-run.

### Stories are too short/long

Adjust in `config.yaml`:
```yaml
generation:
  max_length: 2000  # Target word count
```

### Evaluation takes too long

Use faster model for evaluation:
```yaml
models:
  evaluation: "gpt-4o-mini"  # Faster, cheaper
```

---

## Next Steps After Validation

### If Validation Passes (≥60% win rate)

✅ **PROCEED TO MVP**

1. Extract all 85 papers (not just top 5)
2. Build production RAG system with Pinecone/Weaviate
3. Implement multi-agent collaboration
4. Create web interface
5. Launch beta with 20 users

**Timeline:** 60 days
**Budget:** $30K

### If Validation Shows Promise (50-60% win rate)

⚠️ **ITERATE AND IMPROVE**

1. Extract more papers (10-15 papers)
2. Improve technique extraction prompts
3. Experiment with different retrieval strategies
4. Test multi-agent approach
5. Re-run validation

**Timeline:** 14 days
**Budget:** $2K

### If Validation Fails (<50% win rate)

❌ **PIVOT**

Consider alternatives:
1. **Fine-tuning approach:** Train model on story datasets instead of RAG
2. **Hybrid:** Use papers for training data, not runtime retrieval
3. **Simpler MVP:** Focus on one genre/technique
4. **Research platform:** Return to commercializing paper list (original idea)

---

## Technical Details

### RAG Architecture

```
User Request
    ↓
Requirement Analysis (GPT-4o-mini)
    ↓
Query Embedding (text-embedding-3-large)
    ↓
Vector Search (ChromaDB)
    ↓
Retrieve Top 3 Papers
    ↓
Extract Techniques
    ↓
Build Enhanced Prompt with Techniques
    ↓
Generate Story (GPT-4o)
    ↓
Story Output
```

### Evaluation Architecture

```
Story Pair (Baseline + RAG)
    ↓
    ├─→ Individual Evaluation (GPT-4o)
    │   ├─ Coherence: X/10
    │   ├─ Creativity: X/10
    │   ├─ Character Depth: X/10
    │   ├─ Plot Structure: X/10
    │   ├─ Engagement: X/10
    │   └─ Genre Appropriateness: X/10
    │
    └─→ Blind Comparison (GPT-4o)
        ├─ Randomly assign A/B labels
        ├─ Compare stories
        ├─ Pick winner
        └─ Return actual winner (RAG or Baseline)
```

---

## Paper Extraction Schema

Each paper extraction includes:

```json
{
  "title": "Paper title",
  "methodology": "Core approach in 2-3 sentences",
  "techniques": ["technique1", "technique2"],
  "genres": ["mystery", "thriller"],
  "prompts": ["Example prompt template 1", "..."],
  "architecture": "multi_agent | iterative_planning | prompt_engineering",
  "complexity": 1-5,
  "insights": ["Key insight 1", "Key insight 2"],
  "manually_curated": true
}
```

---

## FAQ

**Q: Why only 5 papers for validation?**
A: Manual curation ensures quality. We're validating the concept, not building production system yet.

**Q: Can I use Claude instead of GPT-4?**
A: Yes! Update `config.yaml` to use Anthropic API. Install `anthropic` package and modify generator code.

**Q: How do I add more test prompts?**
A: Edit `configs/config.yaml` under `generation.test_prompts`.

**Q: Can I use local LLMs?**
A: Yes, but quality may suffer. Consider Llama 3.1 70B+ for comparable results.

**Q: What if I don't have $5K budget?**
A: Run with 2-3 test prompts instead of 5. Use `gpt-4o-mini` for generation. Total cost: ~$1-2.

---

## Support

For issues or questions:
1. Check troubleshooting section above
2. Review code comments in `src/` files
3. Open GitHub issue on repository

---

## License

This validation code is provided as-is for research and development purposes.

---

**Last Updated:** November 23, 2025
**Version:** 1.0.0
**Status:** Ready for validation
