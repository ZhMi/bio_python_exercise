#-*- coding:utf8 -*-
#!usr/bin/python

####################################### PART0 : Description ############################################################
# Filename:        exercises_of_biopython_dna.py
# Description:     Doing some exercises about bio_python
#                  dna.fasta is a txt of DNA sequence
#                  A record in a dna.fasta file is defined as a single-line header, followed by lines of sequence data.
#                  The header line is distinguished from the sequence data by a greater-than (">") symbol in the first
#                  column. The word following the ">" symbol is the identifier of the sequence, and the rest of the line
#                  is an optional description of the entry. There should be no space between the ">" and the first
#                  letter of the identifier.  An open reading frame (ORF) is the part of a reading frame that has the
#                  potential to encode a protein. It starts with a start codon (ATG), and ends with a stop codon
#                  (TAA, TAG or TGA). For instance, ATGAAATAG is an ORF of length 9.
#                  This program is written to solve the question about"What is the length of the longest forward ORF
#                  that appears in the sequence with the identifier gi|142022655|gb|EQ086233.1|16?"
# Author:          ZhMi
# E-mail:          zmmingtiandege1314@126.com
# Create:          2015-9-3
# Recent-changes:  2015-9-3

####################################### Part1 : coding    ##############################################################

fp = open("/home/zhmi/Documents/dna2.fasta")
original_sequence_list = fp.readlines()
fp.close()

def seprate_fun(line):
    '''
    Param:
        line is the element of list original_sequence_list
    Function:
        first,filter sepecial characters "\n"
        then,add sepical flag * at the begin of the sequence with the identifier gi|142022655|gb|EQ086233.1|16
    '''
    line = line.strip()
    if line[0]==">":
        if "gi|142022655|gb|EQ086233.1|16" in line:
            line = ">*"
        else:
            line = ">"
    return line

total_sequence_str = reduce(lambda x,y:x+y,map(seprate_fun,original_sequence_list))
#take original_sequence_list into a string ,for example : change list[1,2,3,4,5,6] into string "123456"
sequence_list = filter(lambda x:x!='',total_sequence_str.split('>'))
#every element of sequence_list is a sequence of DNA
pure_sequence_str = filter(lambda x:x[0]=="*",sequence_list)[0][1:]
#select sequence with the identifier gi|142022655|gb|EQ086233.1|16,type(pure_sequence_str) is string

def seperate_three_sequence(line,read_frame):
    '''
        Param:
            line:sequence of DNA
            read_frame:
                read_frame_1: AT  CTA GCC ATC CGC
                read_frame_2: A   TCT AGC CAT CCG C
                read_frame_3: ATC TAG CCA TCC GC
    '''
    templist = []
    templine = line[3-read_frame:]
    tempstr = ''
    for i in xrange((len(line)-1)/3):
        tempstr = templine[0:3]
        templist.append(tempstr)
        templine = templine[3:]
    return templist












