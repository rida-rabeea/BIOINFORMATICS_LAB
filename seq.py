from Bio import SeqIO

#create a function to parse a fasta file
def read_fasta(file_path):
    for record in SeqIO.parse(file_path,"fasta"):
        print(f"Description : {record.description}")
        print(f"Sequence : {record.seq}")
        print()

#specify path to the fasta file
fasta_file = "fasta_1.fasta"

#call the function to read the fasta file and print the sequence data
read_fasta(fasta_file)