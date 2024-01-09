<h1 align="center">Awesome-Story-Generation</h1>

<div align="center">Contributed by <a href="https://yingpengma.github.io/">Yingpeng Ma</a></div>

## Table of Contents

- [Introduction](#introduction)
<!--
- [Related Repository](#related-repository)
-->
- [Papers](#papers)
  - [Literature Review](#literature-review)
  - [Language Models](#language-models)
  - [Plot Development](#plot-development)
  - [Better Storytelling](#better-storytelling)
  - [Controllability](#controllability)
  - [Characterization](#characterization)
  - [Writing Style](#writing-style)
  - [Story Planning](#story-planning)
  - [Prompt Design](#prompt-design)
  - [Evaluation](#evaluation)
  - [Application](#application)
  - [Dataset](#dataset)
- [Public Data](#public-data)

## Introduction
This repository collects an extensive list of awesome papers about **Story Generation** / **Storytelling**, primarily focusing on the era of **Large Language Models (LLMs)**.

All papers are sorted in **chronological order**, with the most recent ones appearing at the top.

Due to limited energy and time, omissions and errors may occur. If you notice any issues or mistakes anywhere, feel free to open issues and make PRs!

If you have any suggestions or questions, please do not hesitate to reach out to me:

`mayingpeng33 [AT] gmail [DOT] com`

<!--
## Related Repository
|**[Awesome-LLM-Characters](https://github.com/yingpengma/Awesome-LLM-Characters)**|
|:---:|
-->

## Papers

Eg. `ACL-2023` **Title** [paper] [code] .. [authors]  [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/fad03a833345b38323d97ee4818d341d6ba4fbdf?fields=citationCount)]()


### Literature Review
- `ArXiv-2023` **Are NLP Models Good at Tracing Thoughts: An Overview of Narrative Understanding** [[paper]](https://arxiv.org/abs/2310.18783) [Lixing Zhu, Runcong Zhao, Lin Gui, Yulan He] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/9ba36db0d9f2d586abaa85ea6a0b48c609c5c9ec?fields=citationCount)]()
- `ACM Computing Surveys-2023` **A Survey of Controllable Text Generation Using Transformer-based Pre-trained Language Models** [[paper]](https://arxiv.org/abs/2201.05337) [Hanqing Zhang, Haolin Song, Shaoyu Li, Ming Zhou, Dawei Song] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/be8e58320203a92bfacc1a1f95f6e65f3ee4fa5c?fields=citationCount)]()
- `Neurocomputing-2023` **Open-world story generation with structured knowledge enhancement: A comprehensive survey** [[paper]](https://arxiv.org/abs/2212.04634) [Yuxin Wang, Jieru Lin, Zhiwei Yu, Wei Hu, Börje F. Karlsson] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/5f7bd3dded6626d571c641ad74b4033b8e591441?fields=citationCount)]()
- `NeurIPS-2022` **Factuality Enhanced Language Models for Open-Ended Text Generation** [[paper]](https://proceedings.neurips.cc/paper_files/paper/2022/file/df438caa36714f69277daa92d608dd63-Paper-Conference.pdf)   [Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/a77f498235f12be4173f87bfca503b597c00f30e?fields=citationCount)]()
- `ArXiv-2022` **Survey: Automatic Movie Plot and Script Generation** [[paper]](https://www.cfilt.iitb.ac.in/resources/surveys/2022/prerak-ampsg-survey-27jun22.pdf)  [Prerak Gandhi, Pushpak Bhattacharyya] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/fbabb1d9d5c4f99fd17441af7a54050ca96c40fd?fields=citationCount)]()
- `ArXiv-2021` **Automatic Story Generation: Challenges and Attempts** [[paper]](https://arxiv.org/abs/2102.12634) [Amal Alabdulkarim, Siyan Li, Xiangyu Peng] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/df7bf316e7bad359e87b10544155be09336720ca?fields=citationCount)]()

### Language Models
- `ArXiv-2023` **RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text** [[paper]](https://arxiv.org/abs/2305.13304) [[code]](https://github.com/aiwaves-cn/RecurrentGPT) [Wangchunshu Zhou, Yuchen Eleanor Jiang, Peng Cui, Tiannan Wang, Zhenxin Xiao, Yifan Hou, Ryan Cotterell, Mrinmaya Sachan] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/d9964ab436eefd21f923a4bc833c6b66692c7f00?fields=citationCount)]()
- `INLG-2023` **The Next Chapter: A Study of Large Language Models in Storytelling** [[paper]](https://arxiv.org/abs/2301.09790) [Zhuohan Xie, Trevor Cohn, Jey Han Lau] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/d01f6e76e67a445f23f807c0d3e68fa0be9a2c9e?fields=citationCount)]()
- `ArXiv-2022` **Little Red Riding Hood Goes Around the Globe:Crosslingual Story Planning and Generation with Large Language Models** [[paper]](https://arxiv.org/abs/2212.10471) [Evgeniia Razumovskaia, Joshua Maynez, Annie Louis, Mirella Lapata, Shashi Narayan] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/30cc7ae95583ade1f05226c08c6f6609777aeedd?fields=citationCount)]()
- `ArXiv-2022` **Future Sight: Dynamic Story Generation with Large Pretrained Language Models** [[paper]](https://arxiv.org/abs/2212.09947) [Brian D. Zimmerman, Gaurav Sahu, Olga Vechtomova] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/0ccbb2015c3d2f43b7ff9d882495de817f4052e7?fields=citationCount)]()
- `CHI-2022` **Co-Writing Screenplays and Theatre Scripts with Language Models: An Evaluation by Industry Professionals** [[paper]](https://arxiv.org/abs/2209.14958)  [Piotr Mirowski, Kory W. Mathewson, Jaylen Pittman, Richard Evans] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/f9b16559282e5bea0bb072f9e260a4f0af697f4a?fields=citationCount)]()
- `ArXiv-2022` **Plot Writing From Pre-Trained Language Models** [[paper]](https://arxiv.org/abs/2206.03021) [Yiping Jin, Vishakha Kadam, Dittaya Wanvarie] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/f3c3c22716629df9f5353956461222ffc8e5e802?fields=citationCount)]()
- `EMNLP-2020` **MEGATRON-CNTRL: Controllable story generation with external knowledge using large-scale language models** [[paper]](https://arxiv.org/abs/2010.00840)  [Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar, Bryan Catanzaro] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/7d884b40ef5892f61e0f6f358b8e29983f64a178?fields=citationCount)]()
- `TACL-2020` **A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation** [[paper]](https://arxiv.org/abs/2001.05139)  [Jian Guan, Fei Huang, Zhihao Zhao, Xiaoyan Zhu, Minlie Huang] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/c6a84615bc36486cd0170f8a3e1b7e5ec8f5344e?fields=citationCount)]()


### Plot Development
- `ArXiv-2023` **End to End Story Plot Generator** [[paper]](https://arxiv.org/abs/2310.08796) [Hanlin Zhu, Andrew Cohen, Danqing Wang, Kevin Yang, Xiaomeng Yang, Jiantao Jiao, Yuandong Tian] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/2dede02e09147614e947ec464f575db6838a0b6c?fields=citationCount)]()
- `RANLP-2023` **Coherent Story Generation with Structured Knowledge** [[paper]](https://aclanthology.org/2023.ranlp-1.74.pdf) [Congda Ma, Kotaro Funakoshi, Kiyoaki Shirai, Manabu Okumura] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/08ba2595613f7e0e54fe28ceb2815c5c0e5da6be?fields=citationCount)]()
- `AAAI Workshop-2023` **Conveying the Predicted Future to Users: A Case Study of Story Plot Prediction** [[paper]](https://arxiv.org/abs/2302.09122)  [Chieh-Yang Huang, Saniya Naphade, Kavya Laalasa Karanam, Ting-Hao 'Kenneth' Huang]  [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/fd8ebaa67ee959b9e794af179feaa2c26a65e86f?fields=citationCount)]()
- `ACL WNU-2022` **Uncovering Surprising Event Boundaries in Narratives** [[paper]](https://aclanthology.org/2022.wnu-1.1/)  [Zhilin Wang, Anna Jafarpour, Maarten Sap]  [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/b6809717e9a1b4b64c879cb18ca30039309f9e84?fields=citationCount)]()
- `AAAI-2020` **Story Realization: Expanding Plot Events into Sentences** [[paper]](https://arxiv.org/abs/1909.03480v2)  [[code]](https://github.com/rajammanabrolu/StoryRealization)   [Prithviraj Ammanabrolu, Ethan Tien, Wesley Cheung, Zhaochen Luo, William Ma, Lara J. Martin, Mark O. Riedl] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/a4dd44938eaf534259aaf4bcb875bb0ab8431c4d?fields=citationCount)]()
- `AAAI-2018` **Event Representations for Automated Story Generation with Deep Neural Nets** [[paper]](https://arxiv.org/abs/1706.01331)  [[code]](https://github.com/lara-martin/ASTER)   [Lara J. Martin, Prithviraj Ammanabrolu, Xinyu Wang, William Hancock, Shruti Singh, Brent Harrison, Mark O. Riedl] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/47a26b0c5d27b99da175e0a719f42d707f97ec3d?fields=citationCount)]()

<!--
update 
-->


### Better Storytelling
- `CoNLL Workshop-2023` **BabyStories: Can Reinforcement Learning Teach Baby Language Models to Write Better Stories?** [[paper]](https://arxiv.org/abs/2310.16681) [Xingmeng Zhao, Tongnian Wang, Sheri Osborn, Anthony Rios]  [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/74a5c1ddb657a7dab8fc3930f9100b2fafa682dd?fields=citationCount)]()
- `EMNLP Findings-2023` **Affective and Dynamic Beam Search for Story Generation** [[paper]](https://arxiv.org/abs/2310.15079) [Tenghao Huang, Ehsan Qasemi, Bangzheng Li, He Wang, Faeze Brahman, Muhao Chen, Snigdha Chaturvedi] b7aff63b893ae0f5178c894b515d1cab00ba97b7
- `EMNLP Findings-2023` **GROVE: A Retrieval-augmented Complex Story Generation Framework with A Forest of Evidence** [[paper]](https://arxiv.org/abs/2310.05388) [Zhihua Wen, Zhiliang Tian, Wei Wu, Yuxin Yang, Yanqi Shi, Zhen Huang, Dongsheng Li]
- `ArXiv-2023` **Creativity Support in the Age of Large Language Models: An Empirical Study Involving Emerging Writers** [[paper]](https://arxiv.org/abs/2309.12570) [Tuhin Chakrabarty, Vishakh Padmakumar, Faeze Brahman, Smaranda Muresan]
- `ACL-2023` **Open-ended Long Text Generation via Masked Language Modeling** [[paper]](https://aclanthology.org/2023.acl-long.13/) [Xiaobo Liang, Zecheng Tang, Juntao Li, Min Zhang]
- `ArXiv-2022` **Creative Writing with an AI-Powered Writing Assistant: Perspectives from Professional Writers** [[paper]](https://arxiv.org/abs/2211.05030) [Daphne Ippolito, Ann Yuan, Andy Coenen, Sehmon Burnam]
- `EMNLP-2022` **Help me write a poem: Instruction Tuning as a Vehicle for Collaborative Poetry Writing** [[paper]](https://arxiv.org/abs/2210.13669) [Tuhin Chakrabarty, Vishakh Padmakumar, He He]
- `EMNLP-2022` **EtriCA: Event-triggered context-aware story generation augmented by cross attention** [[paper]](https://arxiv.org/abs/2210.12463) [Chen Tang, Chenghua Lin, Henglin Huang, Frank Guerin, Zhihao Zhang]
- `AACL-2022` **Improving Chinese Story Generation via Awareness of Syntactic Dependencies and Semantics** [[paper]](https://arxiv.org/abs/2210.10618) [Henglin Huang, Chen Tang, Tyler Loakman, Frank Guerin, Chenghua Lin]
- `ArXiv-2022` **Generating Coherent Narratives by Learning Dynamic and Discrete Entity States with a Contrastive Framework** [[paper]](https://arxiv.org/abs/2208.03985)   [Jian Guan, Zhenyu Yang, Rongsheng Zhang, Zhipeng Hu, Minlie Huang]
- `ArXiv-2022` **Great Expectations: Unsupervised Inference of Suspense, Surprise and Salience in Storytelling** [[paper]](https://arxiv.org/abs/2206.09708) [David Wilmot]
- `NAACL-2022` **Aligning to Social Norms and Values in Interactive Narratives** [[paper]](https://arxiv.org/abs/2205.01975)   [Prithviraj Ammanabrolu, Liwei Jiang, Maarten Sap, Hannaneh Hajishirzi, Yejin Choi]
- `ICASSP-2022` **Clseg: Contrastive learning of story ending generation** [[paper]](https://arxiv.org/abs/2202.09049) [Yuqiang Xie, Yue Hu, Luxi Xing, Yunpeng Li, Wei Peng, Ping Guo]
- `ICML-2022` **Towards Coherent and Consistent Use of Entities in Narrative Generation** [[paper]](https://arxiv.org/abs/2202.01709)   [Pinelopi Papalampidi, Kris Cao, Tomas Kocisky]
- `EMNLP Findings-2021` **Guiding Neural Story Generation with Reader Models** [[paper]](https://arxiv.org/abs/2112.08596) [Xiangyu Peng, Kaige Xie, Amal Alabdulkarim, Harshith Kayam, Samihan Dani, Mark O. Riedl] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/03f079c0d6d5b14a3948e55de0f40677d9634338?fields=citationCount)]()
- `ArXiv-2021` **Goal-Directed Story Generation: Augmenting Generative Language Models with Reinforcement Learning** [[paper]](https://arxiv.org/abs/2112.08593)  [Amal Alabdulkarim, Winston Li, Lara J. Martin, Mark O. Riedl] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/4ae9648bfa97dfe6a01b8bc2282ae363660856f5?fields=citationCount)]()
- `ArXiv-2021` **Automated Story Generation as Question-Answering** [[paper]](https://arxiv.org/abs/2112.03808)  [Louis Castricato, Spencer Frazier, Jonathan Balloch, Nitya Tarakad, Mark Riedl] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/56d2095d64051a95a1050a439e0c4b5db9a735e9?fields=citationCount)]()
- `EMNLP Findings-2021` **Towards Document-Level Paraphrase Generation with Sentence Rewriting and Reordering** [[paper]](https://arxiv.org/abs/2109.07095v1)   [[code]](https://github.com/l-zhe/corpg)   [Zhe Lin, Yitao Cai, Xiaojun Wan] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/9b1263b047b13276f03030670da8175677102c74?fields=citationCount)]()
- `ACL-2021` **Long text generation by modeling sentence-level and discourse-level coherence** [[paper]](https://arxiv.org/abs/2105.08963)  [Jian Guan, Xiaoxi Mao, Changjie Fan, Zitao Liu, Wenbiao Ding, Minlie Huang] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/798c61b2b985e918a74b9aa154e6bc3f01040763?fields=citationCount)]()
- `EMNLP Findings-2022` **Inferring the Reader: Guiding Automated Story Generation with Commonsense Reasoning** [[paper]](https://arxiv.org/abs/2105.01311)  [Xiangyu Peng, Siyan Li, Sarah Wiegreffe, Mark Riedl] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/a791712371ed865cb6debe9cb4d5fd59a3405b85?fields=citationCount)]()
- `INLG-2021` **GraphPlan: Story Generation by Planning with Event Graph** [[paper]](https://arxiv.org/abs/2102.02977)  [Hong Chen, Raphael Shu, Hiroya Takamura, Hideki Nakayama] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/8b7ba36adb432a9bacbd8172c28b016eaca21086?fields=citationCount)]()
- `AACL-2020` **Cue Me In: Content-Inducing Approaches to Interactive Story Generation** [[paper]](https://arxiv.org/abs/2010.09935) [Faeze Brahman, Alexandru Petrusca, Snigdha Chaturvedi] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/a66389733c6090baf3fc07f950afecf122ab3420?fields=citationCount)]()
- `AAAI-2021` **Automated Storytelling via Causal, Commonsense Plot Ordering** [[paper]](https://arxiv.org/abs/2009.00829) [Prithviraj Ammanabrolu, Wesley Cheung, William Broniec, Mark O. Riedl] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/4e0af5f4944c16e3ae49b3c96cce7f81989c30f8?fields=citationCount)]()
- `CHI-2020` **Heteroglossia: In-Situ Story Ideation with the Crowd** [[paper]](https://arxiv.org/abs/2001.04519) [Chieh-Yang Huang, Shih-Hong Huang, Ting-Hao 'Kenneth' Huang] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/500e6de64cfb6e1bd0693f2f9006508065542c69?fields=citationCount)]()
- `EMNLP-2020` **Improving Neural Story Generation by Targeted Common Sense Grounding** [[paper]](https://arxiv.org/abs/1908.09451) [Huanru Henry Mao, Bodhisattwa Prasad Majumder, Julian McAuley, Garrison W. Cottrell] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/3e0201b514f5f09703eaa0eed25afaa9f09be20a?fields=citationCount)]()
- `ACL-2019` **Learning to Control the Fine-grained Sentiment for Story Ending Generation** [[paper]](https://aclanthology.org/P19-1603/) [Fuli Luo, Damai Dai, Pengcheng Yang, Tianyu Liu, Baobao Chang, Zhifang Sui, Xu Sun] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/2dd5a8b04be7199f7d8bb3b727705f7de66ed6c8?fields=citationCount)]()
- `AAAI-2019` **Story Ending Generation with Incremental Encoding and Commonsense Knowledge** [[paper]](https://arxiv.org/abs/1808.10113)  [Jian Guan, Yansen Wang, Minlie Huang] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/d03d24241fc95e018517d6b1e3be40c5dc31ee66?fields=citationCount)]()


### Controllability
- `ArXiv-2023` **Controlling keywords and their positions in text generation** [[paper]](https://arxiv.org/abs/2304.09516)
- `COLING-2022` **Psychology-guided Controllable Story Generation** [[paper]](https://arxiv.org/abs/2210.07493) [Yuqiang Xie, Yue Hu, Yunpeng Li, Guanqun Bi, Luxi Xing, Wei Peng]
- `WWW-2022` **Genre-controllable story generation via supervised contrastive learning** [[paper]](https://dl.acm.org/doi/abs/10.1145/3485447.3512004) [JinUk Cho, MinSu Jeong, JinYeong Bak, Yun-Gyung Cheong]
- `EMNLP Findings-2021` **A Plug-and-Play Method for Controlled Text Generation** [[paper]](https://arxiv.org/abs/2109.09707v1)  [[code]](https://github.com/dapascual/k2t) 
- `ArXiv-2021` **Plug-and-Blend: A Framework for Plug-and-play Controllable Story Generation with Sketches** [[paper]](https://arxiv.org/abs/2104.04039v2)  [[code]](https://github.com/xxbidiao/plug-and-blend) [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/a2b12e3b0440d2d00550adf7620a23b01af84193?fields=citationCount)]()
- `ACL-2018` **Towards Controllable Story Generation** [[paper]](https://aclanthology.org/W18-1505.pdf) [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/f9de0d4a5adefc59bfb033f162d8a4a5212882cf?fields=citationCount)]()

### Characterization
- `EMNLP-2022` **Towards Inter-character Relationship-driven Story Generation** [[paper]](https://arxiv.org/abs/2211.00676)
- `COLING-2022` **CHAE: Fine-Grained Controllable Story Generation with Characters, Actions and Emotions** [[paper]](https://arxiv.org/abs/2210.05221) [Xinpeng Wang, Han Jiang, Zhihua Wei, Shanlin Zhou]
- `ArXiv-2022` **An Ion Exchange Mechanism Inspired Story Ending Generator for Different Characters** [[paper]](https://arxiv.org/abs/2209.00200) [Xinyu Jiang, Qi Zhang, Chongyang Shi, Kaiying Jiang, Liang Hu, Shoujin Wang]
- `NAACL-2022` **TVShowGuess: Character Comprehension in Stories as Speaker Guessing** [[paper]](https://arxiv.org/abs/2204.07721) [Yisi Sang, Xiangyang Mou, Mo Yu, Shunyu Yao, Jing Li, Jeffrey Stanton]
- `NAACL-2022` **Persona-Guided Planning for Controlling the Protagonist’s Persona in Story Generation** [[paper]](https://arxiv.org/abs/2204.10703) [[code]](https://github.com/thu-coai/ConPer) [Zhexin Zhang, Jiaxin Wen, Jian Guan, Minlie Huang]
- `ArXiv-2021` **Modeling Worlds in Text** [[paper]](https://arxiv.org/abs/2106.09578) [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/fc56bbd824b907a7d047f4a37afd61788fa23067?fields=citationCount)]()
- `ACL-2021` **Unsupervised Enrichment of Persona-grounded Dialog with Background Stories** [[paper]](https://arxiv.org/abs/2106.08364) [Bodhisattwa Prasad Majumder, Taylor Berg-Kirkpatrick, Julian McAuley, Harsh Jhamtani] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/8f0686ccf1a706a4cf797e0fd9ee0b9ac007dc91?fields=citationCount)]()
- `SIGDIAL-2021` **Telling Stories through Multi-User Dialogue by Modeling Character Relations** [[paper]](https://arxiv.org/abs/2105.15054) [Wai Man Si, Prithviraj Ammanabrolu, Mark O. Riedl] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/b1d8c868e1d6d4980ee2f8c50e6fc5e4e7027ca2?fields=citationCount)]()


### Writing Style
- `ACL-2023` **StoryTrans: Non-Parallel Story Author-Style Transfer with Discourse Representations and Content Enhancing** [[paper]](https://arxiv.org/abs/2208.13423) [Xuekai Zhu, Jian Guan, Minlie Huang, Juan Liu]
- `ACL-2021` **Stylized story generation with style-guided planning** [[paper]](https://arxiv.org/abs/2105.08625)  [Xiangzhe Kong, Jialiang Huang, Ziquan Tung, Jian Guan, Minlie Huang] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/1513639b0079694855e87006545d55edd57e5e81?fields=citationCount)]()


### Story Planning
- `EMNLP Findings-2023` **Improving Pacing in Long-Form Story Planning** [[paper]](https://arxiv.org/abs/2311.04459) [Yichen Wang, Kevin Yang, Xiaoming Liu, Dan Klein]
- `ArXiv-2023` **EIPE-text: Evaluation-Guided Iterative Plan Extraction for Long-Form Narrative Text Generation** [[paper]](https://arxiv.org/abs/2310.08185) [Wang You, Wenshan Wu, Yaobo Liang, Shaoguang Mao, Chenfei Wu, Maosong Cao, Yuzhe Cai, Yiduo Guo, Yan Xia, Furu Wei, Nan Duan]
- `ArXiv-2023` **Enhancing Generation through Summarization Duality and Explicit Outline Control** [[paper]](https://arxiv.org/abs/2305.14459) [Yunzhe Li, Qian Chen, Weixiang Yan, Wen Wang, Qinglin Zhang, Hari Sundaram]
- `ACL-2023` **DOC: Improving Long Story Coherence With Detailed Outline Control** [[paper]](https://arxiv.org/abs/2212.10077) [Kevin Yang, Dan Klein, Nanyun Peng, Yuandong Tian]
- `CHI-2022` **TaleBrush: Sketching Stories with Generative Pretrained Language Models** [[paper]](http://www.cond.org/talebrush.pdf)  [John Joon Young Chung, Wooseok Kim, Kang Min Yoo, Hwaran Lee, Eytan Adar, Minsuk Chang]
- `ArXiv-2022` **Neural Story Planning** [[paper]](https://arxiv.org/abs/2212.08718) [Anbang Ye, Christopher Cui, Taiwei Shi, Mark O. Riedl]
- `AAAI-2021` **Narrative Plan Generation with Self-Supervised Learning** [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/16747) [Mihai Polceanu, Julie Porteous, Alan Lindsay, Marc Cavazza] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/c4a00c3d61b3656afcde10ba0341e12b3ff54065?fields=citationCount)]()
- `ArXiv-2022` **Event Transition Planning for Open-ended Text Generation** [[paper]](https://arxiv.org/abs/2204.09453) [Qintong Li, Piji Li, Wei Bi, Zhaochun Ren, Yuxuan Lai, Lingpeng Kong]
- `EMNLP-2020` **Content Planning for Neural Story Generation with Aristotelian Rescoring** [[paper]](https://arxiv.org/abs/2009.09870) [Seraphina Goldfarb-Tarrant, Tuhin Chakrabarty, Ralph Weischedel, Nanyun Peng] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/12cfe5d242c940a0383b55978c7419ee6633ed85?fields=citationCount)]()
- `AAAI-2020` **Draft and Edit: Automatic Storytelling Through Multi-Pass Hierarchical Conditional Variational Autoencoder** [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/5538) [Meng-Hsuan Yu, Juntao Li, Danyang Liu, Dongyan Zhao, Rui Yan, Bo Tang, Haisong Zhang] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/b60959f6b9502f90cb3657e89c4df9592577e3ce?fields=citationCount)]()
- `ArXiv-2019` **Strategies for Structuring Story Generation** [[paper]](https://arxiv.org/abs/1902.01109)  [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/2d6c0f7774d9d30d4972f5dba1d6e5389b3ddd2f?fields=citationCount)]()
- `AAAI-2019` **Plan-And-Write: Towards Better Automatic Storytelling** [[paper]](https://arxiv.org/abs/1811.05701) [[code]](https://bitbucket.org/VioletPeng/language-model)  [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/b0e716728e940eb2164892b7e284940157a2cebe?fields=citationCount)]()
- `EMNLP-2018` **A Skeleton-Based Model for Promoting Coherence Among Sentences in Narrative Story Generation** [[paper]](https://arxiv.org/abs/1808.06945) [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/6ac772a03a7ab6cce1fd3afcceff58bbc89da3ff?fields=citationCount)]()
- `ACL-2018` **Hierarchical Neural Story Generation** [[paper]](https://arxiv.org/abs/1805.04833) [[code]](https://github.com/kevalnagda/StoryGeneration) [[Writing prompt]](https://www.kaggle.com/ratthachat/writing-prompts) [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/29de7c0fb3c09eaf55b20619bceaeafe72fd87a6?fields=citationCount)]()


### Prompt Design
- `ACL Findings-2023` **CoRRPUS: Code-based Structured Prompting for Neurosymbolic Story Understanding** [[paper]](https://arxiv.org/abs/2212.10754)  [Yijiang River Dong, Lara J. Martin, Chris Callison-Burch]
- `EMNLP-2022` **Re3: Generating longer stories with recursive reprompting and revision** [[paper]](https://arxiv.org/abs/2210.06774) [Kevin Yang, Yuandong Tian, Nanyun Peng, Dan Klein]
- `NAACL-2022` **Go Back in Time: Generating Flashbacks in Stories with Event Temporal Prompts** [[paper]](https://arxiv.org/abs/2205.01898)  [Rujun Han, Hong Chen, Yufei Tian, Nanyun Peng]  [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/078f4efd448822b0e25d3ee0aec842ced606a595?fields=citationCount)]()
- `SIGIR-2022` **What makes the story forward? inferring commonsense explanations as prompts for future event generation** [[paper]](https://arxiv.org/abs/2201.07099) [Li Lin, Yixin Cao, Lifu Huang, Shu'ang Li, Xuming Hu, Lijie Wen, Jianmin Wang]


<!--
update 
-->

### Evaluation
- `ArXiv-2023` **Experimental Narratives: A Comparison of Human Crowdsourced Storytelling and AI Storytelling** [[paper]](https://arxiv.org/abs/2310.12902) [Nina Begus] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/db599a0ffcaf891bda55b62dafe348c3cc88ec6e?fields=citationCount)]()
- `ArXiv-2023` **EIPE-text: Evaluation-Guided Iterative Plan Extraction for Long-Form Narrative Text Generation** [[paper]](https://arxiv.org/abs/2310.08185) [Wang You, Wenshan Wu, Yaobo Liang, Shaoguang Mao, Chenfei Wu, Maosong Cao, Yuzhe Cai, Yiduo Guo, Yan Xia, Furu Wei, Nan Duan]
- `ArXiv-2023` **Learning Personalized Story Evaluation** [[paper]](https://arxiv.org/abs/2310.03304) [Danqing Wang, Kevin Yang, Hanlin Zhu, Xiaomeng Yang, Andrew Cohen, Lei Li, Yuandong Tian]
- `ArXiv-2023` **BooookScore: A systematic exploration of book-length summarization in the era of LLMs**[[paper]](https://arxiv.org/abs/2310.00785)[Yapei Chang, Kyle Lo, Tanya Goyal, Mohit Iyyer]
- `ArXiv-2023` **TIGERScore: Towards Building Explainable Metric for All Text Generation Tasks**[[paper]](https://arxiv.org/abs/2310.00752)[Dongfu Jiang, Yishan Li, Ge Zhang, Wenhao Huang, Bill Yuchen Lin, Wenhu Chen]
- `ArXiv-2023` **Art or Artifice? Large Language Models and the False Promise of Creativity** [[paper]](https://arxiv.org/abs/2309.14556) [Tuhin Chakrabarty, Philippe Laban, Divyansh Agarwal, Smaranda Muresan, Chien-Sheng Wu]
- `ACL-2023` **HAUSER: Towards Holistic and Automatic Evaluation of Simile Generation** [[paper]](https://arxiv.org/abs/2306.07554) [Qianyu He, Yikai Zhang, Jiaqing Liang, Yuncheng Huang, Yanghua Xiao, Yunwen Chen]
- `ACL-2023` **Can Large Language Models Be an Alternative to Human Evaluations?** [[paper]](https://arxiv.org/abs/2305.01937) [Cheng-Han Chiang, Hung-yi Lee]
- `ArXiv-2023` **Exploring the Use of Large Language Models for Reference-Free Text Quality Evaluation: An Empirical Study** [[paper]](https://arxiv.org/abs/2304.00723) [Yi Chen, Rui Wang, Haiyun Jiang, Shuming Shi, Ruifeng Xu]
- `ArXiv-2023` **DeltaScore: Evaluating Story Generation with Differentiating Perturbations** [[paper]](https://arxiv.org/abs/2303.08991) [Zhuohan Xie, Miao Li, Trevor Cohn, Jey Han Lau]
- `EMNLP-2022` **Automatic Comment Generation for Chinese Student Narrative Essays** [[paper]](https://aclanthology.org/2022.emnlp-demos.21/) [Zhexin Zhang, Jian Guan, Guowei Xu, Yixiang Tian, Minlie Huang]
- `EMNLP-2022` **StoryER: Automatic Story Evaluation via Ranking, Rating and Reasoning** [[paper]](https://arxiv.org/abs/2210.08459) [Hong Chen, Duc Minh Vo, Hiroya Takamura, Yusuke Miyao, Hideki Nakayama]
- `ArXiv-2022` **A Benchmark for Understanding and Generating Dialogue between Characters in Stories** [[paper]](https://arxiv.org/abs/2209.08524) [Jianzhu Yao, Ziqi Liu, Jian Guan, Minlie Huang]
- `ArXiv-2022` **The Glass Ceiling of Automatic Evaluation in Natural Language Generation** [[paper]](https://arxiv.org/abs/2208.14585) [Pierre Colombo, Maxime Peyrard, Nathan Noiry, Robert West, Pablo Piantanida]
- `COLING-2022` **Of Human Criteria and Automatic Metrics: A Benchmark of the Evaluation of Story Generation** [[paper]](https://arxiv.org/abs/2208.11646)  [Cyril Chhun, Pierre Colombo, Chloé Clavel, Fabian M. Suchanek]
- `ArXiv-2021` **Toward Educator-focused Automated Scoring Systems for Reading and Writing** [[paper]](https://arxiv.org/abs/2112.11973) [Mike Hardy]
- `TACL-2022` **LOT: A story-centric benchmark for evaluating Chinese long text understanding and generation** [[paper]](https://arxiv.org/abs/2108.12960) [Jian Guan, Zhuoer Feng, Yamei Chen, Ruilin He, Xiaoxi Mao, Changjie Fan, Minlie Huang]
- `ACL-2021` **Openmeva: A benchmark for evaluating open-ended story generation metrics** [[paper]](https://arxiv.org/abs/2105.08920) [Jian Guan, Zhexin Zhang, Zhuoer Feng, Zitao Liu, Wenbiao Ding, Xiaoxi Mao, Changjie Fan, Minlie Huang] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/7ffc1b425026e916cd6db37c79df3e08e8f47ee6?fields=citationCount)]()
- `EMNLP-2020` **Union: An unreferenced metric for evaluating open-ended story generation** [[paper]](https://arxiv.org/abs/2009.07602) [Jian Guan, Minlie Huang] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/70aa38ddb852ff33fcf990792ca0690047464f99?fields=citationCount)]()


### Application
- `ArXiv-2023` **Inspo: Writing Stories with a Flock of AIs and Humans**  [[paper]](https://arxiv.org/abs/2311.16521)  [Chieh-Yang Huang, Sanjana Gautam, Shannon McClellan Brooks, Ya-Fang Lin, Ting-Hao 'Kenneth' Huang]
- `ArXiv-2023` **NarrativePlay: Interactive Narrative Understanding**  [[paper]](https://arxiv.org/abs/2310.01459)   [Runcong Zhao, Wenjia Zhang, Jiazheng Li, Lixing Zhu, Yanran Li, Yulan He, Lin Gui]
- `AAAI-2023` **SceneCraft: Automating Interactive Narrative Scene Generation in Digital Games with Large Language Models** [[paper]](https://ojs.aaai.org/index.php/AIIDE/article/view/27504) [Vikram Kumaran, Jonathan Rowe, Bradford Mott, James Lester]
- `UIST-2023` **Storyfier: Exploring Vocabulary Learning Support with Text Generation Models**[[paper]](https://arxiv.org/abs/2308.03864) [Zhenhui Peng, Xingbo Wang, Qiushi Han, Junkai Zhu, Xiaojuan Ma, Huamin Qu]
- `FDG-2022` **TropeTwist: Trope-based Narrative Structure Generation** [[paper]](https://arxiv.org/abs/2204.09672) [Alberto Alvarez, Jose Font]
- `IUI-2022` **Wordcraft: Story Writing With Large Language Models** [[paper]](https://dl.acm.org/doi/10.1145/3490099.3511105) [Ann Yuan, Andy Coenen, Emily Reif, Daphne Ippolito] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/fb5c11bbf63884f75d2da615fbf37a3bcfa2bd20?fields=citationCount)]()
- `AAAI-2020` **Generating Interactive Worlds with Text** [[paper]](https://arxiv.org/abs/1911.09194)  [Angela Fan, Jack Urbanek, Pratik Ringshia, Emily Dinan, Emma Qian, Siddharth Karamcheti, Shrimai Prabhumoye, Douwe Kiela, Tim Rocktaschel, Arthur Szlam, Jason Weston] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/4b891175d01123422d64b12cc5b15a50de98bf87?fields=citationCount)]()
- `EMNLP-2019` **Learning to Speak and Act in a Fantasy Text Adventure Game** [[paper]](https://arxiv.org/abs/1903.03094)  [Jack Urbanek, Angela Fan, Siddharth Karamcheti, Saachi Jain, Samuel Humeau, Emily Dinan, Tim Rocktäschel, Douwe Kiela, Arthur Szlam, Jason Weston] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/f7c455cc5a40d2a31b63ac2657c9d2d6c53b1be5?fields=citationCount)]()
- `IJCAI-2018` **TextWorld: A Learning Environment for Text-based Game** [[paper]](https://arxiv.org/abs/1806.11532)  [Marc-Alexandre Côté, Ákos Kádár, Xingdi Yuan, Ben Kybartas, Tavian Barnes, Emery Fine, James Moore, Matthew Hausknecht, Layla El Asri, Mahmoud Adada, Wendy Tay, Adam Trischler] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/89daae27e7df4a418b9610d307ce3df0e30fc8a2?fields=citationCount)]()


### Dataset
- `ArXiv-2023` **STONYBOOK: A System and Resource for Large-Scale Analysis of Novels** [[paper]](https://arxiv.org/abs/2311.03614) [Charuta Pethe, Allen Kim, Rajesh Prabhakar, Tanzir Pial, Steven Skiena] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/402a7b3947116b46fa4e1ca5c6f57bd595f50bf2?fields=citationCount)]()
- `ACL-2023` **StoryWars: A Dataset and Instruction Tuning Baselines for Collaborative Story Understanding and Generation** [[paper]](https://arxiv.org/abs/2305.08152) [Yulun Du, Lydia Chilton]
- `INLG-2023` **Long Story Generation Challenge** [[paper]](https://aclanthology.org/2023.inlg-genchal.2/) [Nikolay Mikhaylovskiy]
- `ArXiv-2022` **PASTA: A Dataset for Modeling Participant States in Narratives** [[paper]](https://arxiv.org/abs/2208.00329) [Sayontan Ghosh, Mahnaz Koupaee, Isabella Chen, Francis Ferraro, Nathanael Chambers, Niranjan Balasubramanian]
- `NAACL-2022` **A corpus for understanding and generating moral stories** [[paper]](https://arxiv.org/abs/2204.09438) [Jian Guan, Ziqi Liu, Minlie Huang]
- `EVAL4NLP-2021` **StoryDB: Broad Multi-language Narrative Dataset** [[paper]](https://arxiv.org/abs/2109.14396) [Alexey Tikhonov, Igor Samenko, Ivan P. Yamshchikov]  [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/9ab78eb54f26693cff1cc07335c31e698349f972?fields=citationCount)]()
- `ACL-2022` **SummScreen: A Dataset for Abstractive Screenplay Summarization** [[paper]](https://arxiv.org/abs/2104.07091) [[code]](https://github.com/mingdachen/SummScreen) [Mingda Chen, Zewei Chu, Sam Wiseman, Kevin Gimpel]
- `NAACL-2016` **A Corpus and Evaluation Framework for Deeper Understanding of Commonsense Stories** [[paper]](https://arxiv.org/abs/1604.01696) [Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong He, Devi Parikh, Dhruv Batra, Lucy Vanderwende, Pushmeet Kohli, James Allen] [![](https://img.shields.io/badge/dynamic/json?label=citation&query=citationCount&url=https://api.semanticscholar.org/graph/v1/paper/2a0114dc4d8ee374506be68bda20c8cd78200c66?fields=citationCount)]()


## Public Data
- [ROC Stories](https://cs.rochester.edu/nlp/rocstories/) is a compilation of 100,000 five-sentence stories and 3,742 Story Cloze Test stories, capturing a rich array of causal and temporal commonsense connections between everyday events, making it suitable for story generation tasks.
- [CommonGen](https://inklab.usc.edu/CommonGen/) was developed by combining crowdsourced and existing caption corpora, containing 79k commonsense descriptions across 35k distinct concept-sets.
- [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) offers access to a dataset containing movie plot summaries and related metadata.
- [Scifi TV Show Plot Summaries & Events](https://huggingface.co/datasets/lara-martin/Scifi_TV_Shows) is a collection of plot synopses for long-running (80+ episodes) science fiction TV shows, sourced from Fandom.com wikis.
- [The LIGHT project](https://github.com/facebookresearch/ParlAI/tree/main/projects/light) serves as a large-scale fantasy text adventure game research platform, designed to train agents capable of both talking and acting, while interacting with other models or humans.
- [The TextWorld project](https://github.com/microsoft/TextWorld) is a sandbox learning environment aimed at training and evaluating reinforcement learning (RL) agents on text-based games.

![Star History Chart](https://api.star-history.com/svg?repos=yingpengma/Awesome-Story-Generation&type=Date)
