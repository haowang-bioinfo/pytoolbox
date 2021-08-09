# -*- coding: utf-8 -*-

import pandas as pd


def get_column_from_tsv(tsv_file, column_id, to_list=True):
    """
    read a column from a tsv file and convert the content into a list by default
    :param tsv_file: a tsv file to read
    :param column_id: 
    :param to_list: 
    """
    tsv_content = pd.read_table(tsv_file)
    target_column = tsv_content[column_id]
    if to_list:
        return target_column.to_list()
    return target_column


def get_column_from_csv(csv_file, column_id, to_list=True):
    """
    read a column from a csv file and convert the content into a list by default
    :param csv_file: a csv file to read
    :param column_id: 
    :param to_list: 
    """
    csv_content = pd.read_csv(csv_file)
    target_column = csv_content[column_id]
    if to_list:
        return target_column.to_list()
    return target_column


