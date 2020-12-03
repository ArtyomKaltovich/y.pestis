import glob
import os
import shutil

from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline as align
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO

MUSCLE_EXE = "/home/my/miniconda3/bin/muscle"


def main():
    alignments = []
    for path in glob.glob("genes/*.fna"):
        _, _, file = path.rpartition("/")
        print(file)
        out = f"alignments/{file}"
        align(MUSCLE_EXE, input=path, out=out)()
        alignment = MultipleSeqAlignment(SeqIO.parse(out, "fasta"))
        alignment.sort(key=lambda record: record.id)
        alignments.append(alignment)
    iterator = iter(alignments)
    first = next(iterator)
    all = sum(iterator, start=first)
    with open("result/all_genes_allignment.fna", "w") as handle:
        AlignIO.write(all, handle, "fasta")


if __name__ == '__main__':
    shutil.rmtree("alignments", ignore_errors=True)
    os.mkdir("alignments")
    main()
