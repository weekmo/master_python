# بسم الله الرحمن الرحيم
import math

#Get frequency in single codon file
def single_fasta_sequence(filename):
    sequ = ''
    head = next(filename)
    for i in filename:
        sequ += i.rstrip('\n')
    return head[1:], sequ

#Get sequences in multi codon file
def fasta_list(filename):
    fasta_dict = {}
    fasta_listata = []
    hd = ''
    for i in filename:
        if i[0] == '>':
            hd = i[1:].rstrip('\n')
            fasta_dict[hd] = ''
        else:
            fasta_dict[hd] += i.rstrip('\n')
    for k, v in fasta_dict.items():
        fasta_listata.append((k, v))
    return fasta_listata

# Yield seqence and head
def fasta_sequences(filename):
    with open(filename) as f:
        counter = 0
        hd = ''
        seq = ''
        for line in f:
            if line[0] == '>':
                if counter > 0:
                    yield hd, seq
                    seq = ''
                hd = line[1:].rstrip('\n')
                counter += 1
            else:
                seq += line.rstrip('\n')
        else:
            yield hd, seq


def longest_shortest(filename):
    mx = 0
    mn = math.inf
    head_min = ''
    head_max = ''
    for hd, seq in fasta_sequences(filename):
        if len(seq) > mx:
            mx = len(seq)
            head_max = hd
        if len(seq) < mn:
            mn = len(seq)
            head_min = hd
    print("Max and Min sequences in", filename)
    print("\nUsing 'fasta_sequences' function:")
    print("\nMax header:", head_max)
    print("Max number:", mx)
    print("\nMin header:", head_min)
    print("Min number:", mn)
    print("\nUsing 'fasta_list' function:")
    with open(filename) as f:
        seq_tuple = sorted([(i[0], len(i[1])) for i in fasta_list(f)], key=lambda x: x[1])
        print("Max header:", seq_tuple[len(seq_tuple) - 1][0])
        print("Max number:", seq_tuple[len(seq_tuple) - 1][1])
        print("\nMin header:", seq_tuple[0][0])
        print("Min number:", seq_tuple[0][1])

# write to fasta file
def write_fasta(outfile, header, sequence):
    if outfile.tell() == 0:
        outfile.write('>' + header)
    else:
        outfile.write('\n>' + header)
    for i in range(0, len(sequence), 70):
        outfile.write('\n' + sequence[i:i + 70])
