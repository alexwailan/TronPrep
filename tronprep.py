#!/usr/bin/env python3
import argparse
import sys
import os
import csv
import tempfile
import subprocess


# input data
parser = argparse.ArgumentParser(
	description = 'Simply preparing the fastq files',
	usage = 'TronPrep [options] file_of_trait_fastqs file_of_nontrait_fastqs')
parser.add_argument('file_of_trait_fastqs', help='File of filenames of each trait isolate')
parser.add_argument('file_of_nontrait_fastqs', help='File of filenames of each nontrait isolate')
options = parser.parse_args()

working_dir = os.getcwd()
trait_output_file  = working_dir+"/trait_file_of_fastqs.csv"
non_trait_output_file = working_dir+"/nontrait_file_of_fastqs.csv"

trait_infile = options.file_of_trait_fastqs
nontrait_infile = options.file_of_nontrait_fastqs
with open(trait_infile, "r") as inputdata:
    with open(trait_output_file, 'w') as outputfile:        
        for isolate in inputdata:
            isolate_name = isolate.strip()
            isolate_foward_read = isolate_name + "_1.fastq.gz"
            isolate_reverse_read = isolate_name + "_2.fastq.gz"
            trait_writer = csv.writer(outputfile, delimiter=',', lineterminator='\n')
            trait_writer.writerow([str(isolate_foward_read)]+[str(isolate_reverse_read)])

with open(nontrait_infile, "r") as inputdata:
    with open(non_trait_output_file, 'w') as outputfile:        
        for isolate in inputdata:
            isolate_name = isolate.strip()
            isolate_foward_read = isolate_name + "_1.fastq.gz"
            isolate_reverse_read = isolate_name + "_2.fastq.gz"
            trait_writer = csv.writer(outputfile, delimiter=',', lineterminator='\n')
            trait_writer.writerow([str(isolate_foward_read)]+[str(isolate_reverse_read)])