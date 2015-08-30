#-*- coding:utf8 -*-
#!usr/bin/python

####################################### PART0 Description ##############################################################

# Filename:        exercises_of_biopython_dna.py
# Description:     doing some exercises about biopython
# Author:          ZhMi
# E-mail:          zmmingtiandege1314@126.com
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

for i in xrange(len(original_list)):
    original_list[i] = original_list[i].strip()
    if original_list[i][0] == '>':
       original_list[i] = '>'
    total_original_str =  total_original_str + original_list[i];

sequence_list = total_original_str.split('>')
sequence_list = filter(lambda x:x!='',sequence_list)

'''
[text codes]
print "length of sequence_list:",len(sequence_list)
length_sequence_list = map(len,sequence_list)
print length_sequence_list
'''

#sepratelist = filter(lambda x:x[0:3]=='ATG',sepratelist)
#sepratelist = filter(lambda x:x[-3:]=='TAG' or x[-3:]=='TAA'or x[-3:]=='TGA',sepratelist)
#three_dna_sequence_list = []

def seperate_three_sequence(line):
    templist = []
    templine = line[1:]
    tempstr = ''
    for i in xrange((len(line)-1)/3):
        tempstr = templine[0:3]
        templist.append(tempstr)
        templine = templine[3:]
    return templist

three_dna_sequence_list = map(seperate_three_sequence,sequence_list)

'''
print 'length of three_dna_sequence_list:',len(three_dna_sequence_list)
[test codes]
for i in xrange(3):
    print "******-----*******"
    print three_dna_sequence_list[i]
    print '\n'
'''

def ofr_sequence_find(line):
    templist = []
    line = line[1:]
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
            try:
                end_code_pos_list.append(line.index('TAG'))
            except:
                pass
            try:
                end_code_pos_list.append(line.index('TAA'))
            except:
                pass
            try:
                end_code_pos_list.append(line.index('TGA'))
            except:
                pass
            if len(end_code_pos_list)==0 :
                break
            else:
                end_code_pos = min(end_code_pos_list)
                templine = line[:end_code_pos+1]
                templist.append(templine)
                line = line[end_code_pos+1:]
    return templist

ofr_sequence_list = map(ofr_sequence_find,three_dna_sequence_list)

#[text codes]
print 'befor filter action,length of ofr_sequence_list:',len(ofr_sequence_list)

ofr_sequence_list = filter(lambda x:len(x)!=0,ofr_sequence_list)
#[text codes]
print 'after filter action,length of ofr_sequence_list:',len(ofr_sequence_list)

'''
[example about flatten]
a = [[1,3],[2,4],[3,5],["abc","def"]]
>>> a1 = [y for x in a for y in x]
>>> a1[1,3,2,4,3,5,"abc","def"]
'''

#[flat vision]
ofr_sequence_list = [y for x in ofr_sequence_list for y in x]

#[text codes]
print 'after flatten action,length of ofr_sequence_list:',len(ofr_sequence_list)

ofr_sequence_length_list = map(lambda x:len(x),ofr_sequence_list)

print 'after get length action,length of ofr_sequence_ength_list',len(ofr_sequence_length_list)

max_ofr_sequence_length = max(ofr_sequence_length_list)
print "max length of max_ofr_sequence_length:",3*max_ofr_sequence_length








