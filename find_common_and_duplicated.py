import pandas as pd

for length in ("1000", "5000"):
    data = pd.read_csv(f"parebrick_{length}/preprocessed_data/blocks_coords.csv")
    print(f"Number of duplicated blocks ({length}):\t", sum(data.groupby("block")["species"].value_counts() > 1))
    print(f"Number of common blocks ({length}):\t", sum(data.groupby("block")["species"].nunique() == 30))
