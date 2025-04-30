from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


fasta_string = open("gene.fna").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

blast_records = NCBIXML.parse(result_handle)

for b in blast_records:
    for alignment in b.alignments:
        for hsp in alignment.hsps:
            print(f"Sequence: {alignment.title}")

