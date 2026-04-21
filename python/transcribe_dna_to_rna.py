import os

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "../datasets/rosalind_transcribe.txt")

with open(file_path, "r") as file:
    dna = file.read()

rna = dna.replace("T", "U")
print(rna)