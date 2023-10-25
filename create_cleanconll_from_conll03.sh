#!/bin/sh

URL="https://data.deepai.org/conll2003.zip"
CONLL03_DIR="data/conll03/"
PATCH_DIR="data/patch_files"

if [ ! -d "$CONLL03_DIR" ] || [ -z "$(ls -A "$CONLL03_DIR")" ]; then
	echo "Downloading the original CoNLL-03 from $URL into $CONLL03_DIR ..."
	mkdir -p "$CONLL03_DIR"
	wget -P "$CONLL03_DIR" "$URL"
	unzip "$CONLL03_DIR/$(basename $URL)" -d "$CONLL03_DIR"
else
	echo "$CONLL03_DIR already exists and has content, so not downloading from $URL"
fi

echo "Now applying the patch files to the original CoNLL tokens to get the modified CleanCoNLL tokens..."

TOKENS_DIR="data/tokens_updated"
mkdir -p "$TOKENS_DIR"

awk '{print $1}' "$CONLL03_DIR/train.txt" > "$CONLL03_DIR/train_tokens.txt"
awk '{print $1}' "$CONLL03_DIR/valid.txt" > "$CONLL03_DIR/valid_tokens.txt"
awk '{print $1}' "$CONLL03_DIR/test.txt" > "$CONLL03_DIR/test_tokens.txt"

patch "$CONLL03_DIR/train_tokens.txt" "$PATCH_DIR/train_tokens.patch" -o "$TOKENS_DIR/train_tokens_updated.txt"
patch "$CONLL03_DIR/valid_tokens.txt" "$PATCH_DIR/dev_tokens.patch" -o "$TOKENS_DIR/dev_tokens_updated.txt"
patch "$CONLL03_DIR/test_tokens.txt" "$PATCH_DIR/test_tokens.patch" -o "$TOKENS_DIR/test_tokens_updated.txt"

echo "Now merging the updated token files with the CleanCoNLL annotations:"
CLEANCONLL_ANNOTATIONS_DIR="data/cleanconll_annotations/"
CLEANCONLL_DIR="data/cleanconll/"
mkdir -p "$CLEANCONLL_DIR"

cut -f 2- "$CLEANCONLL_ANNOTATIONS_DIR/cleanconll.train" | paste "$TOKENS_DIR/train_tokens_updated.txt" - | sed 's/^\t$//' > "$CLEANCONLL_DIR/cleanconll.train"
cut -f 2- "$CLEANCONLL_ANNOTATIONS_DIR/cleanconll.dev" | paste "$TOKENS_DIR/dev_tokens_updated.txt" - | sed 's/^\t$//' > "$CLEANCONLL_DIR/cleanconll.dev"
cut -f 2- "$CLEANCONLL_ANNOTATIONS_DIR/cleanconll.test" | paste "$TOKENS_DIR/test_tokens_updated.txt" - | sed 's/^\t$//' > "$CLEANCONLL_DIR/cleanconll.test"

echo "Done!"
