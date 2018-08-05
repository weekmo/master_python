import fastatools as bio
import time


# Get cDNA in a list
def cdna_list(input_file):
    cdna_l = []
    with open(input_file, 'r') as f:
        dna_list = bio.fasta_list2(f)
        for k, v in dna_list:
            cdna_l.append((k, cdna(v)))
    return cdna_l


# Get single cDNA sequence as a string
def cdna(sequence):
    nucleotides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    seq = ''
    for nucleotide in sequence:
        seq += nucleotides[nucleotide]
    return seq


# Write cDNA in a file
def cdna_writer(input_file, output_file):
    with open(output_file, 'w') as f:
        for k, v in cdna_list(input_file):
            bio.write_fasta(f, k, v)


# Write open reading frames in a file
def orf(infile, outfile):
    def check_codon(index, codon):
        if codon == 'ATG' and not semaphores[index]:
            start = ''
            if index < 4:
                start = '+' + str(i + 1 + index) + '+'
            else:
                start = '+c' + str(len(v) - i - index + 3) + '+'
            seq[index] += '*' + start
            semaphores[index] = True
        elif codon in ['TAA', 'TAG', 'TGA'] and semaphores[index]:
            stop = ''
            if index < 4:
                stop = '+' + str(i + 3 + index) + '+'
            else:
                stop = '+' + str(len(v) - i + 1 - index) + '+'
            seq[index] += codon + stop + '*'
            semaphores[index] = False

        if semaphores[index]:
            seq[index] += codon

    with open(outfile, 'w') as fw:
        with open(infile, 'r') as f:
            semaphores = [False for _ in range(6)]
            seq = ['' for _ in range(6)]
            for head, v in bio.fasta_list2(f):
                cdna_codon = cdna(v)[::-1]
                for i in range(0, len(v), 3):
                    check_codon(0, v[i:i + 3])
                    check_codon(1, v[i + 1:i + 4])
                    check_codon(2, v[i + 2:i + 5])
                    check_codon(3, cdna_codon[i:i + 3])
                    check_codon(4, cdna_codon[i + 1:i + 4])
                    check_codon(5, cdna_codon[i + 2:i + 5])
                for i in set("".join(seq).split('*')):
                    if len(i) > 6 and i[-1:] == '+':
                        i = i.split('+')
                        bio.write_fasta(fw, "|".join(head.split('|')[:-1]) + '|:' + i[1] + '-' + i[3], i[2])


# Write open reading frames in a file using loop
def orf2(infile, outfile):
    def check_codon(index, codon):
        if codon == 'ATG' and not semaphores[index]:
            start = ''
            if index < 4:
                start = '+' + str(i + 1 + index) + '+'
            else:
                start = '+c' + str(len(v) - i - index + 3) + '+'
            seq[index] += '*' + start
            semaphores[index] = True
        elif codon in ['TAA', 'TAG', 'TGA'] and semaphores[index]:
            stop = ''
            if index < 4:
                stop = '+' + str(i + 3 + index) + '+'
            else:
                stop = '+' + str(len(v) - i + 1 - index) + '+'
            seq[index] += codon + stop + '*'
            semaphores[index] = False

        if semaphores[index]:
            seq[index] += codon

    with open(outfile, 'w') as fw:
        with open(infile, 'r') as f:
            semaphores = [False for _ in range(6)]
            seq = ['' for _ in range(6)]
            for head, v in bio.fasta_list2(f):
                cdna_codon = cdna(v)[::-1]
                for i in range(0, len(v), 3):
                    for gd in range(3):
                        check_codon(gd, v[i + gd:i + 3 + gd])
                        check_codon(gd + 3, cdna_codon[i + gd:i + 3 + gd])
                for i in set("".join(seq).split('*')):
                    if len(i) > 6 and i[-1:] == '+':
                        i = i.split('+')
                        bio.write_fasta(fw, "|".join(head.split('|')[:-1]) + '|:' + i[1] + '-' + i[3], i[2])


# I find that the orf function as is faster than orf2
"""
speed1=0
speed2=0
for i in range(1000):
    start=time.time()
    orf('ecoli-genome-sample.fna','test1.txt')
    speed1+=time.time()-start

    start=time.time()
    orf2('ecoli-genome-sample.fna','test2.txt')
    speed2+=time.time()-start

print(speed1/1000)
print(speed2/1000)
"""
