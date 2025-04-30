from Bio import SeqIO
from collections import Counter
from matplotlib import pyplot as plt

# Sequence read
DNA = SeqIO.read("gene2.fna", "fasta")

# Full transcription
mRNA_sequence = DNA.seq.transcribe()

# Translate all aminoacids
full_amino_acids = mRNA_sequence.translate()

most_common_amino_acids = Counter(full_amino_acids).most_common(20)
print(f"Most Common 20 amino acids: {most_common_amino_acids}")

most_common_aa_count = [amount for letter, amount in most_common_amino_acids if letter != "*"]
most_common_aa_letters = [letter for letter, amount in most_common_amino_acids if letter != "*"]

fig, ax = plt.subplots()

