#!/bin/bash
# Produces a pdf document with all test cases.
# Should be called from the project root folder.

OUTFILE=test_cases.md
pandoc $OUTFILE --number-sections -o ${OUTFILE%.*}.pdf
