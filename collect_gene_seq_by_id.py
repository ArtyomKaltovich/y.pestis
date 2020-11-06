import glob
import gzip
import os
import re

from Bio import SeqIO

IDS = [
"frdC",
"frdA",
"epmA",
"mscM",
"psd",
"rsgA",
"orn",
"queG",
"nnr",
"tsaE",
"amiB",
"mutL",
"miaA",
"hfq",
"hflX",
"hflK",
"hflC",
"nsrR",
"rnr",
]
PATTERN = re.compile(f"\[gene=({'|'.join(id_ for id_ in IDS)})\]")
seqs = {key: [] for key in IDS}

for i, file in enumerate(glob.glob("data/*.gz")):
    sample = file[5:-24]
    with gzip.open(file, "rt") as handle:
        for seq_record in SeqIO.parse(handle, "fasta"):
            if m := re.search(PATTERN, seq_record.description):
                gene = m.group(1)
                seqs[gene].append((sample, seq_record.seq))
    #if i > 1:
    #    break

for gene, lines in seqs.items():
    with open(os.path.join("result", f"{gene}.fasta"), "w") as file:
        for sample, line in lines:
            file.write(f">{sample}\n{line}\n")
