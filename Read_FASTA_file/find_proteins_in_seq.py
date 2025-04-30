from Bio import SeqIO
from collections import Counter


# Sequence read
DNA = SeqIO.read("gene2.fna", "fasta")

# Get mRNA from DNA
mRNA_sequence = DNA.seq.transcribe()

# Get the amino acids from the RNA sequence
amino_acids = mRNA_sequence.translate()

proteins = [p for p in amino_acids.split("*")]
print(f"Proteins: {proteins}")
print(f"Protein length: {len(proteins)}")

for i in range(10):
    print(f"Protein: {proteins[i]}, Length: {len(proteins[i])}")


