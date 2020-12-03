import gzip
import glob
from Bio import SeqIO

files = glob.glob("data/genome_assemblies_genome_fasta/ncbi-genomes-2020-12-03/*.fna.gz")
id_to_file = {}
for file in files:
    with gzip.open(file, "rt") as handle:
        _, _, file = file.rpartition("/")
        for r in SeqIO.parse(handle, "fasta"):
            id_to_file[r.id] = file

with open("data/selected.txt", "w") as selected:
    prev = None
    for r in SeqIO.parse("merged.fna", "fasta"):
        if (current := id_to_file[r.id]) != prev:
            prev = current
            selected.write(f"{prev}\n")
