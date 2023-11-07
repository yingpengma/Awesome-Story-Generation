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

Eg. Title (ACL-2023) [paper] [code] .. [authors]


### Literature Review
- Open-world story generation with structured knowledge enhancement: A comprehensive survey (Neurocomputing-2023) [[paper]](https://arxiv.org/abs/2212.04634) [Yuxin Wang, Jieru Lin, Zhiwei Yu, Wei Hu, Börje F. Karlsson]
- Factuality Enhanced Language Models for Open-Ended Text Generation (NeurIPS-2022) [[paper]](https://proceedings.neurips.cc/paper_files/paper/2022/file/df438caa36714f69277daa92d608dd63-Paper-Conference.pdf) [Open-Ended] [Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro]
- Survey: Automatic Movie Plot and Script Generation (Arxiv-2022) [[paper]](https://www.cfilt.iitb.ac.in/resources/surveys/2022/prerak-ampsg-survey-27jun22.pdf)  [Movie Plot and Script] [Prerak Gandhi, Pushpak Bhattacharyya]
- Automatic Story Generation: Challenges and Attempts  (Arxiv-2021) [[paper]](https://arxiv.org/abs/2102.12634) [Amal Alabdulkarim, Siyan Li, Xiangyu Peng]
- Plans and Planning in Narrative Generation: A Review of  Plan-Based Approaches to the Generation of Story, Discourse and Interactivity in Narratives (Sprache und Datenverarbeitung-2013) [[paper]](https://www.justusrobertson.com/papers/Young%20Ware%20Cassell%20and%20Robertson%202013%20-%20Plans%20and%20Planning%20in%20Narrative%20Generation.pdf)
[A Review of Narrative Generation] [R. Michael Young, Stephen Ware, Brad Cassell, Justus Robertson]
- From Linear Story Generation to Branching Story Graphs (AAAI-2006) [[paper]](http://www.cc.gatech.edu/~riedl/pubs/riedl-aiide05.pdf)
[Story Generation and Graphs] [Mark O. Riedl, R. Michael Young]

### Plot Development
- Uncovering Surprising Event Boundaries in Narratives (ACL WNU-2022) [[paper]](https://aclanthology.org/2022.wnu-1.1/) [Event Boundaries] [Zhilin Wang, Anna Jafarpour, Maarten Sap] 
- Story Realization: Expanding Plot Events into Sentences (AAAI-2020) [[paper]](https://arxiv.org/abs/1909.03480v2)  [[code]](https://github.com/rajammanabrolu/StoryRealization) [Expanding Plot] [Prithviraj Ammanabrolu, Ethan Tien, Wesley Cheung, Zhaochen Luo, William Ma, Lara J. Martin, Mark O. Riedl]
- Event Representations for Automated Story Generation with Deep Neural Nets (AAAI-2018) [[paper]](https://arxiv.org/abs/1706.01331)  [[code]](https://github.com/lara-martin/ASTER) [Event Representations] [Lara J. Martin, Prithviraj Ammanabrolu, Xinyu Wang, William Hancock, Shruti Singh, Brent Harrison, Mark O. Riedl]

### Improving Storytelling
- Creativity Support in the Age of Large Language Models: An Empirical Study Involving Emerging Writers (Arxiv-2023) [[paper]](https://arxiv.org/abs/2309.12570) [Tuhin Chakrabarty, Vishakh Padmakumar, Faeze Brahman, Smaranda Muresan]
- Open-ended Long Text Generation via Masked Language Modeling (ACL-2023) [[paper]](https://aclanthology.org/2023.acl-long.13/) [Xiaobo Liang, Zecheng Tang, Juntao Li, Min Zhang]
- Creative Writing with an AI-Powered Writing Assistant: Perspectives from Professional Writers (Arxiv-2022) [[paper]](https://arxiv.org/abs/2211.05030) [Daphne Ippolito, Ann Yuan, Andy Coenen, Sehmon Burnam]
- Help me write a poem: Instruction Tuning as a Vehicle for Collaborative Poetry Writing (EMNLP-2022) [[paper]](https://arxiv.org/abs/2210.13669) [Tuhin Chakrabarty, Vishakh Padmakumar, He He]
- EtriCA: Event-triggered context-aware story generation augmented by cross attention (EMNLP-2022) [[paper]](https://arxiv.org/abs/2210.12463) [Chen Tang, Chenghua Lin, Henglin Huang, Frank Guerin, Zhihao Zhang]
- Generating Coherent Narratives by Learning Dynamic and Discrete Entity States with a Contrastive Framework (Arxiv-2022) [[paper]](https://arxiv.org/abs/2208.03985) [Contrastive Framework] [Jian Guan, Zhenyu Yang, Rongsheng Zhang, Zhipeng Hu, Minlie Huang]
- Great Expectations: Unsupervised Inference of Suspense, Surprise and Salience in Storytelling (Arxiv-2022) [[paper]](https://arxiv.org/abs/2206.09708) [David Wilmot]
- Aligning to Social Norms and Values in Interactive Narratives (NAACL-2022) [[paper]](https://arxiv.org/abs/2205.01975) [Social Norms and Values] [Prithviraj Ammanabrolu, Liwei Jiang, Maarten Sap, Hannaneh Hajishirzi, Yejin Choi]
- Improving Chinese Story Generation via Awareness of Syntactic Dependencies and Semantics (AACL-2022) [[paper]](https://arxiv.org/abs/2210.10618) [Henglin Huang, Chen Tang, Tyler Loakman, Frank Guerin, Chenghua Lin]
- Clseg: Contrastive learning of story ending generation (ICASSP-2022) [[paper]](https://arxiv.org/abs/2202.09049) [Yuqiang Xie, Yue Hu, Luxi Xing, Yunpeng Li, Wei Peng, Ping Guo]
- Towards Coherent and Consistent Use of Entities in Narrative Generation (ICML-2022) [[paper]](https://arxiv.org/abs/2202.01709) [Coherent and Consistent] [Pinelopi Papalampidi, Kris Cao, Tomas Kocisky]
- Guiding Neural Story Generation with Reader Models (EMNLP-2021) [[paper]](https://arxiv.org/abs/2112.08596) [Reader Models Guide] [Xiangyu Peng, Kaige Xie, Amal Alabdulkarim, Harshith Kayam, Samihan Dani, Mark O. Riedl]
- Goal-Directed Story Generation: Augmenting Generative Language Models with Reinforcement Learning (Arxiv-2021) [[paper]](https://arxiv.org/abs/2112.08593) [Reinforcement Learning] [Amal Alabdulkarim, Winston Li, Lara J. Martin, Mark O. Riedl]
- Towards Document-Level Paraphrase Generation with Sentence Rewriting and Reordering (EMNLP Findings-2021) [[paper]](https://arxiv.org/abs/2109.07095v1)   [[code]](https://github.com/l-zhe/corpg) [Sentence Rewriting and Reordering] [Zhe Lin, Yitao Cai, Xiaojun Wan]
- Long text generation by modeling sentence-level and discourse-level coherence (ACL-2021) [[paper]](https://arxiv.org/abs/2105.08963) [Modeling Coherence] [Jian Guan, Xiaoxi Mao, Changjie Fan, Zitao Liu, Wenbiao Ding, Minlie Huang]
- Improving Neural Story Generation by Targeted Common Sense Grounding (EMNLP-2020) [[paper]](https://arxiv.org/abs/1908.09451) [Huanru Henry Mao, Bodhisattwa Prasad Majumder, Julian McAuley, Garrison W. Cottrell]
- Heteroglossia: In-Situ Story Ideation with the Crowd (CHI-2020) [[paper]](https://arxiv.org/abs/2001.04519) [Chieh-Yang Huang, Shih-Hong Huang, Ting-Hao 'Kenneth' Huang]
- Learning to Control the Fine-grained Sentiment for Story Ending Generation (ACL-2019) [[paper]](https://aclanthology.org/P19-1603/) [Fuli Luo, Damai Dai, Pengcheng Yang, Tianyu Liu, Baobao Chang, Zhifang Sui, Xu Sun]
- Story Ending Generation with Incremental Encoding and Commonsense Knowledge (AAAI-2019) [[paper]](https://arxiv.org/abs/1808.10113) [Better Ending] [Jian Guan, Yansen Wang, Minlie Huang]


### Controllability
- Controlling keywords and their positions in text generation (ArXiv-2023) [[paper]](https://arxiv.org/abs/2304.09516) [控制关键词在文中位置]
- Psychology-guided Controllable Story Generation  (COLING-2022) [[paper]](https://arxiv.org/abs/2210.07493) [Yuqiang Xie, Yue Hu, Yunpeng Li, Guanqun Bi, Luxi Xing, Wei Peng]
- Genre-controllable story generation via supervised contrastive learning (WWW-2022) [[paper]](https://dl.acm.org/doi/abs/10.1145/3485447.3512004) [JinUk Cho, MinSu Jeong, JinYeong Bak, Yun-Gyung Cheong]
- A Plug-and-Play Method for Controlled Text Generation (EMNLP Findings-2021) [[paper]](https://arxiv.org/abs/2109.09707v1)  [[code]](https://github.com/dapascual/k2t) [即插即用可控文本生成]
- Plug-and-Blend: A Framework for Plug-and-play Controllable Story Generation with Sketches (ArXiv-2021) [[paper]](https://arxiv.org/abs/2104.04039v2)  [[code]](https://github.com/xxbidiao/plug-and-blend) [可控故事生成框架]
- Towards Controllable Story Generation (ACL-2018) [[paper]](https://aclanthology.org/W18-1505.pdf) [可控的故事生成]

### Characterization
- TVShowGuess: Character Comprehension in Stories as Speaker Guessing (NAACL-2022) [[paper]](https://arxiv.org/abs/2204.07721) [Yisi Sang, Xiangyang Mou, Mo Yu, Shunyu Yao, Jing Li, Jeffrey Stanton]
- Towards Inter-character Relationship-driven Story Generation (EMNLP-2022) [[paper]](https://arxiv.org/abs/2211.00676) [从角色人际关系出发编写故事]
- CHAE: Fine-Grained Controllable Story Generation with Characters, Actions and Emotions (COLING-2022) [[paper]](https://arxiv.org/abs/2210.05221) [Characters, Actions and Emotions] [Xinpeng Wang, Han Jiang, Zhihua Wei, Shanlin Zhou]
- An Ion Exchange Mechanism Inspired Story Ending Generator for Different Characters (Arxiv-2022) [[paper]](https://arxiv.org/abs/2209.00200) [Xinyu Jiang, Qi Zhang, Chongyang Shi, Kaiying Jiang, Liang Hu, Shoujin Wang]
- Persona-Guided Planning for Controlling the Protagonist’s Persona in Story Generation (NAACL-2022) [[paper]](https://arxiv.org/abs/2204.10703) [[code]](https://github.com/thu-coai/ConPer) [Zhexin Zhang, Jiaxin Wen, Jian Guan, Minlie Huang]
- Modeling Worlds in Text (ArXiv-2021) [[paper]](https://arxiv.org/abs/2106.09578) [交互式语言代理]
- Unsupervised Enrichment of Persona-grounded Dialog with Background Stories (ACL-2021) [[paper]](https://arxiv.org/abs/2106.08364) [Bodhisattwa Prasad Majumder, Taylor Berg-Kirkpatrick, Julian McAuley, Harsh Jhamtani]
- Telling Stories through Multi-User Dialogue by Modeling Character Relations (ACL-2021) [[paper]](https://arxiv.org/abs/2105.15054v1) [通过建模角色关系通过多用户对话讲故事]


### Writing Style
- StoryTrans: Non-Parallel Story Author-Style Transfer with Discourse Representations and Content Enhancing (ACL-2023) [[paper]](https://arxiv.org/abs/2208.13423) [Author-Style Transfer] [Xuekai Zhu, Jian Guan, Minlie Huang, Juan Liu]
- Stylized story generation with style-guided planning (ACL-2021) [[paper]](https://arxiv.org/abs/2105.08625) [style-guided planning] [Xiangzhe Kong, Jialiang Huang, Ziquan Tung, Jian Guan, Minlie Huang]


### Story Outlining
- DOC: Improving Long Story Coherence With Detailed Outline Control (ACL-2023) [[paper]](https://arxiv.org/abs/2212.10077) [Detailed Outline] [Kevin Yang, Dan Klein, Nanyun Peng, Yuandong Tian]
- TaleBrush: Sketching Stories with Generative Pretrained Language Models (CHI-2022) [[paper]](http://www.cond.org/talebrush.pdf)  [John Joon Young Chung, Wooseok Kim, Kang Min Yoo, Hwaran Lee, Eytan Adar, Minsuk Chang]
- Neural Story Planning (Arxiv-2022) [[paper]](https://arxiv.org/abs/2212.08718) [Planning] [Anbang Ye, Christopher Cui, Taiwei Shi, Mark O. Riedl]
- Event Transition Planning for Open-ended Text Generation (Arxiv-2022) [[paper]](https://arxiv.org/abs/2204.09453) [Qintong Li, Piji Li, Wei Bi, Zhaochun Ren, Yuxuan Lai, Lingpeng Kong]
- Draft and Edit: Automatic Storytelling Through Multi-Pass Hierarchical Conditional Variational Autoencoder (AAAI-2020) [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/5538) [Meng-Hsuan Yu, Juntao Li, Danyang Liu, Dongyan Zhao, Rui Yan, Bo Tang, Haisong Zhang]
- Strategies for Structuring Story Generation (Arxiv-2019) [[paper]](https://arxiv.org/abs/1902.01109) [故事生成策略]
- Plan-And-Write: Towards Better Automatic Storytelling (AAAI-2019) [[paper]](https://arxiv.org/abs/1811.05701) [[code]](https://bitbucket.org/VioletPeng/language-model)  [自动故事生成]
- A Skeleton-Based Model for Promoting Coherence Among Sentences in Narrative Story Generation (EMNLP-2018) [[paper]](https://arxiv.org/abs/1808.06945) [基于草稿的更连贯故事生成]
- Hierarchical Neural Story Generation (ACL-2018) [[paper]](https://arxiv.org/abs/1805.04833) [[code]](https://github.com/kevalnagda/StoryGeneration) [[Writing prompt]](https://www.kaggle.com/ratthachat/writing-prompts) [分层故事生成]


### Prompt Design
- CoRRPUS: Code-based Structured Prompting for Neurosymbolic Story Understanding (ACL Findings-2023) [[paper]](https://arxiv.org/abs/2212.10754) [Code-based Structured Prompting] [Yijiang River Dong, Lara J. Martin, Chris Callison-Burch]
- Re3: Generating longer stories with recursive reprompting and revision (EMNLP-2022) [[paper]](https://arxiv.org/abs/2210.06774) [recursive reprompting and revision] [Kevin Yang, Yuandong Tian, Nanyun Peng, Dan Klein]
- Go Back in Time: Generating Flashbacks in Stories with Event Temporal Prompts (NAACL-2022) [[paper]](https://arxiv.org/abs/2205.01898) [Flashbacks via Temporal Event] [Rujun Han, Hong Chen, Yufei Tian, Nanyun Peng]
- What makes the story forward? inferring commonsense explanations as prompts for future event generation (SIGIR-2022) [[paper]](https://arxiv.org/abs/2201.07099) [Li Lin, Yixin Cao, Lifu Huang, Shu'ang Li, Xuming Hu, Lijie Wen, Jianmin Wang]


<!--
update 
-->


### Language Models
- RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text (ArXiv-2023) [[paper]](https://arxiv.org/abs/2305.13304) [[code]](https://github.com/aiwaves-cn/RecurrentGPT) [Wangchunshu Zhou, Yuchen Eleanor Jiang, Peng Cui, Tiannan Wang, Zhenxin Xiao, Yifan Hou, Ryan Cotterell, Mrinmaya Sachan
]
- The Next Chapter: A Study of Large Language Models in Storytelling (INLG-2023) [[paper]](https://arxiv.org/abs/2301.09790) [Zhuohan Xie, Trevor Cohn, Jey Han Lau]
- Little Red Riding Hood Goes Around the Globe:Crosslingual Story Planning and Generation with Large Language Models (Arxiv-2023) [[paper]](https://arxiv.org/abs/2212.10471) [Evgeniia Razumovskaia, Joshua Maynez, Annie Louis, Mirella Lapata, Shashi Narayan]
- Plot Writing From Pre-Trained Language Models (ArXiv-2022) [[paper]](https://arxiv.org/abs/2206.03021) [Yiping Jin, Vishakha Kadam, Dittaya Wanvarie]
- Co-Writing Screenplays and Theatre Scripts with Language Models: An Evaluation by Industry Professionals (CHI-2022) [[paper]](https://arxiv.org/abs/2209.14958)  [Piotr Mirowski, Kory W. Mathewson, Jaylen Pittman, Richard Evans]
- MEGATRON-CNTRL: Controllable story generation with external knowledge using large-scale language models (EMNLP-2020) [[paper]](https://arxiv.org/abs/2010.00840)  [Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar, Bryan Catanzaro]
- A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation (TACL-2020) [[paper]](https://arxiv.org/abs/2001.05139)  [Jian Guan, Fei Huang, Zhihao Zhao, Xiaoyan Zhu, Minlie Huang]

### Evaluation Methods
- Learning Personalized Story Evaluation (ArXiv-2023) [[paper]](https://arxiv.org/abs/2310.03304) [Danqing Wang, Kevin Yang, Hanlin Zhu, Xiaomeng Yang, Andrew Cohen, Lei Li, Yuandong Tian]
- Art or Artifice? Large Language Models and the False Promise of Creativity (ArXiv-2023) [[paper]](https://arxiv.org/abs/2309.14556) [Tuhin Chakrabarty, Philippe Laban, Divyansh Agarwal, Smaranda Muresan, Chien-Sheng Wu]
- HAUSER: Towards Holistic and Automatic Evaluation of Simile Generation (ACL-2023) [[paper]](https://arxiv.org/abs/2306.07554) [Qianyu He, Yikai Zhang, Jiaqing Liang, Yuncheng Huang, Yanghua Xiao, Yunwen Chen]
- Can Large Language Models Be an Alternative to Human Evaluations? (ACL-2023) [[paper]](https://arxiv.org/abs/2305.01937) [Cheng-Han Chiang, Hung-yi Lee]
- Exploring the Use of Large Language Models for Reference-Free Text Quality Evaluation: An Empirical Study (Arxiv-2023) [[paper]](https://arxiv.org/abs/2304.00723) [Yi Chen, Rui Wang, Haiyun Jiang, Shuming Shi, Ruifeng Xu]
- DeltaScore: Evaluating Story Generation with Differentiating Perturbations (ArXiv-2023) [[paper]](https://arxiv.org/abs/2303.08991) [Zhuohan Xie, Miao Li, Trevor Cohn, Jey Han Lau]
- Automatic Comment Generation for Chinese Student Narrative Essays (EMNLP-2022) [[paper]](https://aclanthology.org/2022.emnlp-demos.21/) [Zhexin Zhang, Jian Guan, Guowei Xu, Yixiang Tian, Minlie Huang]
- StoryER: Automatic Story Evaluation via Ranking, Rating and Reasoning (EMNLP-2022) [[paper]](https://arxiv.org/abs/2210.08459) [Hong Chen, Duc Minh Vo, Hiroya Takamura, Yusuke Miyao, Hideki Nakayama]
- A Benchmark for Understanding and Generating Dialogue between Characters in Stories (ArXiv-2022) [[paper]](https://arxiv.org/abs/2209.08524) [Jianzhu Yao, Ziqi Liu, Jian Guan, Minlie Huang]
- The Glass Ceiling of Automatic Evaluation in Natural Language Generation (Arxiv-2022) [[paper]](https://arxiv.org/abs/2208.14585) [Pierre Colombo, Maxime Peyrard, Nathan Noiry, Robert West, Pablo Piantanida]
- Of Human Criteria and Automatic Metrics: A Benchmark of the Evaluation of Story Generation (COLING-2022) [[paper]](https://arxiv.org/abs/2208.11646)  [Cyril Chhun, Pierre Colombo, Chloé Clavel, Fabian M. Suchanek]
- Toward Educator-focused Automated Scoring Systems for Reading and Writing (ArXiv-2021)  [[paper]](https://arxiv.org/abs/2112.11973) [Mike Hardy]
- LOT: A story-centric benchmark for evaluating Chinese long text understanding and generation (TACL-2022) [[paper]](https://arxiv.org/abs/2108.12960) [Jian Guan, Zhuoer Feng, Yamei Chen, Ruilin He, Xiaoxi Mao, Changjie Fan, Minlie Huang]
- Openmeva: A benchmark for evaluating open-ended story generation metrics (ACL-2021) [[paper]](https://arxiv.org/abs/2105.08920) [Jian Guan, Zhexin Zhang, Zhuoer Feng, Zitao Liu, Wenbiao Ding, Xiaoxi Mao, Changjie Fan, Minlie Huang]
- Union: An unreferenced metric for evaluating open-ended story generation (EMNLP-2020) [[paper]](https://arxiv.org/abs/2009.07602) [Jian Guan, Minlie Huang]


### Applications
- TropeTwist: Trope-based Narrative Structure Generation (FDG-2022) [[paper]](https://arxiv.org/abs/2204.09672) [Alberto Alvarez, Jose Font]
- Generating Interactive Worlds with Text (AAAI-2020) [[paper]](https://arxiv.org/abs/1911.09194)  [Angela Fan, Jack Urbanek, Pratik Ringshia, Emily Dinan, Emma Qian, Siddharth Karamcheti, Shrimai Prabhumoye, Douwe Kiela, Tim Rocktaschel, Arthur Szlam, Jason Weston]
- Learning to Speak and Act in a Fantasy Text Adventure Game (EMNLP-2019) [[paper]](https://arxiv.org/abs/1903.03094)  [Jack Urbanek, Angela Fan, Siddharth Karamcheti, Saachi Jain, Samuel Humeau, Emily Dinan, Tim Rocktäschel, Douwe Kiela, Arthur Szlam, Jason Weston]
- TextWorld: A Learning Environment for Text-based Game (IJCAI-2018) [[paper]](https://arxiv.org/abs/1806.11532)  [Marc-Alexandre Côté, Ákos Kádár, Xingdi Yuan, Ben Kybartas, Tavian Barnes, Emery Fine, James Moore, Matthew Hausknecht, Layla El Asri, Mahmoud Adada, Wendy Tay, Adam Trischler]


### Datasets
- StoryWars: A Dataset and Instruction Tuning Baselines for Collaborative Story Understanding and Generation (ACL-2023) [[paper]](https://arxiv.org/abs/2305.08152) [Yulun Du, Lydia Chilton]
- Long Story Generation Challenge  (INLG-2023) [[paper]](https://aclanthology.org/2023.inlg-genchal.2/) [Nikolay Mikhaylovskiy]
- PASTA: A Dataset for Modeling Participant States in Narratives (Arxiv-2022) [[paper]](https://arxiv.org/abs/2208.00329) [Sayontan Ghosh, Mahnaz Koupaee, Isabella Chen, Francis Ferraro, Nathanael Chambers, Niranjan Balasubramanian]
- SummScreen: A Dataset for Abstractive Screenplay Summarization (ACL-2022) [[paper]](https://arxiv.org/abs/2104.07091) [[code]](https://github.com/mingdachen/SummScreen) [Mingda Chen, Zewei Chu, Sam Wiseman, Kevin Gimpel]
- A corpus for understanding and generating moral stories (NAACL-2022) [[paper]](https://arxiv.org/abs/2204.09438) [Jian Guan, Ziqi Liu, Minlie Huang]
- A Corpus and Evaluation Framework for Deeper Understanding of Commonsense Stories (NAACL-2016) [[paper]](https://arxiv.org/abs/1604.01696) [Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong He, Devi Parikh, Dhruv Batra, Lucy Vanderwende, Pushmeet Kohli, James Allen]


## Public Data
- [ROC Stories](https://cs.rochester.edu/nlp/rocstories/) is a compilation of 100,000 five-sentence stories and 3,742 Story Cloze Test stories, capturing a rich array of causal and temporal commonsense connections between everyday events, making it suitable for story generation tasks.
- [CommonGen](https://inklab.usc.edu/CommonGen/) was developed by combining crowdsourced and existing caption corpora, containing 79k commonsense descriptions across 35k distinct concept-sets.
- [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) offers access to a dataset containing movie plot summaries and related metadata.
- [Scifi TV Show Plot Summaries & Events](https://huggingface.co/datasets/lara-martin/Scifi_TV_Shows) is a collection of plot synopses for long-running (80+ episodes) science fiction TV shows, sourced from Fandom.com wikis.
- [The LIGHT project](https://github.com/facebookresearch/ParlAI/tree/main/projects/light) serves as a large-scale fantasy text adventure game research platform, designed to train agents capable of both talking and acting, while interacting with other models or humans.
- [The TextWorld project](https://github.com/microsoft/TextWorld) is a sandbox learning environment aimed at training and evaluating reinforcement learning (RL) agents on text-based games.


