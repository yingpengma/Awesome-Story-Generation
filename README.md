<h1 align="center">Awesome-Story-Generation</h1>

## Table of Contents

- [Introduction](#introduction)
- [Papers](#papers)
  - [Survey Overview Review](#survey-overview-review)
  - [Plot Event](#plot-event)
  - [Better Story](#better-story)
  - [Controllable](#controllable)
  - [Character](#character)
  - [Style](#style)
  - [Storyline Sketch Outline](#storyline-sketch-outline)
  - [Prompt](#prompt)
  - [PLM LLM](#plm-llm)
  - [Evaluation](#evaluation)
  - [Application](#application)
  - [Analysis Challenge FutureWork](#analysis-challenge-futurework)
  - [Datasets](#datasets)
- [PublicData](#publicdata)

## Introduction
This project collects awesome papers on story generation, with a focus on the LLM era papers. 

We would like to express our gratitude to the [Awesome-story-generation](https://github.com/Whorra/Awesome-story-generation) for their help. 

The citations are current as of our discovery of the papers, but they may not be revised later. This serves as a reference for you to gauge the paper's impact.

We have provided the papers for download, but we cannot guarantee that they are the final versions.

## Papers

Eg. Title (ACL-2023, Citations:0) [paper] [code] .. [summary] [authors]

### Survey Overview Review
- Plans and Planning in Narrative Generation: A Review of  Plan-Based Approaches to the Generation of Story, Discourse and Interactivity in Narratives (Sprache und Datenverarbeitung-2013, Citations:108) [[paper]](https://www.justusrobertson.com/papers/Young%20Ware%20Cassell%20and%20Robertson%202013%20-%20Plans%20and%20Planning%20in%20Narrative%20Generation.pdf)
[A Review of Narrative Generation] [R. Michael Young, Stephen Ware, Brad Cassell, Justus Robertson]
- From Linear Story Generation to Branching Story Graphs (AAAI-2006, Citations:300) [[paper]](http://www.cc.gatech.edu/~riedl/pubs/riedl-aiide05.pdf)
[Story Generation and Graphs] [Mark O. Riedl, R. Michael Young]

### Plot Event
- Story Realization: Expanding Plot Events into Sentences (AAAI-2020, Citations:57) [[paper]](https://arxiv.org/pdf/1909.03480v2.pdf)  [[code]](https://github.com/rajammanabrolu/StoryRealization) [Expanding Plot] [Prithviraj Ammanabrolu, Ethan Tien, Wesley Cheung, Zhaochen Luo, William Ma, Lara J. Martin, Mark O. Riedl]
- Event Representations for Automated Story Generation with Deep Neural Nets (AAAI-2018, Citations:221) [[paper]](https://arxiv.org/pdf/1706.01331v3.pdf)  [[code]](https://github.com/lara-martin/ASTER) [Event Representations] [Lara J. Martin, Prithviraj Ammanabrolu, Xinyu Wang, William Hancock, Shruti Singh, Brent Harrison, Mark O. Riedl]

### Better Story
- Towards Document-Level Paraphrase Generation with Sentence Rewriting and Reordering (EMNLP Findings-2021, Citations:5) [[paper]](https://arxiv.org/pdf/2109.07095v1.pdf)   [[code]](https://github.com/l-zhe/corpg) [Sentence Rewriting and Reordering] [Zhe Lin, Yitao Cai, Xiaojun Wan]
- Guiding Neural Story Generation with Reader Models (EMNLP-2021, Citations:5) [[paper]](https://arxiv.org/pdf/2112.08596.pdf) [Reader Models Guide] [Xiangyu Peng, Kaige Xie, Amal Alabdulkarim, Harshith Kayam, Samihan Dani, Mark O. Riedl]
- Goal-Directed Story Generation: Augmenting Generative Language Models with Reinforcement Learning (Arxiv-2021, Citations:6) [[paper]](https://arxiv.org/pdf/2112.08593.pdf) [Reinforcement Learning] [Amal Alabdulkarim, Winston Li, Lara J. Martin, Mark O. Riedl]
- Story Ending Generation with Incremental Encoding and Commonsense Knowledge (AAAI-2019, Citations:146) [[paper]](https://arxiv.org/pdf/1808.10113.pdf) [Better Ending] [Jian Guan, Yansen Wang, Minlie Huang]


### Controllable
- 🔥 Controlling keywords and their positions in text generation (ArXiv-2023, Citations:0) [[paper]](https://arxiv.org/pdf/2304.09516.pdf) [控制关键词在文中位置]
- A Plug-and-Play Method for Controlled Text Generation (EMNLP Findings-2021, Citations:41) [[paper]](https://arxiv.org/pdf/2109.09707v1.pdf)  [[code]](https://github.com/dapascual/k2t) [即插即用可控文本生成]
- Plug-and-Blend: A Framework for Plug-and-play Controllable Story Generation with Sketches (ArXiv-2021, Citations:16) [[paper]](https://arxiv.org/pdf/2104.04039v2.pdf)  [[code]](https://github.com/xxbidiao/plug-and-blend) [可控故事生成框架]
- Towards Controllable Story Generation (ACL-2018, Citations:129) [[paper]](https://aclanthology.org/W18-1505.pdf) [可控的故事生成]

### Character
- Persona-Guided Planning for Controlling the Protagonist’s Persona in Story Generation (ArXiv-2022, Citations:9) [[paper]](https://arxiv.org/pdf/2204.10703.pdf) [[code]](https://github.com/thu-coai/ConPer) [从角色性格和上下文出发编写故事]
- Towards Inter-character Relationship-driven Story Generation (EMNLP-2022, Citations:3) [[paper]](https://arxiv.org/pdf/2211.00676.pdf) [从角色人际关系出发编写故事]
- Telling Stories through Multi-User Dialogue by Modeling Character Relations (ACL-2021, Citations:9) [[paper]](https://arxiv.org/pdf/2105.15054v1.pdf) [通过建模角色关系通过多用户对话讲故事]
- Modeling Worlds in Text (ArXiv-2021, Citations:11) [[paper]](https://arxiv.org/pdf/2106.09578.pdf) [交互式语言代理]

### Style
- 🔥 StoryTrans: Non-Parallel Story Author-Style Transfer with Discourse Representations and Content Enhancing (ACL-2023, Citations:0) [[paper]](https://arxiv.org/pdf/2208.13423.pdf) [作者风格迁移]


### Storyline Sketch Outline
- 🔥 DOC: Improving Long Story Coherence With Detailed Outline Control (ACL-2023, Citations:5) [[paper]](https://arxiv.org/pdf/2212.10077.pdf) [详细的大纲控制]
- TaleBrush: Sketching Stories with Generative Pretrained Language Models (CHI-2022, Citations:39) [[paper]](http://www.cond.org/talebrush.pdf)  [使用草图引导叙事]
- Strategies for Structuring Story Generation (Arxiv-2019, Citations:167) [[paper]](https://arxiv.org/pdf/1902.01109.pdf) [故事生成策略]
- Plan-And-Write: Towards Better Automatic Storytelling (AAAI-2019, Citations:286) [[paper]](https://arxiv.org/pdf/1811.05701.pdf) [[code]](https://bitbucket.org/VioletPeng/language-model)  [自动故事生成]
- Hierarchical Neural Story Generation (ACL-2018, Citations:929) [[paper]](https://arxiv.org/pdf/1805.04833.pdf) [[code]](https://github.com/kevalnagda/StoryGeneration) [[Writing prompt]](https://www.kaggle.com/ratthachat/writing-prompts) [分层故事生成]
- A Skeleton-Based Model for Promoting Coherence Among Sentences in Narrative Story Generation (EMNLP-2018, Citations:85) [[paper]](https://arxiv.org/pdf/1808.06945.pdf) [基于草稿的更连贯故事生成]

### Prompt
- 🔥 CoRRPUS: Code-based Structured Prompting for Neurosymbolic Story Understanding (ACL Findings-2023, Citations:0) [[paper]](https://arxiv.org/pdf/2212.10754.pdf) [使用符号理解故事]

### PLM LLM
- 🔥 RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text (ArXiv-2023, Citations:0) [[paper]](https://arxiv.org/pdf/2305.13304.pdf) [[code]](https://github.com/aiwaves-cn/RecurrentGPT) [自然语言模拟LSTM机制，拓展生成长度且保证长期记忆]
- A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation (TACL-2020, Citations:167) [[paper]](https://arxiv.org/pdf/2001.05139.pdf)  [结合Commonsense]
- Controllable Story Generation with External Knowledge Using Large-Scale Language Models (EMNLP-2020, Citations:80) [[paper]](https://arxiv.org/pdf/2010.00840.pdf)  [使用LLM的新框架 结合外部知识]


### Evaluation
- 🔥 Can Large Language Models Be an Alternative to Human Evaluations? (ArXiv-2023, Citations:8) [[paper]](https://arxiv.org/pdf/2305.01937.pdf)  [对比人类和LLM对文本生成的质量]
- 🔥 DeltaScore: Evaluating Story Generation with Differentiating Perturbations (ArXiv-2023, Citations:1) [[paper]](https://arxiv.org/pdf/2303.08991.pdf) [通过微分扰动从细粒度（错别字和相关性）评价故事生成]
- Of Human Criteria and Automatic Metrics: A Benchmark of the Evaluation of Story Generation (ArXiv-2022, Citations:7) [[paper]](https://arxiv.org/pdf/2208.11646.pdf)  [定量分析人类标准与自动标准]
- Toward Educator-focused Automated Scoring Systems for Reading and Writing (ArXiv-2021, Citations:0)  [[paper]](https://arxiv.org/ftp/arxiv/papers/2112/2112.11973.pdf) [自动评分系统]

### Application
- Learning to Speak and Act in a Fantasy Text Adventure Game (ACL-2019, Citations:132) [[paper]](https://arxiv.org/pdf/1903.03094.pdf)  [文本冒险游戏交互]
- TextWorld: A Learning Environment for Text-based Game (IJCAI-2018, Citations:202) [[paper]](https://arxiv.org/pdf/1806.11532)  [自动或手动生成交互文本游戏]
- Generating Interactive Worlds with Text (ArXiv-2019, Citations:22) [[paper]](https://arxiv.org/pdf/1911.09194.pdf)  [文本交互式生成游戏世界]

### Analysis Challenge FutureWork


### Datasets
- 🔥 StoryWars: A Dataset and Instruction Tuning Baselines for Collaborative Story Understanding and Generation (ACL-2023, Citations:0) [[paper]](https://arxiv.org/pdf/2305.08152.pdf) [协作写作数据集]


## PublicData
- [ROC Stories](https://cs.rochester.edu/nlp/rocstories/) is a collection of 100,000 five-sentence stories and 3,742 Story Cloze Test stories that capture a rich set of causal and temporal commonsense relations between daily events, and can be used for story generation.
- [CommonGen](https://inklab.usc.edu/CommonGen/) is constructed through a combination of crowdsourced and existing caption corpora, consists of 79k commonsense descriptions over 35k unique concept-sets.
- [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) provides links to a dataset of movie plot summaries and associated metadata.
- [Scifi TV Show Plot Summaries & Events](https://huggingface.co/datasets/lara-martin/Scifi_TV_Shows) is a collection of long-running (80+ episodes) science fiction TV show synopses, scraped from Fandom.com wikis.
- [The LIGHT project](https://github.com/facebookresearch/ParlAI/tree/main/projects/light) is a large-scale fantasy text adventure game research platform for training agents that can both talk and act, interacting either with other models or with humans.
- [The TextWorld project](https://github.com/microsoft/TextWorld) is a  sandbox learning environment for the training and evaluation of reinforcement learning (RL) agents on text-based games.


