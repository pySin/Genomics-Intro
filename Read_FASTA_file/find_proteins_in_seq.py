from Bio import SeqIO
from collections import Counter


# Sequence read
DNA = SeqIO.read("gene2.fna", "fasta")

# Get mRNA from DNA
mRNA_sequence = DNA.seq.transcribe()

# Get the amino acids from the RNA sequence
amino_acids = mRNA_sequence.translate()

print(f"Amino Acids: {amino_acids[:66]}")


