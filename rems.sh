#!/bin/bash

for filename in $1
do 

tr '\n' '@' < $filename | sed 's/>/#>/g' | tr '#' '\n' | grep -v $2 | tr '@' '\n' | sed '/^$/d'

done
