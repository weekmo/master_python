#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:58:57 2017

@author: mohammed
This file is just to execute exercises
"""
import os
import ex2
def ex1_a():
    print("Ex1-(a)\n")
    with open("ecoli-genome.fna") as f:
        hd, seq = ex2.ft.single_fasta_sequence(f)
        print('header:',hd)
    print('sequence length:',len(seq))
def ex1_b():
    print('\n\n---------------------------------','\nEx1-(b)')
    with open('ecoli-genes.ffn') as f:
        for hd,seq in ex2.ft.fasta_list(f):
            print(hd,'\n',seq)
def ex1_d():
    print('\n\n---------------------------------','\nEx1-(d)')
    ex2.ft.longest_shortest('ecoli-proteome.faa')
    
def ex1_e():
    print('\n\n---------------------------------','\nEx1-(e)')
    with open("ecoli-genes.ffn") as f:
        sequence = ex2.ft.fasta_list(f)
        with open('ex1_e.ffn', 'w') as f2:
            ex2.ft.write_fasta(f2, sequence[0][0], sequence[0][1])
            ex2.ft.write_fasta(f2, sequence[1][0], sequence[1][1])
            ex2.ft.write_fasta(f2, sequence[2][0], sequence[2][1])
            ex2.ft.write_fasta(f2, sequence[3][0], sequence[3][1])
def ex2_a():
    print('\n\n---------------------------------','\nEx2-(a)')
    ex2.gene_translator('drosophila/chr4.ffn','ex2_a.faa')
    
def ex2_b():
    print('\n\n---------------------------------','\nEx2-(b)')
    print(ex2.codon_freq("ecoli-genes.ffn"))
    
def ex2_c():
    for k,v in ex2.chi_peramino('ecoli-genes.ffn'):
        print('Amino:',k)
        print(v)
    
def ex2_d():
    print('\n\n---------------------------------','\nEx2-(d)')
    print('\nChi between "ecoli-genes.ffn" and "drosophila/*.ffn"')
    filename='ecoli-genes.ffn'
    for i in os.listdir('drosophila'):
        if i.endswith('ffn'):
            print('\nChromosome',i,'and',filename,'\n\n----------------------------------')
            for k,v in ex2.compare_chi_peramino(filename,'drosophila/'+i):
                print('Amino:',k)
                print(v[:-1],'\n')
    print('\nChi between "Chr2L" and "Chr3L"')
    for k,v in ex2.compare_chi_peramino('drosophila/chr2L.ffn','drosophila/chr3L.ffn'):
        print('Amino:',k)
        print(v[:-1],'\n')
def ex2_e():
    ex2.plotting_codon("drosophila/chr2L.ffn","ecoli-genes.ffn","drosophila","ecoli")
                
#ex1_a()
#ex1_b()
#ex1_d()
#ex1_e()
#ex2_a()
#ex2_b()
#ex2_c()
#ex2_d()
#ex2_e()