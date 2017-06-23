import scipy.stats as sci
import fastatools as ft
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
#codon dict
genecode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_', 'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}
#Translate genes considering start and stop codon
def gene_translator_frame(genes_filename, output_filename):
    with open(genes_filename, 'r') as f:
        list_seq = ft.fasta_list(f)
        write_switch = False
        with open(output_filename, 'w') as fw:
            for seq_tuple in list_seq:
                sequence = ''
                for i in range(0, len(seq_tuple[1]), 3):
                    code = seq_tuple[1][i:i + 3]
                    if code in ['ATG','GTG']:
                        if not write_switch:
                            code='ATG'
                        write_switch = True
                    elif code in ['TAA', 'TAG', 'TGA']:
                        write_switch = False
                    if write_switch and len(code)==3:
                        sequence += genecode[code]
                ft.write_fasta(fw, seq_tuple[0], sequence)

#Translate all genes without considering start and stop codon
def gene_translator(genes_filename, output_filename):
    with open(genes_filename, 'r') as f:
        list_seq = ft.fasta_list(f)
        with open(output_filename, 'w') as fw:
            for seq_tuple in list_seq:
                sequence = ''
                for i in range(0, len(seq_tuple[1]), 3):
                    code=seq_tuple[1][i:i + 3]
                    if len(code)==3:
                        sequence += genecode[code]
                ft.write_fasta(fw, seq_tuple[0], sequence.rstrip('_'))

#codon frequenceis
def codon_freq(genes_filename):
    frequs = {}
    codon_frequs={}
    for k,v in ft.fasta_sequences(genes_filename):
        for i in range(0,len(v),3):
            code=v[i:i+3]
            if len(code)==3:
                if code in frequs:
                    frequs[code]+=1
                else:
                    frequs[code]=1
    #freq = {i[1][j:j + 3]: i[1].count(i[1][j:j + 3]) for i in ft.fasta_list(f) for j in range(0, len(i[1]), 3)}
    # if i[1][j:j + 3] not in ['ATG','TAA','TAG','TGA']}
    for k, v in frequs.items():
        if genecode[k] not in ['T', 'M']:
            if genecode[k] in codon_frequs:
                codon_frequs[genecode[k]].append((k, v))
            else:
                codon_frequs[genecode[k]] = [(k, v)]
    return codon_frequs

#Amino acid frequenceis
def amino_freq(genes_filename):
    with open(genes_filename, 'r') as f:
        seq_list = ft.fasta_list(f)
        amino_frequence = {j: i[1].count(j) for i in seq_list for j in i[1]}
        return amino_frequence
#Calculate Chi per amino acid
def chi_peramino(filename):
    freq=codon_freq(filename)
    for k,v in freq.items():
        lis=[f[1] for f in v]
        yield k,sci.chisquare(lis)
        
def compare_chi_peramino(filename1,filename2):
    freq1=codon_freq(filename1)
    freq2=codon_freq(filename2)
    for k in freq1.keys():
        lis1=[f[1] for f in freq1[k]]
        lis2=[f[1] for f in freq2[k]]
        yield k,sci.chi2_contingency([lis1,lis2])
#compare chi between two
def chi2_contingency_codon(filename1,filename2):
    freq1=codon_freq(filename1)
    freq2=codon_freq(filename2)
    freq1=[j[1] for i in freq1.values() for j in i]
    freq2=[j[1] for i in freq2.values() for j in i]
    return sci.chi2_contingency([freq1,freq2])

#By default it will save all plots in one pdf file
def plotting_codon(filename1,filename2,name1,name2,show_save='save'):
    
    file1=codon_freq(filename1)
    with PdfPages('Plotting_output.pdf') as pdf:
        for k,v in codon_freq(filename2).items():
            lable_file2=tuple()
            freq_file2=tuple()
            freq_file1=tuple()
            v=sorted(v,key=lambda x: x[0])
            h=sorted(file1[k],key=lambda x: x[0])
            for i,j in v:
                lable_file2+=(i,)
                freq_file2+=(j,)
            for i,j in h:
                freq_file1+=(j,)
            ind = np.arange(len(lable_file2))
            width = 0.35
            fig, ax = plt.subplots()
            ax.bar(ind, freq_file2, width, color='r')
            ax.bar(ind + width, freq_file1, width, color='y')
            
            ax.set_ylabel('Frequencies')
            ax.set_title('Amino ('+k+') in "'+name1+'" and "'+name2+'"')
            ax.set_xticks(ind + width / 2)
            ax.set_xticklabels(lable_file2)
            ax.legend((name2, name1))
            if show_save=='save':
                pdf.savefig()
                plt.close()
            else:
                plt.show()  
        