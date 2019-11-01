#!/bin/bash

# 

for input_fasta in $1
do 

tr '\n' '@' < $input_fasta | sed 's/>/#>/g' | tr '#' '\n' > expm_TEMP
grep -Ff $2 expm_TEMP > expm_TEMP2
tr '@' '\n' < expm_TEMP2 | sed '/^$/d'
rm expm_TEMP expm_TEMP2

done
