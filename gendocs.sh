#!/bin/bash
# Requires pandoc installed and pandoc-include panflute filter.
# Produces a pdf document with all test cases.
# Should be called from the project root folder.

OUTFILE=test_cases.md

rm $OUTFILE
for dir in test_cases/*/;
do
    cd $dir
    dir=${dir%*/}        # remove the trailing "/"
    test=${dir##*/}      # remove leading part, giving just the folder name
    echo "Processing $test"
    pandoc $test.md --filter pandoc-include --to markdown >> ../../$OUTFILE
    cd ../../
    echo "" >> $OUTFILE
done

pandoc $OUTFILE --to pdf --number-sections > ${OUTFILE%.*}.pdf
