import pandas as pd

NUMBER_OF_SAMPLES = 44

data = pd.read_csv("result/gene_vector.csv")
data["N"] = data.sum(1)
data[data["N"] == NUMBER_OF_SAMPLES]["gene"].to_csv("result/core_genes.csv")
data[(data["N"] >= 3) & (data["N"] <= 10)]["gene"].to_csv("result/rare_genes.csv")
data[(data["N"] >= NUMBER_OF_SAMPLES - 6) & (data["N"] <= NUMBER_OF_SAMPLES - 4)]["gene"].to_csv("result/common_genes.csv")
