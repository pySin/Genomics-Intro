from Bio import SeqIO

# DNA read
DNA = SeqIO.read("gene2.fna", "fasta")
DNA_100 = DNA.seq[:100]

# Transcribe the DNA to mRNA
# mRNA_sequence = DNA.seq.transcribe()
mRNA_sequence_100 = DNA_100.transcribe()
print(f"mRNA original---: {DNA_100}")
print(f"mRNA transcribed: {mRNA_sequence_100}")
