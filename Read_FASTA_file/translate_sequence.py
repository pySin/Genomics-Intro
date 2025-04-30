from Bio import SeqIO
from Bio.Seq import transcribe

# DNA read
DNA = SeqIO.read("gene2.fna", "fasta")
DNA_99 = DNA.seq[:99]

# Transcribe the DNA to mRNA
mRNA_sequence_99 = DNA_99.transcribe()

# Full transcription
mRNA_sequence = DNA.seq.transcribe()

amino_acids = mRNA_sequence_99.translate()
full_amino_acids = mRNA_sequence.translate()

print(f"Amino Acids: {amino_acids}")
print(f"All Amino Acids: {full_amino_acids}")
print(f"Count all aminoacids: {len(full_amino_acids)}")
