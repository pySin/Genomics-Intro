from Bio.Seq import Seq
from Bio import SeqIO

# DNA read
DNA = SeqIO.read("gene2.fna", "fasta")
print(f"Type DNA: {DNA.seq}")

# Transcribe the DNA to mRNA
mRNA_sequence = DNA.seq.transcribe()
print(f"mRNA transcribed: {mRNA_sequence}")
