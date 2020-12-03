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

#20.11.2020
 - create script ``select_30_seqs.py`` for selecting and merging 30 random genomes.
 as there are already almost 60 genomes and it will take to many time to process them all.
 - ``sibeliaz -k 15 -n -o sibeliaz_out merged.fn``
 - ``maf2synteny -s fine.txt -b 5000 sibeliaz_out/blocks_coords.gff``
 - ``maf2synteny -s fine_500.txt -b 1000 sibeliaz_out/blocks_coords.gff``

#03.12.2020
 - extract files names of samples, because they wasn't presented in merged.fna by get_file_path_from_merged.py and
   selected_assembles_path_to_cds_path.py, save them to data\selected.txt and data\selected_cds.txt
 - create parse_cds.py to extract 100 random genes, represented in every sample, select random genes, because 
   conservative ones are too conservatives.
 - create script muscle.py to align gene sequence and merge them to one alignment
 - create tree by megax minumal evalution model and put it to result/all_genes.newick and plot/all_genes_tree.png

