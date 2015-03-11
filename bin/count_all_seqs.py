#!/usr/bin/env python

import sys
import os
import seq_utils

def count_seqs(path):
        filenames = sorted(os.listdir(path))
        os.chdir(path)

        for filex in filenames:
                input_file=open(filex)
                seq_count = seq_utils.count_seqs(input_file)
                print seq_count, "in", filex

if len(sys.argv) != 2:
        sys.exit("Usage: count_all_seqs.py <filenames>")

print count_seqs(sys.argv[1])
