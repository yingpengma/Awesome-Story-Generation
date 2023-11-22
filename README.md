<h1 align="center">Awesome-Story-Generation</h1>

<div align="center">Contributed by <a href="https://yingpengma.github.io/">Yingpeng Ma</a></div>

## Table of Contents

- [Introduction](#introduction)
- [Related Repository](#related-repository)
- [Papers](#papers)
  - [Literature Review](#literature-review)
  - [Language Models](#language-models)
  - [Plot Development](#plot-development)
  - [Improving Storytelling](#improving-storytelling)
  - [Controllability](#controllability)
  - [Characterization](#characterization)
  - [Writing Style](#writing-style)
  - [Story Outlining](#story-outlining)
  - [Prompt Design](#prompt-design)
  - [Evaluation Methods](#evaluation-methods)
  - [Applications](#applications)
  - [Datasets](#datasets)
- [Public Data](#public-data)

## Introduction
This repository collects an extensive list of awesome papers about **Story Generation** / **Storytelling**, primarily focusing on the era of **Large Language Models (LLMs)**.

All papers are sorted in **chronological order**, with the most recent ones appearing at the top.

We would like to extend our heartfelt gratitude to 「 [**Awesome-story-generation**](https://github.com/Whorra/Awesome-story-generation) 」,  「 [**PaperForONLG**](https://github.com/thu-coai/PaperForONLG) 」 for their invaluable assistance and contributions.

Open issues and make PRs freely! If you have any suggestions or questions, please do not hesitate to reach out to me:

`mayingpeng33 [AT] gmail [DOT] com`

## Related Repository
|**[Awesome-LLM-Characters](https://github.com/yingpengma/Awesome-LLM-Characters)**|
|:---:|

## Papers

Eg. `ACL-2023` **Title** [paper] [code] .. [authors]


### Literature Review
- `ArXiv-2023` **Are NLP Models Good at Tracing Thoughts: An Overview of Narrative Understanding** [[paper]](https://arxiv.org/abs/2310.18783) [Lixing Zhu, Runcong Zhao, Lin Gui, Yulan He]
- `Neurocomputing-2023` **Open-world story generation with structured knowledge enhancement: A comprehensive survey** [[paper]](https://arxiv.org/abs/2212.04634) [Yuxin Wang, Jieru Lin, Zhiwei Yu, Wei Hu, Börje F. Karlsson]
- `NeurIPS-2022` **Factuality Enhanced Language Models for Open-Ended Text Generation** [[paper]](https://proceedings.neurips.cc/paper_files/paper/2022/file/df438caa36714f69277daa92d608dd63-Paper-Conference.pdf)   [Nayeon Lee, Wei Ping, Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro]
- `ArXiv-2022` **Survey: Automatic Movie Plot and Script Generation** [[paper]](https://www.cfilt.iitb.ac.in/resources/surveys/2022/prerak-ampsg-survey-27jun22.pdf)  [Prerak Gandhi, Pushpak Bhattacharyya]
- `ArXiv-2021` **Automatic Story Generation: Challenges and Attempts** [[paper]](https://arxiv.org/abs/2102.12634) [Amal Alabdulkarim, Siyan Li, Xiangyu Peng]

### Language Models
- `ArXiv-2023` **RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text** [[paper]](https://arxiv.org/abs/2305.13304) [[code]](https://github.com/aiwaves-cn/RecurrentGPT) [Wangchunshu Zhou, Yuchen Eleanor Jiang, Peng Cui, Tiannan Wang, Zhenxin Xiao, Yifan Hou, Ryan Cotterell, Mrinmaya Sachan]
- `INLG-2023` **The Next Chapter: A Study of Large Language Models in Storytelling** [[paper]](https://arxiv.org/abs/2301.09790) [Zhuohan Xie, Trevor Cohn, Jey Han Lau]
- `ArXiv-2022` **Little Red Riding Hood Goes Around the Globe:Crosslingual Story Planning and Generation with Large Language Models** [[paper]](https://arxiv.org/abs/2212.10471) [Evgeniia Razumovskaia, Joshua Maynez, Annie Louis, Mirella Lapata, Shashi Narayan]
- `ArXiv-2022` **Future Sight: Dynamic Story Generation with Large Pretrained Language Models** [[paper]](https://arxiv.org/abs/2212.09947) [Brian D. Zimmerman, Gaurav Sahu, Olga Vechtomova]
- `CHI-2022` **Co-Writing Screenplays and Theatre Scripts with Language Models: An Evaluation by Industry Professionals** [[paper]](https://arxiv.org/abs/2209.14958)  [Piotr Mirowski, Kory W. Mathewson, Jaylen Pittman, Richard Evans]
- `ArXiv-2022` **Plot Writing From Pre-Trained Language Models** [[paper]](https://arxiv.org/abs/2206.03021) [Yiping Jin, Vishakha Kadam, Dittaya Wanvarie]
- `EMNLP-2020` **MEGATRON-CNTRL: Controllable story generation with external knowledge using large-scale language models** [[paper]](https://arxiv.org/abs/2010.00840)  [Peng Xu, Mostofa Patwary, Mohammad Shoeybi, Raul Puri, Pascale Fung, Anima Anandkumar, Bryan Catanzaro]
- `TACL-2020` **A Knowledge-Enhanced Pretraining Model for Commonsense Story Generation** [[paper]](https://arxiv.org/abs/2001.05139)  [Jian Guan, Fei Huang, Zhihao Zhao, Xiaoyan Zhu, Minlie Huang]


### Plot Development
- `ArXiv-2023` **End to End Story Plot Generator** [[paper]](https://arxiv.org/abs/2310.08796) [Hanlin Zhu, Andrew Cohen, Danqing Wang, Kevin Yang, Xiaomeng Yang, Jiantao Jiao, Yuandong Tian]
- `RANLP-2023` **Coherent Story Generation with Structured Knowledge** [[paper]](https://aclanthology.org/2023.ranlp-1.74.pdf) [Congda Ma, Kotaro Funakoshi, Kiyoaki Shirai, Manabu Okumura]
- `AAAI Workshop-2023` **Conveying the Predicted Future to Users: A Case Study of Story Plot Prediction** [[paper]](https://arxiv.org/abs/2302.09122)  [Chieh-Yang Huang, Saniya Naphade, Kavya Laalasa Karanam, Ting-Hao 'Kenneth' Huang] 
- `ACL WNU-2022` **Uncovering Surprising Event Boundaries in Narratives** [[paper]](https://aclanthology.org/2022.wnu-1.1/)  [Zhilin Wang, Anna Jafarpour, Maarten Sap] 
- `AAAI-2020` **Story Realization: Expanding Plot Events into Sentences** [[paper]](https://arxiv.org/abs/1909.03480v2)  [[code]](https://github.com/rajammanabrolu/StoryRealization)   [Prithviraj Ammanabrolu, Ethan Tien, Wesley Cheung, Zhaochen Luo, William Ma, Lara J. Martin, Mark O. Riedl]
- `AAAI-2018` **Event Representations for Automated Story Generation with Deep Neural Nets** [[paper]](https://arxiv.org/abs/1706.01331)  [[code]](https://github.com/lara-martin/ASTER)   [Lara J. Martin, Prithviraj Ammanabrolu, Xinyu Wang, William Hancock, Shruti Singh, Brent Harrison, Mark O. Riedl]

### Improving Storytelling
- `EMNLP Findings-2023` **Affective and Dynamic Beam Search for Story Generation** [[paper]](https://arxiv.org/abs/2310.15079) [Tenghao Huang, Ehsan Qasemi, Bangzheng Li, He Wang, Faeze Brahman, Muhao Chen, Snigdha Chaturvedi]
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
- `EMNLP-2021` **Guiding Neural Story Generation with Reader Models** [[paper]](https://arxiv.org/abs/2112.08596) [Xiangyu Peng, Kaige Xie, Amal Alabdulkarim, Harshith Kayam, Samihan Dani, Mark O. Riedl]
- `ArXiv-2021` **Goal-Directed Story Generation: Augmenting Generative Language Models with Reinforcement Learning** [[paper]](https://arxiv.org/abs/2112.08593)  [Amal Alabdulkarim, Winston Li, Lara J. Martin, Mark O. Riedl]
- `EMNLP Findings-2021` **Towards Document-Level Paraphrase Generation with Sentence Rewriting and Reordering** [[paper]](https://arxiv.org/abs/2109.07095v1)   [[code]](https://github.com/l-zhe/corpg)   [Zhe Lin, Yitao Cai, Xiaojun Wan]
- `ACL-2021` **Long text generation by modeling sentence-level and discourse-level coherence** [[paper]](https://arxiv.org/abs/2105.08963)  [Jian Guan, Xiaoxi Mao, Changjie Fan, Zitao Liu, Wenbiao Ding, Minlie Huang]
- `CHI-2020` **Heteroglossia: In-Situ Story Ideation with the Crowd** [[paper]](https://arxiv.org/abs/2001.04519) [Chieh-Yang Huang, Shih-Hong Huang, Ting-Hao 'Kenneth' Huang]
- `EMNLP-2020` **Improving Neural Story Generation by Targeted Common Sense Grounding** [[paper]](https://arxiv.org/abs/1908.09451) [Huanru Henry Mao, Bodhisattwa Prasad Majumder, Julian McAuley, Garrison W. Cottrell]
- `ACL-2019` **Learning to Control the Fine-grained Sentiment for Story Ending Generation** [[paper]](https://aclanthology.org/P19-1603/) [Fuli Luo, Damai Dai, Pengcheng Yang, Tianyu Liu, Baobao Chang, Zhifang Sui, Xu Sun]
- `AAAI-2019` **Story Ending Generation with Incremental Encoding and Commonsense Knowledge** [[paper]](https://arxiv.org/abs/1808.10113)  [Jian Guan, Yansen Wang, Minlie Huang]


### Controllability
- `ArXiv-2023` **Controlling keywords and their positions in text generation** [[paper]](https://arxiv.org/abs/2304.09516)
- `COLING-2022` **Psychology-guided Controllable Story Generation** [[paper]](https://arxiv.org/abs/2210.07493) [Yuqiang Xie, Yue Hu, Yunpeng Li, Guanqun Bi, Luxi Xing, Wei Peng]
- `WWW-2022` **Genre-controllable story generation via supervised contrastive learning** [[paper]](https://dl.acm.org/doi/abs/10.1145/3485447.3512004) [JinUk Cho, MinSu Jeong, JinYeong Bak, Yun-Gyung Cheong]
- `EMNLP Findings-2021` **A Plug-and-Play Method for Controlled Text Generation** [[paper]](https://arxiv.org/abs/2109.09707v1)  [[code]](https://github.com/dapascual/k2t) 
- `ArXiv-2021` **Plug-and-Blend: A Framework for Plug-and-play Controllable Story Generation with Sketches** [[paper]](https://arxiv.org/abs/2104.04039v2)  [[code]](https://github.com/xxbidiao/plug-and-blend) 
- `ACL-2018` **Towards Controllable Story Generation** [[paper]](https://aclanthology.org/W18-1505.pdf) 

### Characterization
- `EMNLP-2022` **Towards Inter-character Relationship-driven Story Generation** [[paper]](https://arxiv.org/abs/2211.00676)
- `COLING-2022` **CHAE: Fine-Grained Controllable Story Generation with Characters, Actions and Emotions** [[paper]](https://arxiv.org/abs/2210.05221) [Xinpeng Wang, Han Jiang, Zhihua Wei, Shanlin Zhou]
- `ArXiv-2022` **An Ion Exchange Mechanism Inspired Story Ending Generator for Different Characters** [[paper]](https://arxiv.org/abs/2209.00200) [Xinyu Jiang, Qi Zhang, Chongyang Shi, Kaiying Jiang, Liang Hu, Shoujin Wang]
- `NAACL-2022` **TVShowGuess: Character Comprehension in Stories as Speaker Guessing** [[paper]](https://arxiv.org/abs/2204.07721) [Yisi Sang, Xiangyang Mou, Mo Yu, Shunyu Yao, Jing Li, Jeffrey Stanton]
- `NAACL-2022` **Persona-Guided Planning for Controlling the Protagonist’s Persona in Story Generation** [[paper]](https://arxiv.org/abs/2204.10703) [[code]](https://github.com/thu-coai/ConPer) [Zhexin Zhang, Jiaxin Wen, Jian Guan, Minlie Huang]
- `ArXiv-2021` **Modeling Worlds in Text** [[paper]](https://arxiv.org/abs/2106.09578) 
- `ACL-2021` **Unsupervised Enrichment of Persona-grounded Dialog with Background Stories** [[paper]](https://arxiv.org/abs/2106.08364) [Bodhisattwa Prasad Majumder, Taylor Berg-Kirkpatrick, Julian McAuley, Harsh Jhamtani]
- `ACL-2021` **Telling Stories through Multi-User Dialogue by Modeling Character Relations** [[paper]](https://arxiv.org/abs/2105.15054v1)


### Writing Style
- `ACL-2023` **StoryTrans: Non-Parallel Story Author-Style Transfer with Discourse Representations and Content Enhancing** [[paper]](https://arxiv.org/abs/2208.13423) [Xuekai Zhu, Jian Guan, Minlie Huang, Juan Liu]
- `ACL-2021` **Stylized story generation with style-guided planning** [[paper]](https://arxiv.org/abs/2105.08625)  [Xiangzhe Kong, Jialiang Huang, Ziquan Tung, Jian Guan, Minlie Huang]


### Story Outlining
- `EMNLP Findings-2023` **Improving Pacing in Long-Form Story Planning** [[paper]](https://arxiv.org/abs/2311.04459) [Yichen Wang, Kevin Yang, Xiaoming Liu, Dan Klein]
- `ArXiv-2023` **EIPE-text: Evaluation-Guided Iterative Plan Extraction for Long-Form Narrative Text Generation** [[paper]](https://arxiv.org/abs/2310.08185) [Wang You, Wenshan Wu, Yaobo Liang, Shaoguang Mao, Chenfei Wu, Maosong Cao, Yuzhe Cai, Yiduo Guo, Yan Xia, Furu Wei, Nan Duan]
- `ArXiv-2023` **Enhancing Generation through Summarization Duality and Explicit Outline Control** [[paper]](https://arxiv.org/abs/2305.14459) [Yunzhe Li, Qian Chen, Weixiang Yan, Wen Wang, Qinglin Zhang, Hari Sundaram]
- `ACL-2023` **DOC: Improving Long Story Coherence With Detailed Outline Control** [[paper]](https://arxiv.org/abs/2212.10077) [Kevin Yang, Dan Klein, Nanyun Peng, Yuandong Tian]
- `CHI-2022` **TaleBrush: Sketching Stories with Generative Pretrained Language Models** [[paper]](http://www.cond.org/talebrush.pdf)  [John Joon Young Chung, Wooseok Kim, Kang Min Yoo, Hwaran Lee, Eytan Adar, Minsuk Chang]
- `ArXiv-2022` **Neural Story Planning** [[paper]](https://arxiv.org/abs/2212.08718) [Anbang Ye, Christopher Cui, Taiwei Shi, Mark O. Riedl]
- `ArXiv-2022` **Event Transition Planning for Open-ended Text Generation** [[paper]](https://arxiv.org/abs/2204.09453) [Qintong Li, Piji Li, Wei Bi, Zhaochun Ren, Yuxuan Lai, Lingpeng Kong]
- `AAAI-2020` **Draft and Edit: Automatic Storytelling Through Multi-Pass Hierarchical Conditional Variational Autoencoder** [[paper]](https://ojs.aaai.org/index.php/AAAI/article/view/5538) [Meng-Hsuan Yu, Juntao Li, Danyang Liu, Dongyan Zhao, Rui Yan, Bo Tang, Haisong Zhang]
- `ArXiv-2019` **Strategies for Structuring Story Generation** [[paper]](https://arxiv.org/abs/1902.01109) 
- `AAAI-2019` **Plan-And-Write: Towards Better Automatic Storytelling** [[paper]](https://arxiv.org/abs/1811.05701) [[code]](https://bitbucket.org/VioletPeng/language-model) 
- `EMNLP-2018` **A Skeleton-Based Model for Promoting Coherence Among Sentences in Narrative Story Generation** [[paper]](https://arxiv.org/abs/1808.06945)
- `ACL-2018` **Hierarchical Neural Story Generation** [[paper]](https://arxiv.org/abs/1805.04833) [[code]](https://github.com/kevalnagda/StoryGeneration) [[Writing prompt]](https://www.kaggle.com/ratthachat/writing-prompts)


### Prompt Design
- `ACL Findings-2023` **CoRRPUS: Code-based Structured Prompting for Neurosymbolic Story Understanding** [[paper]](https://arxiv.org/abs/2212.10754)  [Yijiang River Dong, Lara J. Martin, Chris Callison-Burch]
- `EMNLP-2022` **Re3: Generating longer stories with recursive reprompting and revision** [[paper]](https://arxiv.org/abs/2210.06774) [Kevin Yang, Yuandong Tian, Nanyun Peng, Dan Klein]
- `NAACL-2022` **Go Back in Time: Generating Flashbacks in Stories with Event Temporal Prompts** [[paper]](https://arxiv.org/abs/2205.01898)  [Rujun Han, Hong Chen, Yufei Tian, Nanyun Peng]
- `SIGIR-2022` **What makes the story forward? inferring commonsense explanations as prompts for future event generation** [[paper]](https://arxiv.org/abs/2201.07099) [Li Lin, Yixin Cao, Lifu Huang, Shu'ang Li, Xuming Hu, Lijie Wen, Jianmin Wang]


<!--
update 
-->


### Evaluation Methods
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
- `ACL-2021` **Openmeva: A benchmark for evaluating open-ended story generation metrics** [[paper]](https://arxiv.org/abs/2105.08920) [Jian Guan, Zhexin Zhang, Zhuoer Feng, Zitao Liu, Wenbiao Ding, Xiaoxi Mao, Changjie Fan, Minlie Huang]
- `EMNLP-2020` **Union: An unreferenced metric for evaluating open-ended story generation** [[paper]](https://arxiv.org/abs/2009.07602) [Jian Guan, Minlie Huang]


### Applications
- `ArXiv-2023` **NarrativePlay: Interactive Narrative Understanding**  [[paper]](https://arxiv.org/abs/2310.01459)   [Runcong Zhao, Wenjia Zhang, Jiazheng Li, Lixing Zhu, Yanran Li, Yulan He, Lin Gui]
- `AAAI-2023` **SceneCraft: Automating Interactive Narrative Scene Generation in Digital Games with Large Language Models**[[paper]](https://ojs.aaai.org/index.php/AIIDE/article/view/27504) [Vikram Kumaran, Jonathan Rowe, Bradford Mott, James Lester]
- `UIST-2023` **Storyfier: Exploring Vocabulary Learning Support with Text Generation Models**[[paper]](https://arxiv.org/abs/2308.03864) [Zhenhui Peng, Xingbo Wang, Qiushi Han, Junkai Zhu, Xiaojuan Ma, Huamin Qu]
- `FDG-2022` **TropeTwist: Trope-based Narrative Structure Generation** [[paper]](https://arxiv.org/abs/2204.09672) [Alberto Alvarez, Jose Font]
- `AAAI-2020` **Generating Interactive Worlds with Text** [[paper]](https://arxiv.org/abs/1911.09194)  [Angela Fan, Jack Urbanek, Pratik Ringshia, Emily Dinan, Emma Qian, Siddharth Karamcheti, Shrimai Prabhumoye, Douwe Kiela, Tim Rocktaschel, Arthur Szlam, Jason Weston]
- `EMNLP-2019` **Learning to Speak and Act in a Fantasy Text Adventure Game** [[paper]](https://arxiv.org/abs/1903.03094)  [Jack Urbanek, Angela Fan, Siddharth Karamcheti, Saachi Jain, Samuel Humeau, Emily Dinan, Tim Rocktäschel, Douwe Kiela, Arthur Szlam, Jason Weston]
- `IJCAI-2018` **TextWorld: A Learning Environment for Text-based Game** [[paper]](https://arxiv.org/abs/1806.11532)  [Marc-Alexandre Côté, Ákos Kádár, Xingdi Yuan, Ben Kybartas, Tavian Barnes, Emery Fine, James Moore, Matthew Hausknecht, Layla El Asri, Mahmoud Adada, Wendy Tay, Adam Trischler]


### Datasets
- `ACL-2023` **StoryWars: A Dataset and Instruction Tuning Baselines for Collaborative Story Understanding and Generation** [[paper]](https://arxiv.org/abs/2305.08152) [Yulun Du, Lydia Chilton]
- `INLG-2023` **Long Story Generation Challenge** [[paper]](https://aclanthology.org/2023.inlg-genchal.2/) [Nikolay Mikhaylovskiy]
- `ArXiv-2022` **PASTA: A Dataset for Modeling Participant States in Narratives** [[paper]](https://arxiv.org/abs/2208.00329) [Sayontan Ghosh, Mahnaz Koupaee, Isabella Chen, Francis Ferraro, Nathanael Chambers, Niranjan Balasubramanian]
- `NAACL-2022` **A corpus for understanding and generating moral stories** [[paper]](https://arxiv.org/abs/2204.09438) [Jian Guan, Ziqi Liu, Minlie Huang]
- `ACL-2022` **SummScreen: A Dataset for Abstractive Screenplay Summarization** [[paper]](https://arxiv.org/abs/2104.07091) [[code]](https://github.com/mingdachen/SummScreen) [Mingda Chen, Zewei Chu, Sam Wiseman, Kevin Gimpel]
- `NAACL-2016` **A Corpus and Evaluation Framework for Deeper Understanding of Commonsense Stories** [[paper]](https://arxiv.org/abs/1604.01696) [Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong He, Devi Parikh, Dhruv Batra, Lucy Vanderwende, Pushmeet Kohli, James Allen]


## Public Data
- [ROC Stories](https://cs.rochester.edu/nlp/rocstories/) is a compilation of 100,000 five-sentence stories and 3,742 Story Cloze Test stories, capturing a rich array of causal and temporal commonsense connections between everyday events, making it suitable for story generation tasks.
- [CommonGen](https://inklab.usc.edu/CommonGen/) was developed by combining crowdsourced and existing caption corpora, containing 79k commonsense descriptions across 35k distinct concept-sets.
- [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) offers access to a dataset containing movie plot summaries and related metadata.
- [Scifi TV Show Plot Summaries & Events](https://huggingface.co/datasets/lara-martin/Scifi_TV_Shows) is a collection of plot synopses for long-running (80+ episodes) science fiction TV shows, sourced from Fandom.com wikis.
- [The LIGHT project](https://github.com/facebookresearch/ParlAI/tree/main/projects/light) serves as a large-scale fantasy text adventure game research platform, designed to train agents capable of both talking and acting, while interacting with other models or humans.
- [The TextWorld project](https://github.com/microsoft/TextWorld) is a sandbox learning environment aimed at training and evaluating reinforcement learning (RL) agents on text-based games.

![Star History Chart](https://api.star-history.com/svg?repos=yingpengma/Awesome-Story-Generation&type=Date)
