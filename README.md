# NLP-Final-Project

CSCI-SHU 376 Natural Language Processing | Spring 2021 | Final Project

By Tinglong Liao (tl2564), Xue Bai (xb347), Alison Yao (yy2564)

"The purpose of the final project is two-fold. First, it will give you the opportunity and incentive to study in-depth a topic that interests you. Second, it will test your ability to use NLP algorithms to solve a problem within this topic. The project definition is purposefully open- ended. The goal is for you to be able to spend time thinking deeply about NLP and how to best apply it in a real-life scenario."

## Dataset

Please check `TableQA` directory.

GitHub Source: https://github.com/ZhuiyiTechnology/TableQA

Paper detailing the dataset: https://arxiv.org/abs/2006.06434

Data is used for a compitition: https://tianchi.aliyun.com/competition/entrance/231716/introduction

## Project Implementation

Please check `NLP_final_paper.pdf`.

All implementation codes are in `code` directory.

### Single-BERT Model:

Variant 1 – SB_multitask: `all_task_7 final.ipynb`

Variant 2 – SB_SELECT: `all_task_only_sel_final.ipynb`

Variant 3 – SB_WHERE: `all_task_only_where_final.ipynb`

### Double Tower Model

Variant 1 – DT_multitask: `double_tower_single_task.ipynb`

Variant 2 – DT_SELECT & Variant 3 – DT_WHERE: `double_tower_multi_task.ipynb`

### Trained models

Baiduyun Link: https://pan.baidu.com/s/12Qj_9CC5PvyXcgz_r_2nWw Password: 4imj

## References

https://github.com/BaeSeulki/NL2LF/blob/master/README.md

### Baseline

Baseline is provided by the data providers: https://github.com/ZhuiyiTechnology/nl2sql_baseline

### Improvement

No.1 Model: https://tianchi.aliyun.com/forum/postDetail?spm=5176.12586969.1002.6.694d1ca2X5AViB&postId=78781

PPT: https://github.com/nudtnlp/tianchi-nl2sql-top1/blob/master/天池NL2SQL冠军方案.pdf

Pretrained BERT Embeddings: https://github.com/ymcui/Chinese-BERT-wwm

No.3 Model: https://github.com/lifloveyou/tianchi_nl2sql

<!-- # Submission: NL2SQL:BERT-based Model For SQL Generation

Tinglong Liao (tl2564), Xue Bai (xb347), Alison Yao (yy2564)

## Note
You can find the dataset and the .bin files in Google Drive folder and the Colab files in the links respectively. We ran many experiments, so we have 5 Colab files in total. Please refer to the paper for detailed explanation.

## Dataset & Pytorch Models
Google Drive: https://drive.google.com/drive/folders/1Xyoc2eNAqOvaxNBrj0O_R60G-nBEp8gN?usp=sharing

### Dataset
Google Drive >>> data >>> TableQA

You can also check the original GitHub here: https://github.com/ZhuiyiTechnology/TableQA

### Pytorch Models
Single-BERT: Google Drive >>> data >>> Single-BERT >>> checkpoints of all sorts

Double Tower: Google Drive >>> data >>> checkpoints of all sorts

## Google Colab

You can run the code in Google Colab notebooks directly.

### Single-BERT Model:
Variant 1 – SB_multitask: https://colab.research.google.com/drive/1v-fhuDpuMG3qZ8CLEbdznvR5rEIbjSYV

Variant 2 – SB_SELECT: https://colab.research.google.com/drive/13YatcSy3SmL-gf7imP1Z5aBTCrS8eoNE

Variant 3 – SB_WHERE: https://colab.research.google.com/drive/19sS7ki1iv8JXPRFND04bC-GL0hWZaGM-

### Double Tower Model
Variant 1 – DT_multitask: https://colab.research.google.com/drive/1_BalGHk_KuiShMcQySA3Wlvf49qUN15s?usp=sharing

Variant 2 – DT_SELECT & Variant 3 – DT_WHERE: https://colab.research.google.com/drive/1l8SXWEhy-WP1L8SJd3uMnp6h9Ur6GDlG?usp=sharing


## Hyperparameters
Please see paper Appendix or Colab file Config.  -->
