import gzip
import os
import random
import re
import shutil
from collections import defaultdict
from typing import Dict

from Bio import SeqIO
import pandas as pd

DIR = "data/ncbi-genomes-2020-12-03/"
GENES_SAMPLE_SIZE = 100

pathes = pd.read_csv("data/selected.csv")["label"]

pathes = [(DIR, p.partition("\n")[0]) for p in pathes]
pathes = random.sample(pathes, 30)

genes: Dict[str, Dict[str, str]] = defaultdict(dict)  # Dict[gene, Dict[sample, seq]]
pattern = re.compile(r"\[gene=(\w+)\]")

for path in pathes:
    with gzip.open(os.path.join(*path), "rt") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            if m := re.search(pattern, record.description):
                gene = m.group(1)
                genes[gene][path[-1]] = record.seq

# select only genes presented in every sample
genes = {key: value for key, value in genes.items() if len(value) == len(pathes)}
genes = dict(random.sample(list(genes.items()), GENES_SAMPLE_SIZE))

if os.path.exists("genes"):
    shutil.rmtree("genes")
os.makedirs("genes")

for gene, seqs in genes.items():
    with open(f"genes/{gene}.fna", "w") as file:
        for id, seq in seqs.items():
            file.write(f">{id}\n{seq}\n")
