#!/bin/bash

for filename in $1
do 

tr '\n' '@' < $filename | sed 's/>/#>/g' | tr '#' '\n' | grep $2 | tr '@' '\n' | sed '/^$/d'

done
