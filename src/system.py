# -*- coding: utf-8 -*-

import os
import sys
import glob
import json


def load_files_in_folder(folder_name, file_extension="*", excludePath=True):
    '''
    load filenames within a folder into a list
    '''
    if not os.path.isdir(folder_name):
        sys.exit('Folder "'+folder_name+'" cannot be found!')
    else:
        files = glob.glob(folder_name+"*."+file_extension)
        if excludePath:
            files = [f.replace(folder_name, '') for f in files]
    return files


def read_json_file(file_name):
    '''
    load JSON file by filename
    '''
    # TODO: check file exists
    with open(file_name) as json_object:
        json_content = json.load(json_object)
    return json_content


def write_json_file(json_object, file_name, path='./'):
    '''
    write out JSON file
    '''
    # TODO: check file exists
    with open(path+file_name, 'w') as fp:
        json.dump(json_object, fp, indent=4)


def pretty_json_file(input_file, output_file):
    '''
    pretty Json file with proper indentations
    '''
    write_json_file(read_json_file(input_file), output_file)

