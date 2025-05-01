from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio import SearchIO

# Sequence read
DNA = SeqIO.read("gene2.fna", "fasta")

# Get mRNA from DNA
mRNA_sequence = DNA.seq.transcribe()

# Get the amino acids from the RNA sequence
amino_acids = mRNA_sequence.translate()

proteins = [p for p in amino_acids.split("*")]
# print(f"Proteins: {proteins}")
print(f"Protein length: {len(proteins)}")

# for i in range(10):
#     print(f"Protein: {proteins[i]}, Length: {len(proteins[i])}")

ordered_proteins = sorted(proteins, key=lambda x: len(x), reverse=True)
[print(f"Protein: {p}, Length: {len(p)}") for p in ordered_proteins[:20]]

# Save the largest protein in FASTA file
longest_protein = ordered_proteins[0]
# print(longest_protein)

with open("largest_protein.fasta", "w") as file:
    file.write(f">protein\n{longest_protein}")

result = NCBIWWW.qblast("blastp", "pdb", longest_protein)
blast_result = SearchIO.read(result, "blast-xml")

print(f"NCBI result: {result}")
for r in blast_result:
    print(f"Data line: {r}")
