#!/bin/bash
# Produces a pdf document with all test cases.
# Should be called from the project root folder.

OUTFILE=test_cases.md
pandoc $OUTFILE --to pdf --number-sections > ${OUTFILE%.*}.pdf
