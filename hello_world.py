import Bio
from Bio.Seq import Seq

#create a DNA sequence object
dna_sequence = Seq("ATGCTAGCTAGCTAGCTG")

#slice the sequence from index 2 to 10
sliced_sequence = dna_sequence[2:11]

#concatenate with another sequence
another_sequence = Seq("GGCTAG")
concatenated_sequence = sliced_sequence + another_sequence

print("Concatenated sequence:", concatenated_sequence)

#transcribe the concatenated sequence into RNA
rna_sequence = concatenated_sequence.transcribe()
print("RNA Sequence:", rna_sequence)
print(len(rna_sequence))

#translate the RNA sequence inot a protien sequence
protein_sequence = rna_sequence.translate()
print("Protien sequence:", protein_sequence)