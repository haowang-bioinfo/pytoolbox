# -*- coding: utf-8 -*-
from Bio import SeqIO


def sort_fasta_file(ref_fasta, fasta_to_sort):
    """
    
    """
    sorted_fasta = []

    for elem in ref_fasta:

        # fetch the corresponding SeqRecord
        for value in fasta_to_sort:
            if elem.description in value.description:
                sorted_fasta.append(value)
                break
    return sorted_fasta


