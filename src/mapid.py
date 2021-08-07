# -*- coding: utf-8 -*-
import re
import requests as r


def get_ccds_id(uniport_id):
    '''
    Return a CCDS id for a given UniProt id
    '''
    url = 'https://www.uniprot.org/uploadlists/'
    uniprot_params = {
        'from': 'ACC+ID',
        'to': 'CCDS_ID',
        'format': 'tab',
        'query': uniport_id
    }
    # Requests will automatically decode content from the server. Most unicode
    # charsets are seamlessly decoded.
    results = r.get(url, uniprot_params)
    ids = re.split('\n|\t', results.text)
    if len(ids) < 4:
        return None
    else:
        return ids[3]
