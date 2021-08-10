
from numpy import record
import mapid
import fasta
from Bio import SeqIO
from io import StringIO

# test for filter_fasta_seq
seq = list(SeqIO.parse(StringIO('>a\nAGCTNACTG\n>b\nAGCT'), 'fasta'))
assert len(fasta.filter_fasta_seqs(seq)) == 1, "failed to filter sequences."

# test for get_ccds_id
uniprotid = "P14550"
ccdsid = "CCDS523.1"
assert ccdsid == mapid.get_ccds_id(uniprotid), "failed in mapping CCDS id."

print("Everything has been passed.")

