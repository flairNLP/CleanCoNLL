# CleanCoNLL: A Nearly Noise-Free Named Entity Recognition Dataset

We semi-automatically corrected annotation errors in the classic CoNLL-03 dataset for Named Entity Recognition (NER). Get our corpus **CleanCoNLL** with the help of this repository!

<img src="data/CleanCoNLL_example_sentence.jpg" width="700">


## About CleanCoNLL
For details on the approach and evaluation, have a look at our EMNLP 2023 paper:
[link to paper]

In short: We leveraged the Wikipedia links from the [AIDA CoNLL Yago dataset](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) for assigning NER labels for each mention in a hybrid (automatically as well as manual) relabeling approach. Furthermore, we performed several rounds of cross-checking for correcting remaining errors and resolving inconsistencies.
Overall, we updated 7\% of labels from the original CoNLL-03.

We keep the original tagging scheme with 4 types (PER, LOC, ORG, MISC). We add the NEL (Named Entity Linking) annotations, i.e. Wikipedia links to our annotations.

As source text base, we use the corrected corpus version by Reiss et al. (2020) ([paper](https://aclanthology.org/2020.conll-1.16/), [repo](https://github.com/CODAIT/Identifying-Incorrect-Labels-In-CoNLL-2003)), as they not only already modify some of the label errors, but also correct some problems with token, sentence and mention splitting. 

## How to get CleanCoNLL?
We distribute our CleanCoNLL annotations in columns format. The tokens are masked (`[TOKEN]`) for licence reasons, but you'll find a simple shell script that allows you to recreate CleanCoNLL with the help of the original CoNLL-03.

Step by step:
* Clone this repository.
* Inside `/data/cleanconll_annotations` you can find our masked annotation files (`cleanconll_annotations.dev.train`, `cleanconll_annotations.dev`, `cleanconll_annotations.test`).
* Inside `/data/patch_files` you find pach files that represent the updates in the text base between the original CoNLL-03 and CleanCoNLL. This is needed for merging our annotations to the original corpus!
* You simply need to run
  ```
  bash create_cleanconll_from_conll03.sh
  ```
  which will:
  * download the original CoNLL-03 corpus
  * apply the patch files to the original CoNLL-03 for getting the text base right before merging our annotations
  * create the three CleanCoNLL files with text and annotations. They will be placed inside `/data/cleanconll`.

  ## Dataset Columns
  The three files will look like this: Column format with the following columns, the last 3 with BIO tagging scheme:
  
  `Token   POS   Wikipedia   NER (CleanCoNLL*)   NER (CleanCoNLL)`
  
  (CleanCoNLL* is the CleanCoNLL version before Phase 3, i.e. before reverting the adjectival affiliations back to MISC, see paper for details.)
  
  ```
  -DOCSTART-	-X-	O	O	O
  
  SOCCER	NN	O	O	O
  -	:	O	O	O
  JAPAN	NNP	B-Japan_national_football_team	B-ORG	B-ORG
  GET	VB	O	O	O
  LUCKY	NNP	O	O	O
  WIN	NNP	O	O	O
  ,	,	O	O	O
  CHINA	NNP	B-China_national_football_team	B-ORG	B-ORG
  IN	IN	O	O	O
  SURPRISE	DT	O	O	O
  DEFEAT	NN	O	O	O
  .	.	O	O	O
  ```


  
