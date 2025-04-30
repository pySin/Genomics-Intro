from Bio import SeqIO
from collections import Counter


# Sequence read
DNA = SeqIO.read("gene2.fna", "fasta")

# Get mRNA from DNA
mRNA_sequence = DNA.seq.transcribe()


