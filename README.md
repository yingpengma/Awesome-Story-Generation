<h1 align="center">Awesome-Story-Generation</h1>

## Table of Contents

- [Introduction](#introduction)
- [Papers](#papers)
  - [Literature Review](#literature-review)
  - [Plot Development](#plot-development)
  - [Improving Storytelling](#improving-storytelling)
  - [Controllability](#controllability)
  - [Characterization](#characterization)
  - [Writing Style](#writing-style)
  - [Story Outlining](#story-outlining)
  - [Prompt Design](#prompt-design)
  - [Language Models](#language-models)
  - [Evaluation Methods](#evaluation-methods)
  - [Applications](#applications)
  - [Datasets](#datasets)
- [Public Data](#public-data)

## Introduction
This project collects an extensive list of remarkable papers on **Story Generation**, primarily focusing on the era of **Large Language Models (LLMs)**.

We would like to extend our heartfelt gratitude to [**Awesome-story-generation**](https://github.com/Whorra/Awesome-story-generation),  [**PaperForONLG**](https://github.com/thu-coai/PaperForONLG/tree/main) for their invaluable assistance and contributions.

If you have any suggestions or questions, please do not hesitate to reach out to me: 

mayingpeng33 [AT] gmail [DOT] com

## Papers

Eg. Title (ACL-2023) [paper] [code] .. [summary] [authors]


### Literature Review
- Factuality Enhanced Language Models for Open-Ended Text Generation (NeurIPS-2022) [[paper]](https://proceedings.neurips.cc/paper_files/paper/2022/file/df438caa36714f69277daa92d608dd63-Paper-Conference.pdf) [Open-Ended] [Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro]
- Survey: Automatic Movie Plot and Script Generation (Arxiv-2022) [[paper]](https://www.cfilt.iitb.ac.in/resources/surveys/2022/prerak-ampsg-survey-27jun22.pdf)  [Movie Plot and Script] [Prerak Gandhi, Pushpak Bhattacharyya] 
- Plans and Planning in Narrative Generation: A Review of  Plan-Based Approaches to the Generation of Story, Discourse and Interactivity in Narratives (Sprache und Datenverarbeitung-2013) [[paper]](https://www.justusrobertson.com/papers/Young%20Ware%20Cassell%20and%20Robertson%202013%20-%20Plans%20and%20Planning%20in%20Narrative%20Generation.pdf)
[A Review of Narrative Generation] [R. Michael Young, Stephen Ware, Brad Cassell, Justus Robertson]
- From Linear Story Generation to Branching Story Graphs (AAAI-2006) [[paper]](http://www.cc.gatech.edu/~riedl/pubs/riedl-aiide05.pdf)
[Story Generation and Graphs] [Mark O. Riedl, R. Michael Young]

### Plot Development
- Uncovering Surprising Event Boundaries in Narratives (ACL WNU-2022) [[paper]](https://aclanthology.org/2022.wnu-1.1/) [Event Boundaries] [Zhilin Wang, Anna Jafarpour, Maarten Sap] 
- Story Realization: Expanding Plot Events into Sentences (AAAI-2020) [[paper]](https://arxiv.org/pdf/1909.03480v2.pdf)  [[code]](https://github.com/rajammanabrolu/StoryRealization) [Expanding Plot] [Prithviraj Ammanabrolu, Ethan Tien, Wesley Cheung, Zhaochen Luo, William Ma, Lara J. Martin, Mark O. Riedl]
- Event Representations for Automated Story Generation with Deep Neural Nets (AAAI-2018) [[paper]](https://arxiv.org/pdf/1706.01331v3.pdf)  [[code]](https://github.com/lara-martin/ASTER) [Event Representations] [Lara J. Martin, Prithviraj Ammanabrolu, Xinyu Wang, William Hancock, Shruti Singh, Brent Harrison, Mark O. Riedl]

### Improving Storytelling
- Generating Coherent Narratives by Learning Dynamic and Discrete Entity States with a Contrastive Framework (Arxiv-2022) [[paper]](https://arxiv.org/pdf/2208.03985.pdf) [Contrastive Framework] [Jian Guan, Zhenyu Yang, Rongsheng Zhang, Zhipeng Hu, Minlie Huang]
- Aligning to Social Norms and Values in Interactive Narratives (NAACL-2022) [[paper]](https://arxiv.org/abs/2205.01975) [Social Norms and Values] [Prithviraj Ammanabrolu, Liwei Jiang, Maarten Sap, Hannaneh Hajishirzi, Yejin Choi] 
- Towards Coherent and Consistent Use of Entities in Narrative Generation (ICML-2022) [[paper]](https://arxiv.org/abs/2202.01709) [Coherent and Consistent] [Pinelopi Papalampidi, Kris Cao, Tomas Kocisky]
- Guiding Neural Story Generation with Reader Models (EMNLP-2021) [[paper]](https://arxiv.org/pdf/2112.08596.pdf) [Reader Models Guide] [Xiangyu Peng, Kaige Xie, Amal Alabdulkarim, Harshith Kayam, Samihan Dani, Mark O. Riedl]
- Goal-Directed Story Generation: Augmenting Generative Language Models with Reinforcement Learning (Arxiv-2021) [[paper]](https://arxiv.org/pdf/2112.08593.pdf) [Reinforcement Learning] [Amal Alabdulkarim, Winston Li, Lara J. Martin, Mark O. Riedl]
- Towards Document-Level Paraphrase Generation with Sentence Rewriting and Reordering (EMNLP Findings-2021) [[paper]](https://arxiv.org/pdf/2109.07095v1.pdf)   [[code]](https://github.com/l-zhe/corpg) [Sentence Rewriting and Reordering] [Zhe Lin, Yitao Cai, Xiaojun Wan]
- Long text generation by modeling sentence-level and discourse-level coherence (ACL-2021) [[paper]](https://arxiv.org/pdf/2105.08963.pdf) [Modeling Coherence] [Jian Guan, Xiaoxi Mao, Changjie Fan, Zitao Liu, Wenbiao Ding, Minlie Huang]
- Story Ending Generation with Incremental Encoding and Commonsense Knowledge (AAAI-2019) [[paper]](https://arxiv.org/pdf/1808.10113.pdf) [Better Ending] [Jian Guan, Yansen Wang, Minlie Huang]


### Controllability
- Controlling keywords and their positions in text generation (ArXiv-2023) [[paper]](https://arxiv.org/pdf/2304.09516.pdf) [控制关键词在文中位置]
- A Plug-and-Play Method for Controlled Text Generation (EMNLP Findings-2021) [[paper]](https://arxiv.org/pdf/2109.09707v1.pdf)  [[code]](https://github.com/dapascual/k2t) [即插即用可控文本生成]
- Plug-and-Blend: A Framework for Plug-and-play Controllable Story Generation with Sketches (ArXiv-2021) [[paper]](https://arxiv.org/pdf/2104.04039v2.pdf)  [[code]](https://github.com/xxbidiao/plug-and-blend) [可控故事生成框架]
- Towards Controllable Story Generation (ACL-2018) [[paper]](https://aclanthology.org/W18-1505.pdf) [可控的故事生成]

### Characterization
- Towards Inter-character Relationship-driven Story Generation (EMNLP-2022) [[paper]](https://arxiv.org/pdf/2211.00676.pdf) [从角色人际关系出发编写故事]
- CHAE: Fine-Grained Controllable Story Generation with Characters, Actions and Emotions (COLING-2022) [[paper]](https://arxiv.org/pdf/2210.05221.pdf) [Characters, Actions and Emotions] [Xinpeng Wang, Han Jiang, Zhihua Wei, Shanlin Zhou]
- Persona-Guided Planning for Controlling the Protagonist’s Persona in Story Generation (NAACL-2022) [[paper]](https://arxiv.org/pdf/2204.10703.pdf) [[code]](https://github.com/thu-coai/ConPer) [Persona-Guided Planning] [Zhexin Zhang, Jiaxin Wen, Jian Guan, Minlie Huang]
- Modeling Worlds in Text (ArXiv-2021) [[paper]](https://arxiv.org/pdf/2106.09578.pdf) [交互式语言代理]
- Telling Stories through Multi-User Dialogue by Modeling Character Relations (ACL-2021) [[paper]](https://arxiv.org/pdf/2105.15054v1.pdf) [通过建模角色关系通过多用户对话讲故事]


### Writing Style
- StoryTrans: Non-Parallel Story Author-Style Transfer with Discourse Representations and Content Enhancing (ACL-2023) [[paper]](https://arxiv.org/pdf/2208.13423.pdf) [Author-Style Transfer] [Xuekai Zhu, Jian Guan, Minlie Huang, Juan Liu]
- Stylized story generation with style-guided planning (ACL-2021) [[paper]](https://arxiv.org/pdf/2105.08625.pdf) [style-guided planning] [Xiangzhe Kong, Jialiang Huang, Ziquan Tung, Jian Guan, Minlie Huang]


### Story Outlining
- DOC: Improving Long Story Coherence With Detailed Outline Control (ACL-2023) [[paper]](https://arxiv.org/pdf/2212.10077.pdf) [Detailed Outline] [Kevin Yang, Dan Klein, Nanyun Peng, Yuandong Tian]
- TaleBrush: Sketching Stories with Generative Pretrained Language Models (CHI-2022) [[paper]](http://www.cond.org/talebrush.pdf)  [使用草图引导叙事]
- Neural Story Planning (Arxiv-2022) [[paper]](https://arxiv.org/pdf/2212.08718.pdf) [Planning] [Anbang Ye, Christopher Cui, Taiwei Shi, Mark O. Riedl]
- Strategies for Structuring Story Generation (Arxiv-2019) [[paper]](https://arxiv.org/pdf/1902.01109.pdf) [故事生成策略]
- Plan-And-Write: Towards Better Automatic Storytelling (AAAI-2019) [[paper]](https://arxiv.org/pdf/1811.05701.pdf) [[code]](https://bitbucket.org/VioletPeng/language-model)  [自动故事生成]
- A Skeleton-Based Model for Promoting Coherence Among Sentences in Narrative Story Generation (EMNLP-2018) [[paper]](https://arxiv.org/pdf/1808.06945.pdf) [基于草稿的更连贯故事生成]
- Hierarchical Neural Story Generation (ACL-2018) [[paper]](https://arxiv.org/pdf/1805.04833.pdf) [[code]](https://github.com/kevalnagda/StoryGeneration) [[Writing prompt]](https://www.kaggle.com/ratthachat/writing-prompts) [分层故事生成]


### Prompt Design
- CoRRPUS: Code-based Structured Prompting for Neurosymbolic Story Understanding (ACL Findings-2023) [[paper]](https://arxiv.org/pdf/2212.10754.pdf) [Code-based Structured Prompting] [Yijiang River Dong, Lara J. Martin, Chris Callison-Burch]
- Re3: Generating longer stories with recursive reprompting and revision (EMNLP-2022) [[paper]](https://arxiv.org/pdf/2210.06774.pdf) [recursive reprompting and revision] [Kevin Yang, Yuandong Tian, Nanyun Peng, Dan Klein]
- Go Back in Time: Generating Flashbacks in Stories with Event Temporal Prompts (NAACL-2022) [[paper]](https://arxiv.org/pdf/2205.01898.pdf) [Flashbacks via Temporal Event] [Rujun Han, Hong Chen, Yufei Tian, Nanyun Peng]

### Language Models
- RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text (ArXiv-2023) [[paper]](https://arxiv.org/pdf/2305.13304.pdf) [[code]](https://github.com/aiwaves-cn/RecurrentGPT) [自然语言模拟LSTM机制，拓展生成长度且保证长期记忆]
- Controllable Story Generation with External Knowledge Using Large-Scale Language Models (EMNLP-2020) [[paper]](https://arxiv.org/pdf/2010.00840.pdf)  [使用LLM的新框架 结合外部知识]
- A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation (TACL-2020) [[paper]](https://arxiv.org/pdf/2001.05139.pdf)  [结合Commonsense]

### Evaluation Methods
- Learning Personalized Story Evaluation (ArXiv-2023) [[paper]](https://arxiv.org/pdf/2310.03304.pdf) [Evaluate open-ended text generation] [Danqing Wang, Kevin Yang, Hanlin Zhu, Xiaomeng Yang, Andrew Cohen, Lei Li, Yuandong Tian]
- Can Large Language Models Be an Alternative to Human Evaluations? (ACL-2023) [[paper]](https://arxiv.org/pdf/2305.01937.pdf) [[Chinese Version]](https://github.com/yingpengma/Awesome-Story-Generation/blob/main/10%20Evaluation%20Methods/Can%20Large%20Language%20Models%20Be%20an%20Alternative%20to%20Human%20Evaluation/%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E5%8F%AF%E4%BB%A5%E6%9B%BF%E4%BB%A3%E4%BA%BA%E7%B1%BB%E8%AF%84%E4%BC%B0%E5%90%97.pdf) [Comparing the quality of human and LLM evaluations of text generation] [Cheng-Han Chiang, Hung-yi Lee]
- DeltaScore: Evaluating Story Generation with Differentiating Perturbations (ArXiv-2023) [[paper]](https://arxiv.org/pdf/2303.08991.pdf) [通过微分扰动从细粒度（错别字和相关性）评价故事生成]
- Art or Artifice? Large Language Models and the False Promise of Creativity (ArXiv-2023) [[paper]](https://arxiv.org/pdf/2309.14556.pdf) [Torrance Test of Creative Writing (TTCW)] [Tuhin Chakrabarty, Philippe Laban, Divyansh Agarwal, Smaranda Muresan, Chien-Sheng Wu]
- StoryER: Automatic Story Evaluation via Ranking, Rating and Reasoning (EMNLP-2022) [[paper]](https://arxiv.org/pdf/2210.08459.pdf) [Automatic Story Evaluation] [Hong Chen, Duc Minh Vo, Hiroya Takamura, Yusuke Miyao, Hideki Nakayama]
- A Benchmark for Understanding and Generating Dialogue between Characters in Stories (ArXiv-2022) [[paper]](https://arxiv.org/pdf/2209.08524.pdf) [Dialogue Benchmark] [Jianzhu Yao, Ziqi Liu, Jian Guan, Minlie Huang]
- Of Human Criteria and Automatic Metrics: A Benchmark of the Evaluation of Story Generation (ArXiv-2022) [[paper]](https://arxiv.org/pdf/2208.11646.pdf)  [定量分析人类标准与自动标准]
- Toward Educator-focused Automated Scoring Systems for Reading and Writing (ArXiv-2021)  [[paper]](https://arxiv.org/ftp/arxiv/papers/2112/2112.11973.pdf) [自动评分系统]
- LOT: A story-centric benchmark for evaluating Chinese long text understanding and generation (TACL-2022) [[paper]](https://arxiv.org/abs/2108.12960)  [Chinese long text] [Jian Guan, Zhuoer Feng, Yamei Chen, Ruilin He, Xiaoxi Mao, Changjie Fan, Minlie Huang]
- Openmeva: A benchmark for evaluating open-ended story generation metrics (ACL-2021) [[paper]](https://arxiv.org/pdf/2105.08920.pdf)  [open-ended story] [Jian Guan, Zhexin Zhang, Zhuoer Feng, Zitao Liu, Wenbiao Ding, Xiaoxi Mao, Changjie Fan, Minlie Huang]
- Union: An unreferenced metric for evaluating open-ended story generation (EMNLP-2020) [[paper]](https://arxiv.org/pdf/2009.07602.pdf) [unreferenced metric] [Jian Guan, Minlie Huang]


### Applications
- TropeTwist: Trope-based Narrative Structure Generation (FDG-2022) [[paper]](https://arxiv.org/abs/2204.09672) [narrative structure in games] [Alberto Alvarez, Jose Font]
- Generating Interactive Worlds with Text (ArXiv-2019) [[paper]](https://arxiv.org/pdf/1911.09194.pdf)  [文本交互式生成游戏世界]
- Learning to Speak and Act in a Fantasy Text Adventure Game (ACL-2019) [[paper]](https://arxiv.org/pdf/1903.03094.pdf)  [文本冒险游戏交互]
- TextWorld: A Learning Environment for Text-based Game (IJCAI-2018) [[paper]](https://arxiv.org/pdf/1806.11532)  [自动或手动生成交互文本游戏]


### Datasets
- StoryWars: A Dataset and Instruction Tuning Baselines for Collaborative Story Understanding and Generation (ACL-2023) [[paper]](https://arxiv.org/pdf/2305.08152.pdf) [协作写作数据集]
- PASTA: A Dataset for Modeling Participant States in Narratives (Arxiv-2022) [[paper]](https://arxiv.org/pdf/2208.00329.pdf) [Modeling Participant States] [Sayontan Ghosh, Mahnaz Koupaee, Isabella Chen, Francis Ferraro, Nathanael Chambers, Niranjan Balasubramanian]
- SummScreen: A Dataset for Abstractive Screenplay Summarization (ACL-2022) [[paper]](https://arxiv.org/pdf/2104.07091) [[code]](https://github.com/mingdachen/SummScreen) [Screenplay Summarization] [Mingda Chen, Zewei Chu, Sam Wiseman, Kevin Gimpel]
- A corpus for understanding and generating moral stories (NAACL-2022) [[paper]](https://arxiv.org/pdf/2204.09438.pdf) [moral stories] [Jian Guan, Ziqi Liu, Minlie Huang]
- A Corpus and Evaluation Framework for Deeper Understanding of Commonsense Stories (Arxiv-2016) [[paper]](https://arxiv.org/pdf/1604.01696) [Story Cloze dataset] [Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong He, Devi Parikh, Dhruv Batra, Lucy Vanderwende, Pushmeet Kohli, James Allen]


## Public Data
- [ROC Stories](https://cs.rochester.edu/nlp/rocstories/) is a compilation of 100,000 five-sentence stories and 3,742 Story Cloze Test stories, capturing a rich array of causal and temporal commonsense connections between everyday events, making it suitable for story generation tasks.
- [CommonGen](https://inklab.usc.edu/CommonGen/) was developed by combining crowdsourced and existing caption corpora, containing 79k commonsense descriptions across 35k distinct concept-sets.
- [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) offers access to a dataset containing movie plot summaries and related metadata.
- [Scifi TV Show Plot Summaries & Events](https://huggingface.co/datasets/lara-martin/Scifi_TV_Shows) is a collection of plot synopses for long-running (80+ episodes) science fiction TV shows, sourced from Fandom.com wikis.
- [The LIGHT project](https://github.com/facebookresearch/ParlAI/tree/main/projects/light) serves as a large-scale fantasy text adventure game research platform, designed to train agents capable of both talking and acting, while interacting with other models or humans.
- [The TextWorld project](https://github.com/microsoft/TextWorld) is a sandbox learning environment aimed at training and evaluating reinforcement learning (RL) agents on text-based games.


