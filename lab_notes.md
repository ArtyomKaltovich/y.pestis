#03.11.2020
 - download data

#04.11.2020
 - create script for gene vector calculation (gene_vector.py), put result to result/gene_vector.csv
 - create script (select_gene_on_frequency.py) for selecting core genes (presented in every sample),
 common genes (presented in almost every sample except 4 or 5 samples),
 rare genes (presented in 4-5 samples).
 Put genes id to according files in result folder.
 - create script (select_gene_seq_by_id.py) to collect sequences by gene, and put result to result folder.

#06.11.2020
 - create tree for rare genes, use 2 genes (traD and TraN), because both of them gave only one outstanding organism.
 - create tree for common (yopO) and core genes(rnr).
 - for every gene MUSCLE codon alignment was made, using default settings.
 - every tree was build by minimal evolution method with default settings.
 - all alignment and trees were build using megax 10.1.8 software on linux machine.  
