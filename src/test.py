
import mapid

uniprotid = "P14550"
ccdsid = "CCDS523.1"
assert ccdsid == mapid.get_ccds_id(uniprotid), "failed in mapping CCDS id."

print("Everything has been passed.")

