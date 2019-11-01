#!/bin/bash

for filename in $1
do 

tr '\n' '@' < $filename | sed 's/>/#>/g' | tr '#' '\n' | grep -f $2 -v | tr '@' '\n' | sed '/^$/d'

done
