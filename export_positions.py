#! /usr/bin/env python3

import sys
import re

if len(sys.argv) != 5:
	sys.exit('This script exports a part of a selected sequence from a fasta file, delimited by base numbers provided.\n'
	         'Usage: ./export_positions.py <fasta_file> <seq_name (or part of it)> <start_position> <end_position>\n')
Script, Fasta, Seq_name, Start_position, End_position = sys.argv

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
   if Seq_name in entry[0]: # entry[0] <- sequence label
      Fragment_to_export = ''
      for char in entry[1][int(Start_position)-1:int(End_position)]: # entry[1] <- sequence
         Fragment_to_export += char
      print(entry[0], '_%s_to_%s_bp\n' % (Start_position, End_position), Fragment_to_export, '\n', sep = '', end = '', file = sys.stdout)
