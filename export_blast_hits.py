#! /usr/bin/env python3

import sys

Exit_message = """\n----- export_blast_hits.py -----
This scripts takes an output of blast search (format -outfmt 6) and produces a list of unique sequences that blast has identified.
Usage:
   export_blast_hits.py blast.result > list_of_sequence_IDs.py
"""


if len(sys.argv) != 2:
   print(Exit_message)
   sys.exit()
	

Script, Blast_result = sys.argv


   ### Reading input count_table as a list of lists. Lists correspond to columns, and indexes to rows.
   ### Row #0 - headings; Column #0 - Unique genotype names; Column #1 - Total counts for given genotype
TABLE = open(Blast_result, 'r')
IDs = []

for row in TABLE:
    ROW = row.split('	')
    #print(ROW)
    
    if ROW[1] not in IDs:
        IDs.append(ROW[1])
            
for ID in IDs:
    print(ID)