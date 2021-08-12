# -*- coding: utf-8 -*-
import sys
import requests as r
from Bio import SeqIO
from io import StringIO


def get_fasta_header(input_fasta):
    '''
    extract header lines from an input fasta in SeqRecord object
    '''
    header_list = []
    for elem in input_fasta:
        header_list.append(elem.description)
    return header_list


def get_uniprot_seq(uniprot_id):
    '''
    Download UniProt protein sequence and retrun as a SeqRecord object
    '''
    uniprotUrl = "http://www.uniprot.org/uniprot/"
    response = r.post(uniprotUrl+uniprot_id+".fasta")
    # TO DO: check response
    Seq = StringIO(''.join(response.text))
    return list(SeqIO.parse(Seq, 'fasta'))


def sort_fasta_file(ref_fasta, fasta_to_sort, use_id=True):
    '''
    Sort an input fasta in SeqRecord object based on a reference fasta
    :param ref_fasta: a reference list of fasta
    :param fasta_to_sort: a list of fasta to be sorted
    :param use_id: True, sort by id; False, sort by description 
    '''
    if not (type(ref_fasta) is list and type(fasta_to_sort) is list):
        sys.exit("Input fasta should be in list type.")

    sorted_fasta = []  # initial return value
    for elem in ref_fasta:

        # fetch the corresponding SeqRecord
        for value in fasta_to_sort:
            if use_id and elem.id == value.id:
                sorted_fasta.append(value)
                break
            elif not use_id and elem.description in value.description:
                sorted_fasta.append(value)
                break
        
        # To do: check consistency between ref and sorted
    return sorted_fasta


def filter_fasta_seqs(input_fasta, chars_to_exclude=['N']):
    '''
    Filter input fasta sequences by removing the ones containing specific bases
    or residues
    :param input_fasta: fasta sequences as a list of SeqRecord object
    :param char_to_exclude: a list of individual characters to be excluded
    '''
    chars_in_set = set([x.lower() for x in chars_to_exclude])
    output_fasta = []
    for elem in input_fasta:
        # Check whether sequence contains ANY of the items in set
        if 1 not in [c in elem.seq.lower() for c in chars_in_set]:
            output_fasta.append(elem)
    return output_fasta


def remove_desc(input_fasta):
    '''
    Clean sequence description for each seqRecord element
    :param input_fasta: fasta sequences as a list of SeqRecord object
    '''
    for elem in input_fasta:
        elem.description = ""
    return input_fasta


