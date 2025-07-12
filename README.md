<h1 align="center">Awesome-Story-Generation</h1>

<div align="center">Contributed by <a href="https://yingpengma.github.io/">Yingpeng Ma</a>, <a href="https://mantle2048.github.io/">Yan Ma</a></div>

##

🔥 Recognizing the paradigm shift brought by **Large Language Models**, we now focus exclusively on LLM-related research.

For those interested in previous research before LLM era, an archived version is available in [Old Version](old_version.md) (this archive is **no longer maintained**). 

## Table of Contents

- [Introduction](#introduction)
<!--
- [Related Repository](#related-repository)
-->
- [Papers](#papers)
  - [Overview](#overview)
  - [Plan And Write](#plan-and-write)
  - [Multi Agent](#multi-agent)
  - [Better Storytelling](#better-storytelling)
  - [More Controllable](#more-controllable)
  - [More Personalized](#more-personalized)
  - [Evaluation](#evaluation)
  - [Dataset](#dataset)
- [Public Resources](#public-resources)

## Introduction

This repository collects awesome papers about **Story Generation / Storytelling** in LLM era.

Papers are listed chronologically (most recent first).

**Thank you for the stars!** We're continuously updating with the latest research. Cheers! 🍻

Your contributions matter! Please help keep this list current and accurate by opening issues or PRs for any mistakes or missing papers.

Contact: `mayingpeng33 [AT] gmail [DOT] com`

<!--
## Related Repository
|**[Awesome-LLM-Characters](https://github.com/yingpengma/Awesome-LLM-Characters)**|
|:---:|
-->

## Papers
Eg. `ACL-20XX` **Title** [paper] [code] .. [authors]  [![](https://img.shields.io/badge/citation-count-blue)]()

### Overview
- `ArXiv-2024` **What Makes a Good Story and How Can We Measure It? A Comprehensive Survey of Story Evaluation** [[paper]](https://arxiv.org/abs/2408.14622) [Dingyi Yang, Qin Jin] [![](https://img.shields.io/badge/citation-7-blue)]()
- `CHI-2024` **The Value, Benefits, and Concerns of Generative AI-Powered Assistance in Writing** [[paper]](https://arxiv.org/abs/2403.12004) [Zhuoyan Li, Chen Liang, Jing Peng, Ming Yin] [Mainly about ChatGPT, not including other models] [![](https://img.shields.io/badge/citation-59-blue)]() 
- `ArXiv-2024` **Weaver: Foundation Models for Creative Writing** [[paper]](https://arxiv.org/abs/2401.17268) [Tiannan Wang, Jiamin Chen, Qingrui Jia, Shuai Wang, Ruoyu Fang, ... , Yuchen Eleanor Jiang, Wangchunshu Zhou] [Foundation Models which focus on writing capabilities] [![](https://img.shields.io/badge/citation-20-blue)]() 
- `EMNLP Findings-2023` **Are NLP Models Good at Tracing Thoughts: An Overview of Narrative Understanding** [[paper]](https://arxiv.org/abs/2310.18783) [Lixing Zhu, Runcong Zhao, Lin Gui, Yulan He] [![](https://img.shields.io/badge/citation-5-blue)]()

### Plan And Write
- `NAACL-2025` **Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement** [[paper]](https://arxiv.org/abs/2412.13575) [Qianyue Wang, Jinwu Hu, Zhengping Li, Yufeng Wang, daiyuan li, Yu Hu, Mingkui Tan] [![](https://img.shields.io/badge/citation-6-blue)]()
- `EMNLP-2024` **Collective Critics for Creative Story Generation** [[paper]](https://arxiv.org/abs/2410.02428) [Minwook Bae, Hyounghun Kim] [![](https://img.shields.io/badge/citation-3-blue)]()
- `ACL-2024` **Ex3: Automatic Novel Writing by Extracting, Excelsior and Expanding** [[paper]](https://arxiv.org/abs/2408.08506) [Lei Huang, Jiaming Guo, Guanhua He, Xishan Zhang, Rui Zhang, Shaohui Peng, Shaoli Liu, Tianshi Chen] [![](https://img.shields.io/badge/citation-2-blue)]()
- `ACL Workshop-2025` **Guiding and Diversifying LLM-Based Story Generation via Answer Set Programming** [[paper]](https://arxiv.org/abs/2406.00554) [Phoebe J. Wang, Max Kreminski] [![](https://img.shields.io/badge/citation-6-blue)]()
- `NAACL-2025` **Navigating the Path of Writing: Outline-guided Text Generation with Large Language Models** [[paper]](https://arxiv.org/abs/2404.13919) [Yukyung Lee, Soonwon Ka, Bokyung Son, Pilsung Kang, Jaewook Kang]  [![](https://img.shields.io/badge/citation-6-blue)]()
- `EACL-2024` **Creating Suspenseful Stories: Iterative Planning with Large Language Models** [[paper]](https://arxiv.org/abs/2402.17119) [Kaige Xie, Mark Riedl] [Prompt Engineering] [![](https://img.shields.io/badge/citation-9-blue)]() 
- `ArXiv-2023` **EIPE-text: Evaluation-Guided Iterative Plan Extraction for Long-Form Narrative Text Generation** [[paper]](https://arxiv.org/abs/2310.08185) [Wang You, Wenshan Wu, Yaobo Liang, Shaoguang Mao, Chenfei Wu, Maosong Cao, Yuzhe Cai, Yiduo Guo, Yan Xia, Furu Wei, Nan Duan] [Prompt Engineering] [![](https://img.shields.io/badge/citation-9-blue)]() 

### Multi Agent
- `ArXiv-2025` **A Cognitive Writing Perspective for Constrained Long-Form Text Generation** [[paper]](https://arxiv.org/abs/2502.12568) [Kaiyang Wan, Honglin Mu, Rui Hao, Haoran Luo, Tianle Gu, Xiuying Chen] [![](https://img.shields.io/badge/citation-1-blue)]()
- `ICLR-2025` **Agents' Room: Narrative Generation through Multi-step Collaboration** [[paper]](https://arxiv.org/abs/2410.02603) [Fantine Huot, Reinald Kim Amplayo, Jennimaria Palomaki, Alice Shoshana Jakobovits, Elizabeth Clark, Mirella Lapata] [![](https://img.shields.io/badge/citation-16-blue)]()
- `ACL-2024` **IBSEN: Director-Actor Agent Collaboration for Controllable and Interactive Drama Script Generation** [[paper]](https://arxiv.org/abs/2407.01093) [Senyu Han, Lu Chen, Li-Min Lin, Zhengshan Xu, Kai Yu] [![](https://img.shields.io/badge/citation-16-blue)]()
- `EMNLP Findings-2024` **HoLLMwood: Unleashing the Creativity of Large Language Models in Screenwriting via Role Playing** [[paper]](https://arxiv.org/abs/2406.11683) [Jing Chen, Xinyu Zhu, Cheng Yang, Chufan Shi, Yadong Xi, Yuxiang Zhang, Junjie Wang, Jiashu Pu, Rongsheng Zhang, Yujiu Yang, Tian Feng] [![](https://img.shields.io/badge/citation-9-blue)]()
- `FDG-2024` **StoryVerse: Towards Co-authoring Dynamic Plot with LLM-based Character Simulation via Narrative Planning** [[paper]](https://arxiv.org/abs/2405.13042) [Yi Wang, Qian Zhou, David Ledo] [virtual characters] [![](https://img.shields.io/badge/citation-14-blue)]() 
- `IJCAI-2024` **AutoAgents: A Framework for Automatic Agent Generation** [[paper]](https://arxiv.org/abs/2309.17288) [Guangyao Chen, Siwei Dong, Yu Shu, Ge Zhang, Jaward Sesay, Börje F. Karlsson, Jie Fu, Yemin Shi] [Prompt Engineering] [![](https://img.shields.io/badge/citation-129-blue)]() 

### Better Storytelling
- `ArXiv-2025` **Finding Flawed Fictions: Evaluating Complex Reasoning in Language Models via Plot Hole Detection** [[paper]](https://arxiv.org/abs/2504.11900) [Kabir Ahuja, Melanie Sclar, Yulia Tsvetkov] [![](https://img.shields.io/badge/citation-4-blue)]()
- `ArXiv-2025` **Learning to Reason for Long-Form Story Generation** [[paper]](https://arxiv.org/abs/2503.22828) [Alexander Gurung, Mirella Lapata] [![](https://img.shields.io/badge/citation-3-blue)]()
- `ArXiv-2024` **MLD-EA: Check and Complete Narrative Coherence by Introducing Emotions and Actions** [[paper]](https://arxiv.org/abs/2412.02897) [Jinming Zhang, Yunfei Long] [![](https://img.shields.io/badge/citation-1-blue)]()
- `EMNLP Findings-2024` **SWAG: Storytelling With Action Guidance** [[paper]](https://arxiv.org/abs/2402.03483) [Zeeshan Patel, Karim El-Refai, Jonathan Pei, Tianle Li] [Reinforcement learning / SFT] [![](https://img.shields.io/badge/citation-4-blue)]() 
- `EMNLP Findings-2023` **Improving Pacing in Long-Form Story Planning** [[paper]](https://arxiv.org/abs/2311.04459) [Yichen Wang, Kevin Yang, Xiaoming Liu, Dan Klein] [Story pacing] [![](https://img.shields.io/badge/citation-19-blue)]() 
- `ArXiv-2023` **End-to-End Story Plot Generator** [[paper]](https://arxiv.org/abs/2310.08796) [Hanlin Zhu, Andrew Cohen, Danqing Wang, Kevin Yang, Xiaomeng Yang, Jiantao Jiao, Yuandong Tian] [SFT] [![](https://img.shields.io/badge/citation-5-blue)]() 
- `EMNLP Findings-2023` **GROVE: A Retrieval-augmented Complex Story Generation Framework with A Forest of Evidence** [[paper]](https://arxiv.org/abs/2310.05388) [Zhihua Wen, Zhiliang Tian, Wei Wu, Yuxin Yang, Yanqi Shi, Zhen Huang, Dongsheng Li] [RAG] [![](https://img.shields.io/badge/citation-14-blue)]() 

### More Controllable
- `ArXiv-2025` **SCORE: Story Coherence and Retrieval Enhancement for AI Narratives** [[paper]](https://arxiv.org/abs/2503.23512) [Qiang Yi, Yangfan He, Jianhui Wang, Xinyuan Song, Shiyao Qian, Miao Zhang, Li Sun, Tianyu Shi] [![](https://img.shields.io/badge/citation-17-blue)]()
- `ArXiv-2024` **Crafting Narrative Closures: Zero-Shot Learning with SSM Mamba for Short Story Ending Generation** [[paper]](https://arxiv.org/abs/2410.10848) [Divyam Sharma, Divya Santhanam] [![](https://img.shields.io/badge/citation-0-blue)]()
- `ACL-2024` **MoPS: Modular Story Premise Synthesis for Open-Ended Automatic Story Generation** [[paper]](https://arxiv.org/abs/2406.05690)  [[code]](https://github.com/GAIR-NLP/MoPS) [Yan Ma, Yu Qiao, Pengfei Liu] [![](https://img.shields.io/badge/citation-6-blue)]()
- `ArXiv-2024` **Multigenre AI-powered Story Composition** [[paper]](https://arxiv.org/abs/2405.06685v2) [Edirlei Soares de Lima, Margot M. E. Neggers, Antonio L. Furtado] [![](https://img.shields.io/badge/citation-1-blue)]()
- `NAACL-2024` **Returning to the Start: Generating Narratives with Related Endpoints** [[paper]](https://arxiv.org/abs/2404.00829) [[code]](https://github.com/adbrei/RENarGen) [Anneliese Brei, Chao Zhao, Snigdha Chaturvedi] [SFT / Prompt Engineering] [![](https://img.shields.io/badge/citation-1-blue)]() 
- `COLM-2024` **With Greater Text Comes Greater Necessity: Inference-Time Training Helps Long Text Generation** [[paper]](https://arxiv.org/abs/2401.11504) [Y. Wang, D. Ma, D. Cai] [LoRA] [![](https://img.shields.io/badge/citation-20-blue)]()
- `ICLR-2024` **RLCD: Reinforcement Learning from Contrast Distillation for Language Model Alignment** [[paper]](https://arxiv.org/abs/2307.12950) [Kevin Yang, Dan Klein, Asli Celikyilmaz, Nanyun Peng, Yuandong Tian] [Reinforcement learning] [![](https://img.shields.io/badge/citation-24-blue)]() 
- `ArXiv-2023` **RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text** [[paper]](https://arxiv.org/abs/2305.13304) [[code]](https://github.com/aiwaves-cn/RecurrentGPT) [Wangchunshu Zhou, Yuchen Eleanor Jiang, Peng Cui, Tiannan Wang, Zhenxin Xiao, Yifan Hou, Ryan Cotterell, Mrinmaya Sachan] [Prompt Engineering] [![](https://img.shields.io/badge/citation-64-blue)]() 

### More Personalized
- `ArXiv-2025` **STORY2GAME: Generating (Almost) Everything in an Interactive Fiction Game** [[paper]](https://arxiv.org/abs/2505.03547) [Eric Zhou, Shreyas Basavatia, Moontashir Siam, Zexin Chen, Mark O. Riedl] [Game] [![](https://img.shields.io/badge/citation-0-blue)]()
- `ICLR-2025` **R^2: A LLM BASED NOVEL-TO-SCREENPLAY GENERATION FRAMEWORK WITH CAUSAL PLOT GRAPHS** [[paper]](https://arxiv.org/pdf/2503.15655) [Zefeng Lin, Yi Xiao, Zhiqiang Mo, Qifan Zhang, Jie Wang, Jiayang Chen, Jiajing Zhang, Hui Zhang, Zhengyi Liu, Xianyong Fang, Xiaohua Xu] [![](https://img.shields.io/badge/citation-0-blue)]()
- `ArXiv-2025` **Towards Enhanced Immersion and Agency for LLM-based Interactive Drama** [[paper]](https://arxiv.org/abs/2502.17878) [Hongqiu Wu, Weiqi Wu, Tianyang Xu, Jiameng Zhang, Hai Zhao] [![](https://img.shields.io/badge/citation-0-blue)]()
- `ArXiv-2025` **Pastiche Novel Generation Creating: Fan Fiction You Love in Your Favorite Author's Style** [[paper]](https://arxiv.org/abs/2502.15616) [Xueran Han, Yuhan Liu, Mingzhe Li, Wei Liu, Sen Hu, Rui Yan, Zhiqiang Xu, Xiuying Chen] [Style] [![](https://img.shields.io/badge/citation-0-blue)]()
- `ArXiv-2025` **Whose story is it? Personalizing story generation by inferring author styles** [[paper]](https://arxiv.org/abs/2502.13028) [Nischal Ashok Kumar, Chau Minh Pham, Mohit Iyyer, Andrew Lan] [![](https://img.shields.io/badge/citation-1-blue)]()
- `EMNLP-2024` **MirrorStories: Reflecting Diversity through Personalized Narrative Generation with Large Language Models** [[paper]](https://arxiv.org/abs/2409.13935) [Sarfaroz Yunusov, Hamza Sidat, Ali Emami] [![](https://img.shields.io/badge/citation-0-blue)]()
- `ArXiv-2024` **CAT-LLM: Prompting Large Language Models with Text Style Definition for Chinese Article-style Transfer** [[paper]](https://arxiv.org/abs/2401.05707) [Zhen Tao, Dinghao Xi, Zhiyu Li, Liumin Tang, Wei Xu] [Style] [![](https://img.shields.io/badge/citation-13-blue)]() 
- `ArXiv-2023` **Learning to Generate Text in Arbitrary Writing Styles** [[paper]](https://arxiv.org/abs/2312.17242) [Aleem Khan, Andrew Wang, Sophia Hager, Nicholas Andrews] [Style] [![](https://img.shields.io/badge/citation-6-blue)]() 

### Evaluation
- `ArXiv-2025` **CoKe: Customizable Fine-Grained Story Evaluation via Chain-of-Keyword Rationalization** [[paper]](https://arxiv.org/abs/2503.17136) [Brihi Joshi, Sriram Venkatapathy, Mohit Bansal, Nanyun Peng, Haw-Shiuan Chang] [![](https://img.shields.io/badge/citation-0-blue)]()
- `ArXiv-2025` **LongEval: A Comprehensive Analysis of Long-Text Generation Through a Plan-based Paradigm** [[paper]](https://arxiv.org/abs/2502.19103) [Siwei Wu, Yizhi Li, Xingwei Qu, Rishi Ravikumar, Yucheng Li, Tyler Loakman, Shanghaoran Quan, Xiaoyong Wei, Riza Batista-Navarro, Chenghua Lin] [![](https://img.shields.io/badge/citation-4-blue)]()
- `ArXiv-2025` **Echoes in AI: Quantifying Lack of Plot Diversity in LLM Outputs** [[paper]](https://arxiv.org/abs/2501.00273) [Weijia Xu, Nebojsa Jojic, Sudha Rao, Chris Brockett, Bill Dolan] [![](https://img.shields.io/badge/citation-7-blue)]()
- `ArXiv-2024` **Evaluating Creative Short Story Generation in Humans and Large Language Models** [[paper]](https://arxiv.org/abs/2411.02316) [Mete Ismayilzada, Claire Stevenson, Lonneke van der Plas] [![](https://img.shields.io/badge/citation-5-blue)]()
- `ArXiv-2024` **CS4: Measuring the Creativity of Large Language Models Automatically by Controlling the Number of Story-Writing Constraints** [[paper]](https://arxiv.org/abs/2410.04197) [Anirudh Atmakuru, Jatin Nainani, Rohith Siddhartha Reddy Bheemreddy, Anirudh Lakkaraju, Zonghai Yao, Hamed Zamani, Haw-Shiuan Chang] [![](https://img.shields.io/badge/citation-3-blue)]()
- `COLING-2025` **Small Language Models can Outperform Humans in Short Creative Writing: A Study Comparing SLMs with Humans and LLMs** [[paper]](https://arxiv.org/abs/2409.11547) [Guillermo Marco, Luz Rello, Julio Gonzalo] [![](https://img.shields.io/badge/citation-7-blue)]()
- `NAACL-2025` **FACTTRACK: Time-Aware World State Tracking in Story Outlines** [[paper]](https://arxiv.org/abs/2407.16347) [Zhiheng Lyu, Kevin Yang, Lingpeng Kong, Daniel Klein] [![](https://img.shields.io/badge/citation-0-blue)]()
- `EMNLP-2024` **Are Large Language Models Capable of Generating Human-Level Narratives?** [[paper]](https://arxiv.org/abs/2407.13248) [Yufei Tian, Tenghao Huang, Miri Liu, Derek Jiang, Alexander Spangher, Muhao Chen, Jonathan May, Nanyun Peng] [![](https://img.shields.io/badge/citation-33-blue)]()
- `EMNLP-2024` **STORYSUMM: Evaluating Faithfulness in Story Summarization** [[paper]](https://arxiv.org/abs/2407.06501) [Melanie Subbiah, Faisal Ladhak, Akankshya Mishra, Griffin Adams, Lydia B. Chilton, Kathleen McKeown] [![](https://img.shields.io/badge/citation-4-blue)]()
- `ArXiv-2024` **Pron vs Prompt: Can Large Language Models already Challenge a World-Class Fiction Author at Creative Text Writing?** [[paper]](https://arxiv.org/abs/2407.01119) [Guillermo Marco, Julio Gonzalo, Ramón del Castillo, María Teresa Mateo Girona] [![](https://img.shields.io/badge/citation-17-blue)]()
- `EMNLP-2024` **Measuring Psychological Depth in Language Models** [[paper]](https://arxiv.org/abs/2406.12680) [Fabrice Harel-Canada, Hanyu Zhou, Sreya Muppalla, Zeynep Yildiz, Miryung Kim, Amit Sahai, Nanyun Peng] [![](https://img.shields.io/badge/citation-3-blue)]()
- `TACL-2024` **Do Language Models Enjoy Their Own Stories? Prompting Large Language Models for Automatic Story Evaluation** [[paper]](https://arxiv.org/abs/2405.13769) [Cyril Chhun, Fabian M. Suchanek, Chloé Clavel] [![](https://img.shields.io/badge/citation-18-blue)]()
- `TACL-2024` **Reading Subtext: Evaluating Large Language Models on Short Story Summarization with Writers** [[paper]](https://arxiv.org/abs/2403.01061) [Melanie Subbiah, Sean Zhang, Lydia B. Chilton, Kathleen McKeown] [![](https://img.shields.io/badge/citation-15-blue)]()
- `EMNLP Findings-2023` **A Confederacy of Models: a Comprehensive Evaluation of LLMs on Creative Writing** [[paper]](https://arxiv.org/abs/2310.08433) [Carlos Gómez-Rodríguez, Paul Williams] [![](https://img.shields.io/badge/citation-83-blue)]()
- `EMNLP-2024` **Learning Personalized Alignment for Evaluating Open-ended Text Generation** [[paper]](https://arxiv.org/abs/2310.03304) [Danqing Wang, Kevin Yang, Hanlin Zhu, Xiaomeng Yang, Andrew Cohen, Lei Li, Yuandong Tian] [![](https://img.shields.io/badge/citation-11-blue)]()
- `ICLR-2024` **BooookScore: A systematic exploration of book-length summarization in the era of LLMs**[[paper]](https://arxiv.org/abs/2310.00785)[Yapei Chang, Kyle Lo, Tanya Goyal, Mohit Iyyer] [![](https://img.shields.io/badge/citation-117-blue)]()
- `TMLR-2024` **TIGERScore: Towards Building Explainable Metric for All Text Generation Tasks**[[paper]](https://arxiv.org/abs/2310.00752)[Dongfu Jiang, Yishan Li, Ge Zhang, Wenhao Huang, Bill Yuchen Lin, Wenhu Chen] [![](https://img.shields.io/badge/citation-69-blue)]()
- `CHI-2023` **Art or Artifice? Large Language Models and the False Promise of Creativity** [[paper]](https://arxiv.org/abs/2309.14556) [Tuhin Chakrabarty, Philippe Laban, Divyansh Agarwal, Smaranda Muresan, Chien-Sheng Wu]   [![](https://img.shields.io/badge/citation-136-blue)]()
- `ACL-2023` **HAUSER: Towards Holistic and Automatic Evaluation of Simile Generation** [[paper]](https://arxiv.org/abs/2306.07554) [Qianyu He, Yikai Zhang, Jiaqing Liang, Yuncheng Huang, Yanghua Xiao, Yunwen Chen] [![](https://img.shields.io/badge/citation-6-blue)]()
- `ACL-2023` **Can Large Language Models Be an Alternative to Human Evaluations?** [[paper]](https://arxiv.org/abs/2305.01937) [Cheng-Han Chiang, Hung-yi Lee] [![](https://img.shields.io/badge/citation-634-blue)]()
- `EMNLP Findings-2023` **DeltaScore: Evaluating Story Generation with Differentiating Perturbations** [[paper]](https://arxiv.org/abs/2303.08991) [Zhuohan Xie, Miao Li, Trevor Cohn, Jey Han Lau] [![](https://img.shields.io/badge/citation-4-blue)]()
- `EMNLP-2022` **StoryER: Automatic Story Evaluation via Ranking, Rating and Reasoning** [[paper]](https://arxiv.org/abs/2210.08459) [Hong Chen, Duc Minh Vo, Hiroya Takamura, Yusuke Miyao, Hideki Nakayama] [![](https://img.shields.io/badge/citation-20-blue)]()
- `COLING-2022` **Of Human Criteria and Automatic Metrics: A Benchmark of the Evaluation of Story Generation** [[paper]](https://arxiv.org/abs/2208.11646)  [Cyril Chhun, Pierre Colombo, Chloé Clavel, Fabian M. Suchanek] [![](https://img.shields.io/badge/citation-55-blue)]()
- `TACL-2022` **LOT: A story-centric benchmark for evaluating Chinese long text understanding and generation** [[paper]](https://arxiv.org/abs/2108.12960) [Jian Guan, Zhuoer Feng, Yamei Chen, Ruilin He, Xiaoxi Mao, Changjie Fan, Minlie Huang] [![](https://img.shields.io/badge/citation-33-blue)]()
- `ACL-2021` **Openmeva: A benchmark for evaluating open-ended story generation metrics** [[paper]](https://arxiv.org/abs/2105.08920) [Jian Guan, Zhexin Zhang, Zhuoer Feng, Zitao Liu, Wenbiao Ding, Xiaoxi Mao, Changjie Fan, Minlie Huang] [![](https://img.shields.io/badge/citation-61-blue)]()
- `EMNLP-2020` **Union: An unreferenced metric for evaluating open-ended story generation** [[paper]](https://arxiv.org/abs/2009.07602) [[code]](https://github.com/thu-coai/UNION) [Jian Guan, Minlie Huang] [![](https://img.shields.io/badge/citation-70-blue)]()


### Dataset
- `EMNLP Findings-2024` **BookWorm: A Dataset for Character Description and Analysis** [[paper]](https://arxiv.org/abs/2410.10372) [Argyrios Papoudakis, Mirella Lapata, Frank Keller] [![](https://img.shields.io/badge/citation-2-blue)]()
- `EMNLP Workshop-2025` **The GPT-WritingPrompts Dataset: A Comparative Analysis of Character Portrayal in Short Stories** [[paper]](https://arxiv.org/abs/2406.16767) [Xi Yu Huang, Krishnapriya Vishnubhotla, Frank Rudzicz] [![](https://img.shields.io/badge/citation-3-blue)]()
- `NAACL Findings-2025` **CollabStory: Multi-LLM Collaborative Story Generation and Authorship Analysis** [[paper]](https://arxiv.org/abs/2406.12665) [Saranya Venkatraman, Nafis Irtiza Tripto, Dongwon Lee]  [![](https://img.shields.io/badge/citation-14-blue)]()
- `ACL Findings-2024` **Large Language Models Fall Short: Understanding Complex Relationships in Detective Narratives** [[paper]](https://arxiv.org/abs/2402.11051) [Runcong Zhao, Qinglin Zhu, Hainiu Xu, Jiazheng Li, Yuxiang Zhou, Yulan He, Lin Gui] [![](https://img.shields.io/badge/citation-13-blue)]()
- `LREC-COLING-2024` **CLAUSE-ATLAS: A Corpus of Narrative Information to Scale up Computational Literary Analysis** [[paper]](https://aclanthology.org/2024.lrec-main.292/) [Enrica Troiano, Piek T.J.M. Vossen] [![](https://img.shields.io/badge/citation-0-blue)]()
- `LREC-COLING-2024` **Reflections & Resonance: Two-Agent Partnership for Advancing LLM-based Story Annotation** [[paper]](https://aclanthology.org/2024.lrec-main.1206/) [Yuetian Chen, Mei Si]  [![](https://img.shields.io/badge/citation-1-blue)]()
- `LREC-COLING-2024` **CMDAG: A Chinese Metaphor Dataset with Annotated Grounds as CoT for Boosting Metaphor Generation** [[paper]](https://arxiv.org/abs/2402.13145) [Yujie Shao, Xinrong Yao, Xingwei Qu, Chenghua Lin, Shi Wang, Stephen W. Huang, Ge Zhang, Jie Fu]  [![](https://img.shields.io/badge/citation-6-blue)]()
- `ArXiv-2023` **STONYBOOK: A System and Resource for Large-Scale Analysis of Novels** [[paper]](https://arxiv.org/abs/2311.03614) [Charuta Pethe, Allen Kim, Rajesh Prabhakar, Tanzir Pial, Steven Skiena] [![](https://img.shields.io/badge/citation-1-blue)]()
- `ACL-2023` **StoryWars: A Dataset and Instruction Tuning Baselines for Collaborative Story Understanding and Generation** [[paper]](https://arxiv.org/abs/2305.08152) [Yulun Du, Lydia Chilton] [![](https://img.shields.io/badge/citation-8-blue)]()
- `NAACL-2022` **A corpus for understanding and generating moral stories** [[paper]](https://arxiv.org/abs/2204.09438) [Jian Guan, Ziqi Liu, Minlie Huang] [![](https://img.shields.io/badge/citation-10-blue)]()
- `EVAL4NLP-2021` **StoryDB: Broad Multi-language Narrative Dataset** [[paper]](https://arxiv.org/abs/2109.14396) [Alexey Tikhonov, Igor Samenko, Ivan P. Yamshchikov] [![](https://img.shields.io/badge/citation-5-blue)]()
- `ACL-2022` **SummScreen: A Dataset for Abstractive Screenplay Summarization** [[paper]](https://arxiv.org/abs/2104.07091) [[data]](https://github.com/mingdachen/SummScreen) [Mingda Chen, Zewei Chu, Sam Wiseman, Kevin Gimpel] [![](https://img.shields.io/badge/citation-96-blue)]() 
- `ArXiv-2021` **TVStoryGen: A Dataset for Generating Stories with Character Descriptions** [[paper]](https://arxiv.org/abs/2109.08833) [Mingda Chen, Kevin Gimpel] [![](https://img.shields.io/badge/citation-5-blue)]() 
- `EMNLP-2020` **STORIUM: A Dataset and Evaluation Platform for Machine-in-the-Loop Story Generation** [[paper]](https://arxiv.org/abs/2010.01717) [Nader Akoury, Shufan Wang, Josh Whiting, Stephen Hood, Nanyun Peng, Mohit Iyyer] [![](https://img.shields.io/badge/citation-88-blue)]()
- `NAACL-2016` **A Corpus and Cloze Evaluation for Deeper Understanding of Commonsense Stories** [[paper]](https://arxiv.org/abs/1604.01696) [Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong He, Devi Parikh, Dhruv Batra, Lucy Vanderwende, Pushmeet Kohli, James Allen] [![](https://img.shields.io/badge/citation-713-blue)]()


## Public Resources
- [Understanding AI for Stories](https://isamu-website.medium.com/understanding-ai-for-stories-d0c1cd7b7bdc) serves as a survey blog that delves into the application of AI in the realm of story generation, shedding light on its potential as well as the challenges that it encounters.
- [ROC Stories](https://cs.rochester.edu/nlp/rocstories/) is a compilation of 100,000 five-sentence stories and 3,742 Story Cloze Test stories, capturing a rich array of causal and temporal commonsense connections between everyday events, making it suitable for story generation tasks.
- [CommonGen](https://inklab.usc.edu/CommonGen/) was developed by combining crowdsourced and existing caption corpora, containing 79k commonsense descriptions across 35k distinct concept-sets.
- [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) offers access to a dataset containing movie plot summaries and related metadata.
- [Scifi TV Show Plot Summaries & Events](https://huggingface.co/datasets/lara-martin/Scifi_TV_Shows) is a collection of plot synopses for long-running (80+ episodes) science fiction TV shows, sourced from Fandom.com wikis.

![Star History Chart](https://api.star-history.com/svg?repos=yingpengma/Awesome-Story-Generation&type=Date)
