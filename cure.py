#!/usr/bin/python3
import re

specie = re.compile(r'[A-Z][a-z]+\s[a-z]{2,}')
with open("/home/eliot/ProjetOBIS1/Phe t-RNA/raw_protein_sequence_rooted.fasta") as input_file:
    with open("/home/eliot/ProjetOBIS1/Phe t-RNA/cleaned_protein_sequence_rooted.fasta", 'w') as output_file:
        for line in input_file.readlines():
            if line[0] == '>':
                if specie.search(line):
                    latin = specie.search(line).group(0)
                    output_file.write('>' + latin + '\n')
                else:
                    output_file.write(line)

            else:
                output_file.write(line.replace(".", "-"))
