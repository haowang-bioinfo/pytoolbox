# -*- coding: utf-8 -*-
import requests as r
from Bio import SeqIO
from io import StringIO


def get_uniprot_seq(uniprot_id):
    '''
    Download UniProt protein sequence and retrun as a SeqRecord object
    '''
    uniprotUrl = "http://www.uniprot.org/uniprot/"
    response = r.post(uniprotUrl+uniprot_id+".fasta")
    # TO DO: check response
    Seq = StringIO(''.join(response.text))
    return list(SeqIO.parse(Seq, 'fasta'))


def sort_fasta_file(ref_fasta, fasta_to_sort):
    '''
    Sort an input fasta in SeqRecord object based on a reference fasta
    :param ref_fasta: a reference list of fasta
    :param fasta_to_sort: a list of fasta to be sorted
    '''
    sorted_fasta = []

    for elem in ref_fasta:

        # fetch the corresponding SeqRecord
        for value in fasta_to_sort:
            if elem.description in value.description:
                sorted_fasta.append(value)
                break
    return sorted_fasta


