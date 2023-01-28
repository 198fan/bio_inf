# Input:
# 1) string

# Output
# Sum of number for each nucleotides

# for test (need test file)
with open('rosalind_dna.txt') as source:
    test = source.readline()

def cnt_nucleotide(str):
    acgt = [0]*4
    for i in str:
        if i == 'A':
            acgt[0] += 1
        if i == 'C':
            acgt[1] += 1
        if i == 'G':
            acgt[2] += 1
        if i == 'T':
            acgt[3] += 1
    for i in acgt:
        print(i,end=" ")    

cnt_nucleotide(test)

# * String can directly be iterated as char array
# * List can be remove and added by using remove() and append