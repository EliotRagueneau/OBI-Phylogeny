LISTE=$(cat raw_protein_sequence.fasta | grep -o ">.*" | cut -d " " -f 1 | tr -d ">")
for access in $LISTE
do
    echo $access
    efetch -db protein -format fasta_cds_na -id ${access}

done
