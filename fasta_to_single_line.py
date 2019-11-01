#! /usr/bin/env python3

import sys

if len(sys.argv) != 2:
	sys.exit('This script rewrites all sequences within a multifasta file, potentially spread across multiple lines,\n'
	         'without any EOL characters --- so that they appear written in a single line.\n'
		 'Usage: ./fasta_to_single_line.py <fasta_file> \n')
Script, Fasta = sys.argv

FASTA = open(Fasta, 'r')


Sequence_list = []
Sequence = ''
for line in FASTA:   # Copying the sequence (potentially spread across multiple lines) to a single line
    if line.startswith('>'):
       if Sequence != '':   # Saves the existing Seq_heading and Sequence to a list before overwriting them
          Sequence_list.append([Seq_heading, Sequence])
          Sequence = ''
       Seq_heading = line.strip('\n')
    else:
       Sequence = Sequence + line.strip('\n').upper()

Sequence_list.append([Seq_heading, Sequence]) # Saves the final sequence (Seq_heading and Sequence) to a list
       
FASTA.close()

for entry in Sequence_list:
   print(entry[0], '\n', entry[1], '\n', end = '', sep = '', file = sys.stdout)
