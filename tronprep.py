#!/usr/bin/env python3
import argparse
import sys
import os
import csv
import tempfile
import subprocess

class SampleData:
	def __init__(self,sample_name):
		self.sample_name = sample_name

# input data
parser = argparse.ArgumentParser(
	description = 'Simply prepping the fastq files',
	usage = 'TronPrep [options] file_of_trait_fastqs file_of_nontrait_fastqs output_directory')
parser.add_argument('output_directory', help='Output directory')
parser.add_argument('file_of_trait_fastqs', help='File of filenames of each trait isolate')
parser.add_argument('file_of_nontrait_fastqs', help='File of filenames of each nontrait isolate')
options = parser.parse_args()

trait_samples = []
#read in metadata
with open(options.file_of_trait_fastqs) as traitfofn:
    for isolate in traitfofn:
        trait_samples.append(isolate)

#with open(options.file_of_trait_fastqs) as fofnfile:
 #   for samples in fofn:
  #      trait_samples.append( (SampleData(sample))


working_dir = os.getcwd()
trait_fileactual = working_dir+"/trait_filename.fofn"
trait_infile = trait_samples
with open(trait_fileactual, 'w') as trait_outfile:        
    for isolate in trait_infile:
        forward_read = isolate+"_1.fastq.gz"
        reverse_read = isolate+"_2.fastq.gz"
        isolate_foward_read = forward_read
        isolate_reverse_read = reverse_read
        trait_writer = csv.writer(trait_outfile, delimiter=',', lineterminator='\n')
        trait_writer.writerow([isolate_foward_read]+[isolate_reverse_read])
   #row_entry = isolate.foward_read+isolate.reverse_read
  # print(isolate.foward_read+isolate.reverse_read)
