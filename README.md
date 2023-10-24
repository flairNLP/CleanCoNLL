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
We distribute our CleanCoNLL annotations in columns format. The tokens are masked (`[TOKEN]`) for licence reasons, but you'll find a simple script that allows you to recreate CleanCoNLL from the Reiss version.

Step by step:
* Clone this repository.
* Go to the [Reiss repository](https://github.com/CODAIT/Identifying-Incorrect-Labels-In-CoNLL-2003) and follow their instruction for creating their version.
* Place those 3 files in the `/data/reiss2020_conll` directory, keeping the names as the are (`eng.train`, `eng.testa`, `eng.testb`).
* Inside `/data/CleanCoNLL_annotations` you can find our masked annotation files (`cleanconll_annotations.dev.train`, `cleanconll_annotations.dev`, `cleanconll_annotations.test`).
 * The files inside `/data/CleanCoNLL_linebreak_changes` list some lines where the text base from CleanCoNLL differs from the Reiss version. These are necessary when creating our version from theirs. 
* You simply need to run
  ```
  python scripts/create_corpus.py
  ```
  for combining the three sources and creating the three CleanCoNLL files with text. They will be placed inside `/data/CleanCoNLL_corpus`.
