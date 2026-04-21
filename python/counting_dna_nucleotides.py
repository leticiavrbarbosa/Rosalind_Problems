import os

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "../datasets/rosalind_dna.txt")


with open(file_path, "r") as file:
    content = file.read()

# Counter(string) -> counts number of occurences of each character in string -> O(n) * 1
from collections import Counter
counts = Counter(content)

# print 4 integers counting A C G T
print(f'{counts["A"]} {counts["C"]} {counts["G"]} {counts["T"]} ')