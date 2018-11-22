import re

list_sp = [
    "Aa, Aquifex aeolicus",
    "Af, Archaeoglobus fulgidus",
    "Ap, Aeropyrum pernix",
    "Bb, Borrelia burgdorferi",
    "Bh, Bacillus halodurans",
    "Bs, Bacillus subtilis",
    "Cj, Campylobacter jejuni",
    "Cp, Chlamydia pneumoniae",
    "Ct, Chlamydia trachomatis",
    "Dr, Deinococcus radiodurans",
    "c, Escherichia coli",
    "Hp, Helicobacter pylori",
    "Mth, Methanothermobacter thermautotrophicus",
    "Mtu, Mycobacterium tuberculosis",
    "Nm, Neisseria meningitidis",
    "Pa, Pseudomonas aeruginosa",
    "Rp, Rickettsia prowazekii",
    "Ssp, Synechocystis sp",
    "Tm, Thermotoga maritima",
    "Tp, Treponema pallidum",
    "Vc, Vibrio cholerae",
    "Uu, Ureaplasma urealyticum",
    "Xf, Xylella fastidiosa"
]
dico_out = {}
for nom in list_sp:
    dico_out[nom.split(", ")[1]] = {"nom": nom}

specie = re.compile(r'[A-Z][a-z]+\s[a-z]{2,}')
with open("/home/eliot/Documents/Travail/M1/Projets/ProjetOBIS1/Phe t-RNA/raw_protein_sequence.fasta", "r") as prot_file:
    for line in prot_file.readlines():

        if line[0] == '>':
            if specie.search(line):
                latin = specie.search(line).group(0)
                dico_out[latin]["prot"] = line.replace(">", "").split(" ")[0].replace("_", "\_")

            else:
                dico_out[line]["prot"] = line.replace(">", "").split(" ")[0].replace("_", "\_")

# for specie in dico_out:
#     try:
#         print("\t{} &  & {} \\\\".format(specie, dico_out[specie]["prot"].replace("_", "\_")))
#     except:
#         pass

specie = re.compile(r'[A-Z][a-z]+\s[a-z]{2,}')
with open("/home/eliot/Documents/Travail/M1/Projets/ProjetOBIS1/Phe t-RNA/DNA_pheT.fasta", "r") as dna_file:
    for line in dna_file.readlines():
        if line[0] == '>':
            latin = specie.search(line).group(0)
            try:
                dico_out[latin]["dna"] = line.replace(">", "").split(":")[0]
            except:
                pass

for specie in dico_out:
    if "prot" in dico_out[specie]:
        if "dna" in dico_out[specie]:
            print("\t{} & \\textit{{{}}} & {} \\\\".format(dico_out[specie]["nom"],
                                                           dico_out[specie]["dna"],
                                                           dico_out[specie]["prot"]))
        else:
            print("\t{} & \\textit{{{}}} & {} \\\\".format(dico_out[specie]["nom"],
                                                           "Introuvable",
                                                           dico_out[specie]["prot"]))
    else:
        print("\t{} & \\textit{{{}}} & \\textit{{{}}} \\\\".format(dico_out[specie]["nom"],
                                                                   "Gene loss",
                                                                   "Protein loss"))
