import gzip
import glob
import random

files = glob.glob("data/ncbi-genomes-2020-11-20/*.fna.gz")
files = random.sample(files, 30)
with open("merged.fna", "w") as merged:
    for path in files:
        with gzip.open(path) as fna:
            merged.write(fna.read().decode() + "\n")
