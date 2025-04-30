from Bio import SeqIO

# DNA read
DNA = SeqIO.read("gene2.fna", "fasta")
DNA_99 = DNA.seq[:99]

# Transcribe the DNA to mRNA
mRNA_sequence_99 = DNA_99.transcribe()

amino_acids = mRNA_sequence_99.translate()
print(f"Amino Acids: {amino_acids}")
