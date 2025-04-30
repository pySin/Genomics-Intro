from Bio import SeqIO
from collections import Counter
from matplotlib import pyplot as plt

# Sequence read
DNA = SeqIO.read("gene2.fna", "fasta")

# Full transcription
mRNA_sequence = DNA.seq.transcribe()
print(f"mRNA sequence 50: {mRNA_sequence[:50]}")

# Translate all aminoacids
full_amino_acids = mRNA_sequence.translate()
print(f"Amino Acids count: {len(full_amino_acids)}")

most_common_amino_acids = Counter(full_amino_acids).most_common(20)
print(f"Most Common 20 amino acids: {most_common_amino_acids}")

most_common_aa_count = [amount for letter, amount in most_common_amino_acids if letter != "*"]
most_common_aa_letters = [letter for letter, amount in most_common_amino_acids if letter != "*"]

fig, ax = plt.subplots()
ax.bar(most_common_aa_letters, most_common_aa_count, color = ["cornflowerblue", "crimson", "gold", "mediumseagreen"])
ax.set_xlabel("Amino Acids")
ax.set_ylabel("Frequency")
ax.set_title("Amino Acid Frequency")
ax.tick_params(axis="x", labelsize=16)
plt.show()

