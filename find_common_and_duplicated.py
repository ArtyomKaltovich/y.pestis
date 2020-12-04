import pandas as pd

LEN = 4.75 * 10 ** 6


def check_duplicates(block):
    return len(block) != len(block.unique())


for length in ("1000", "5000"):
    data = pd.read_csv(f"parebrick_{length}/preprocessed_data/blocks_coords.csv")
    duplicated = data.groupby("block")["species"].nunique() != data.groupby("block")["species"].count()
    print(f"Number of duplicated blocks ({length}):\t", int(duplicated.sum()))
    common = data.groupby("block")["species"].nunique() == 30
    print(f"Number of common blocks ({length}):\t", sum(common))
    data["length"] = data["chr_end"] - data["chr_beg"]
    d = data.groupby("block").aggregate(dict(length="mean"))
    print(f"Coverage common block ({length}):\t", float(d[common].sum()) / LEN)
    print(f"Coverage duplicated block ({length}):\t", float(d[duplicated].sum()) / LEN)
