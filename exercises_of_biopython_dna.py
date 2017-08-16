#-*- coding:utf8 -*-
#!usr/bin/python

####################################### PART0 Description ##############################################################

# Filename:        exercises_of_biopython_dna.py
# Description:     doing some exercises about bio_python
#                  dna.fasta is a txt of DNA sequence
#                  A record in a dna.fasta file is defined as a single-line header, followed by lines of sequence data.
#                  The header line is distinguished from the sequence data by a greater-than (">") symbol in the first
#                  column. The word following the ">" symbol is the identifier of the sequence, and the rest of the line
#                  is an optional description of the entry. There should be no space between the ">" and the first
#                  letter of the identifier.  An open reading frame (ORF) is the part of a reading frame that has the
#                  potential to encode a protein. It starts with a start codon (ATG), and ends with a stop codon
#                  (TAA, TAG or TGA). For instance, ATGAAATAG is an ORF of length 9.
#                  This program is written to solve the question about"What is the length of the longest ORF appearing
#                  in reading frame 1 or frame 2 or frame 3 of any of the sequences"
# Author:          ZhMi
# E-mail:          
# Create:          2015-8-29
# Recent-changes:  2015-8-30

####################################### Part1 : coding    ##############################################################

fp = open("/home/zhmi/Documents/dna2.fasta")
original_list = list()
sequlengthlist = list()

try:
    original_list = fp.readlines()
except:
    print "Read Error !"
finally:
    fp.close()

total_original_str = ''
def combine_sequence(line):
    global total_original_str
    line = line.strip()
    if line[0]=='>':
        line = '>'
    total_original_str = total_original_str + line
map(combine_sequence,original_list)
sequence_list = total_original_str.split('>')
sequence_list = filter(lambda x:x!='',sequence_list)

def seperate_three_sequence(line,read_frame):
    templist = []
    templine = line[3-read_frame:]
    tempstr = ''
    for i in xrange((len(line)-1)/3):
        tempstr = templine[0:3]
        templist.append(tempstr)
        templine = templine[3:]
    return templist

frame_input = input("Please input the reading frame of sequence:")
three_dna_sequence_list = map(lambda element_in_list: seperate_three_sequence(element_in_list, frame_input), sequence_list)

def end_code_position_find(end_code_list,sequence):
    try:
        end_code_list.append(sequence.index('TAG'))
    except:
        pass
    try:
        end_code_list.append(sequence.index('TAA'))
    except:
        pass
    try:
        end_code_list.append(sequence.index('TGA'))
    except:
        pass
    return end_code_list

def ofr_sequence_find(line):
    templist = []
    while(len(line)):
        try:
            begin_code_pos = line.index('ATG')
        except:
            begin_code_pos = -1
        if begin_code_pos==-1:
            break
        else:
            line = line[begin_code_pos:]
            end_code_pos_list = []
            end_code_position_find(end_code_pos_list,line)
            if len(end_code_pos_list)==0 :
                break
            else:
                end_code_pos = min(end_code_pos_list)
                templine = line[:end_code_pos+1]
                templist.append(templine)
                line = line[end_code_pos+1:]
    return templist

ofr_sequence_list = map(ofr_sequence_find,three_dna_sequence_list)
ofr_sequence_list = filter(lambda x:len(x)!=0,ofr_sequence_list)

'''
[example about flatten]
a = [[1,3],[2,4],[3,5],["abc","def"]]
>>> a1 = [y for x in a for y in x]
>>> a1[1,3,2,4,3,5,"abc","def"]
'''

ofr_sequence_list = [y for x in ofr_sequence_list for y in x] #[flatten action]
ofr_sequence_length_list = map(len,ofr_sequence_list)
max_ofr_sequence_length = 3*max(ofr_sequence_length_list)
print "max length of max_ofr_sequence_length:",max_ofr_sequence_length








