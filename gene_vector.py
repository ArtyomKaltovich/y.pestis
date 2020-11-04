import gzip
import glob
import re
import pandas as pd

pattern = re.compile(r"\[gene=(\w+)\]")


result = {}
for i, file in enumerate(glob.glob("data/*.gz")):
    sample = file[5:-24]
    current = {}
    with gzip.open(file) as gz:
        for line in gz:
            if m := re.search(pattern, line.decode()):
                gene = m.group(1)
                current[gene] = 1
    result[sample] = current
    #if i > 1:
    #    break

result = pd.DataFrame(result)
result = result.reset_index()
result = result.rename(columns=dict(index="gene"))
result.to_csv("result/gene_vector.csv", index=False)
