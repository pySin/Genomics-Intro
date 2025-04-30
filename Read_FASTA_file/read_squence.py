from Bio import SeqIO
import matplotlib.pyplot as plt


# DNA read
DNA = SeqIO.read("gene2.fna", "fasta")
print(f"Print DNA: {DNA}")
print(f"Length DNA: {len(DNA)}")


count_nucleotides = {
    "A": DNA.count("A"),
    "G": DNA.count("G"),
    "C": DNA.count("C"),
    "T": DNA.count("T"),
}

fig, ax = plt.subplots()
ax.bar(count_nucleotides.keys(), count_nucleotides.values(), color = ["cornflowerblue", "crimson", "gold", "mediumseagreen"])
ax.set_xlabel("Nucleotides")
ax.set_ylabel("Frequency")
ax.set_title("Nucleotide Frequency")
ax.tick_params(axis="x", labelsize=16)
plt.show()


