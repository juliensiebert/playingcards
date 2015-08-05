#!/bin/sh
python ./src/generate_tex.py --input=./dat/phys_const.csv --outdir=./tex/;
for f in $(ls ./tex/*.tex);
do
  pdflatex -output-directory=./tex $f;
done
mv ./tex/*.pdf ./pdf/;
