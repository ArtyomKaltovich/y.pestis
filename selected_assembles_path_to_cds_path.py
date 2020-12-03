with open("data/selected.txt", "r") as selected, open("data/selected_cds.txt", "w") as cds:
    for path in selected:
        id, _, _ = path.rpartition("_")
        id += "_cds_from_genomic.fna.gz"
        cds.write(f"{id}\n")
