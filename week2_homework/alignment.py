#!/usr/bin/env python3

import numpy as np
import sys
from fasta import readFASTA



input_sequences = readFASTA(open(sys.argv[1]))
sequence1=input_sequences[0][1]
sequence2=input_sequences[1][1]

score = open(sys.argv[2]) # read the score 
sc = np.genfromtxt(score, dtype="str" )


l=[] # a list with all pairs and  scores
for i in range(1,sc.shape[0]):
    for j in range(1,sc.shape[1]):
        a=(sc[0][i]+sc[j][0])
        l.append([a,sc[i][j]])


dic_score={}  # change the list into a dictionary to check the score
for i in range(len(l)): 
    dic_score[l[i][0]]=l[i][1]
# if we want to check the mismatch score for a certain mismatch pair, just:  dic_score[sequence1[i])+sequence2[i]]


gap_penality = -300 #should change the number for protein alignment

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1)) # Initialize F-matrix
T_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1)) # Initialize traceback matrix but I think I don't need one

for i in range(len(sequence1)+1):
    F_matrix[i,0] = i*gap_penality
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j*gap_penality

for i in range(1,len(sequence1)+1):
    for j in range(1,len(sequence2)+1):
        d = F_matrix[i-1,j-1] + int(dic_score[sequence1[i-1]+sequence2[j-1]])
        h = F_matrix[i,j-1] + gap_penality # gap in sequence1
        v = F_matrix[i-1,j] + gap_penality # gap in sequence2
        
        F_matrix[i,j] = max(d,h,v)
        if max(d,h,v) == d:
            T_matrix[i,j] = 0
        if max(d,h,v) == h:
            T_matrix[i,j] = 1 
        if max(d,h,v) == v:
            T_matrix[i,j] = -1

# Trying to track back by comparing 
align1 = ""
align2 = ""
i = len(sequence1)
j = len(sequence2)
gap_1 = 0
gap_2 = 0
finalscore = F_matrix[i][j]
#trace back from the end
while i > 0 and j > 0: 
    score = F_matrix[i][j]
    d = F_matrix[i-1][j-1]
    h = F_matrix[i][j-1]
    v = F_matrix[i-1][j]
   
    if score == d + int(dic_score[sequence1[i-1]+sequence2[j-1]]):
        align1 += sequence1[i-1]
        align2 += sequence2[j-1]
        i -= 1
        j -= 1
       
        
    elif score == h + gap_penality:
        align2 += sequence2[j-1]
        align1 += '-'
        j -= 1
        gap_1 += 1
        
        
    elif score == v + gap_penality:
        align2 += '-'
        align1 += sequence1[i-1]
        i -= 1
        gap_2 +=1
        

while i > 0:
    align1 += sequence1[i-1]
    align2 += '-'
    i -= 1
    gap_2 +=1
    
while j > 0:
    align1 += '-'
    align2 += sequence2[j-1]
    j -= 1
    gap_1 += 1
    
#reverse the order of the characters in each sequence.
align1 = align1[::-1]
align2 = align2[::-1]
    
print(align1)
print(align2)
print(gap_1)
print(gap_2)
print(finalscore)


