# CoNLL-A

Repository for creating our corrected version of the CoNLL03 dataset.
We made use of the Wikipedia links from the [AIDA CoNLL Yago dataset](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/ambiverse-nlu/aida/downloads) for (re-)assigning NER labels for each mention.
For label assignment we applied a hybrid approach with both automatically derived (using Wikidata info) and - in more difficult cases - manual decisions from two annotators.

We keep the original tagging scheme with 4 types (PER, LOC, ORG, MISC), however modified some usage principles (e. g. assiginig ORG for sports teams identified by country names).

As text base, we use the corrected corpus version by Reiss et al. 2020 ([paper](https://aclanthology.org/2020.conll-1.16/), [repo](https://github.com/CODAIT/Identifying-Incorrect-Labels-In-CoNLL-2003)), who in their work not only modified label errors but also corrected some problems with sentence/span/mention splitting. 

## Method overview

TODO

## How to use the repository

We distribute our annotations in CoNLL format where the tokens themselfs are masked (`[TOKEN]`), along with a script to recreate our corpus from the Reiss version.
So:
* Clone this repository.
* Go to the Reiss repo and follow their instruction for creating their version.
* Place those 3 files in the `/data/reiss2020_conll` directory, keeping the names as the are (`eng.train`, `eng.testa`, `eng.testb`).
* Our annotations can be found inside `/data/ruecker2023_annotations`.
* Executing the script `/scripts/create_corpus.py` (`python create_corpus.py`) will create 3 files (`clean_conll.{train|dev|text`) and place them into `/data/corpus/`.

