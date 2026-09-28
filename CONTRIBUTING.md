# Contributing

Thanks for helping keep this list useful! You can recommend a paper by opening a [paper recommendation issue](https://github.com/yingpengma/Awesome-Story-Generation/issues/new/choose), or add it yourself with a pull request.

## What we include

This list collects research on **AI creating narrative works in the era of large language models**, in any form: novels and short stories, screenplays and drama, games and interactive narrative, narrative world models, comics, illustrated stories and video.

A paper is included when it meets all of the following:

1. **Topic.** It generates stories, evaluates generated stories, or studies how people create stories with AI.
   - Story *understanding* work (summarization, narrative QA, literary analysis) is included only if it directly helps generation, for example as an evaluator or a consistency checker.
   - General long-text and writing methods are welcome. Generic alignment, generic LLM-as-a-judge and generic agent frameworks are not.
   - Role-play papers are included only when the character acts inside a story or plot. Persona chat and companion bots are out of scope.
   - Pure figurative-language work (similes, metaphors) is out of scope.
   - Visual and video work is included only at the story level (plot, script, shot planning, narrative reasoning). Work that only improves rendering quality or character consistency across frames is out of scope.
   - World models are included when characters or narrative drive the generated world, not for navigation or physics alone.
2. **Time.** Published in 2023 or later.
3. **Venue.** Accepted at a major venue: ACL, EMNLP, NAACL, EACL, COLING (Findings included), TACL, COLM, ICLR, ICML, NeurIPS, CVPR, ICCV, ECCV, AAAI, IJCAI or CHI. Papers from other venues, workshops and arXiv preprints are included if they average **10 or more citations per year**. Preprints less than a year old are judged case by case on their contribution.

We do not list commercial products, paid or gated datasets, or promotional tool and prompt collections.

## Where a paper goes

The list has four sections, ordered from the most specific to the most general, followed by surveys:

- **Beyond Text**: Interactive Drama · Games · World Models · Screenplays · Visual2Story · Story2Visual
- **Text Stories**: Planning · Coherence · Characters · Creativity · Training
- **Evaluation**: Benchmarks · Metrics · Analyses
- **Co-creation**: Tools · User Studies
- **Surveys**

Each paper appears in exactly one topic, decided in this order:

1. Human-centered systems and user studies → **Co-creation**
2. Work on anything other than a plain written story (interactive drama, games, world models, screenplays, images, comics, video) → the matching **Beyond Text** topic, including its benchmarks
3. Benchmarks, metrics, datasets and analyses of written stories → **Evaluation**
4. Surveys → **Surveys**
5. Everything else → the **Text Stories** topic for the main challenge the paper tackles

Within a topic, papers are sorted by year (most recent first), with 🌟 must-reads first within the same year.

## Entry format

Each entry is a single line:

```markdown
- ![ACL 2025](https://img.shields.io/badge/ACL-2025-1f6feb) [![](https://img.shields.io/badge/citation-0-blue)]() **Paper Title** [[paper]](https://arxiv.org/abs/xxxx.xxxxx) [![GitHub stars](https://img.shields.io/github/stars/owner/repo?style=social)](https://github.com/owner/repo)<br><sub>First Author, Second Author, ...</sub><br><sub>💡 One-sentence summary of the contribution.</sub>
```

- **Venue badge**: `VENUE-YEAR` with the venue family color: NLP `1f6feb`, ML `8250df`, Vision & Graphics `bf3989`, AI `1a7f37`, HCI `bc4c00`, Games `0e8a7d`, arXiv `b31b1b`, other `6e7781`. Write a hyphen inside the venue name as `--` (for example `LREC--COLING`).
- **Code**: add the GitHub stars badge only for official code; otherwise leave it out.
- **Citation badge**: keep it exactly as `[![](https://img.shields.io/badge/citation-N-blue)]()`. Any number is fine; a weekly workflow updates the counts from Semantic Scholar.
- **Authors**: list up to ten, then `et al.`
- **Summary**: one sentence, at most about 22 words, starting with what the paper contributes ("Proposes ...", "Introduces a benchmark ...", "Finds that ...").
- The 🌟 must-read mark is assigned by the maintainers.

Thank you!
