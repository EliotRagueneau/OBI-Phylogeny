#!/usr/bin/python3
import re

specie = re.compile(r'[A-Z][a-z]+\s[a-z]{2,}')
with open("Phe t-RNA/DNA_pheT.fasta") as input_file:
    with open("Phe t-RNA/cleaned_DNA_pheT.fasta", 'w') as output_file:
        for line in input_file.readlines():
            if line[0] == '>':
                if specie.search(line):
                    latin = specie.search(line).group(0)
                    output_file.write('>' + latin + '\n')
                else:
                    output_file.write(line)

            else:
                output_file.write(line.replace(".", "-"))
