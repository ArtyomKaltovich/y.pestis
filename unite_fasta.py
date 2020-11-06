from collections import defaultdict

import pandas as pd
from Bio import SeqIO

files = ["result/alignment_traD.fas", "result/alignment_traN.fas"]


def main(files, result_path):
    result = defaultdict(lambda: defaultdict(str))
    for file in files:
        for seq_record in SeqIO.parse(file, "fasta"):
            result[file][seq_record.id] = seq_record.seq

    result = pd.DataFrame(result)

    for col in result:
        filler = "-" * int(result[col].str.len().max())
        result[col] = result[col].fillna(filler)

    result["S"] = result.sum(1)
    with open(result_path, "w") as file:
        for id_, seq in result["S"].iteritems():
            file.write(f">{id_}\n{seq}\n")


if __name__ == '__main__':
    main(files, "result/alignment_rare.fas")
