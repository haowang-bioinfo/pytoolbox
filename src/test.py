
from numpy import record
from numpy.core.fromnumeric import sort
import mapid
import fasta
import system
from Bio import SeqIO
from io import StringIO

# test for filter_fasta_seq
seq = list(SeqIO.parse(StringIO('>a\nAGCTNACTG\n>b\nAGCT'), 'fasta'))
assert len(fasta.filter_fasta_seqs(seq)) == 1, "failed to filter sequences."

# test for get_ccds_id
uniprotid = "P14550"
ccdsid = "CCDS523.1"
assert ccdsid == mapid.get_ccds_id(uniprotid), "failed in mapping CCDS id."

# test for system
files = ['__init__.py', 'fasta.py', 'gem.py', 'mapid.py', 'parsers.py', 'system.py', 'test.py']
assert files == sorted(system.load_files_in_folder("./")), "failed in loading files."

print("All tests have passed.")

