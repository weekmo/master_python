import sys


# Get sequence positions without considering orf length
def get_sequence_position(fasta_file):
    pos_dictionary = {}
    with open(fasta_file, 'r') as fr:
        for line in fr:
            if line[0] == '>':
                line = ''.join(line.rstrip('\n').split(' ')[0].split(':')[1:]).split(',')
                """if len(line)>1:
                    print(line)"""
                for pos in line:
                    pos = pos.split('-')
                    if pos[1] in pos_dictionary:
                        pos_dictionary[pos[1]] += (pos[0],)
                    else:
                        pos_dictionary[pos[1]] = (pos[0],)
    return pos_dictionary


# Get sequence positions with considering orf length
def get_sequence_position_mit_lenght(fasta_file, length):
    pos_dictionary = {}
    with open(fasta_file, 'r') as fr:
        for line in fr:
            if line[0] == '>':
                line = ''.join(line.rstrip('\n').split(' ')[0].split(':')[1:]).split(',')
                for pos in line:
                    pos = pos.split('-')
                    orf_lenght = 0
                    if pos[0][0] == 'c':
                        orf_lenght = abs(int(pos[0][1:]) - int(pos[1]))
                    else:
                        orf_lenght = abs(int(pos[0]) - int(pos[1]))
                    if orf_lenght >= length:
                        if pos[1] in pos_dictionary:
                            pos_dictionary[pos[1]] += (pos[0],)
                        else:
                            pos_dictionary[pos[1]] = (pos[0],)
    return pos_dictionary


# Validate orf software
def orf_validation(orf_file, genes_file, length=0):
    genes = get_sequence_position_mit_lenght(genes_file, length)
    orf = get_sequence_position_mit_lenght(orf_file, length)
    tot_orf = 0
    orf_pred = 0
    orf_stop = 0
    num_genes = len(genes)
    for i, j in orf.items():
        tot_orf += len(i)

    for stop, start in genes.items():
        if stop in orf:
            orf_stop += 1
            for i in orf[stop]:
                if i in start:
                    orf_pred += 1
    print('Total number of open reading frames:', tot_orf)
    print('Total number of genes:', num_genes)
    print('Ratio of open reading frames correctly predicting a gene:', orf_pred / num_genes)
    print('Total number and ratio of open reading frames correctly predicting at least the stop codon of a gene',
          orf_stop / num_genes)
    print('Number of missed genes', num_genes - orf_stop)


standard_genes = sys.argv[2]
orfs = sys.argv[1]
orf_validation(orfs, standard_genes)

# Validate with different lengths
for i in range(50, 351, 50):
    print('\nWithe length >=', i)
    orf_validation(orfs, standard_genes, i * 3)
