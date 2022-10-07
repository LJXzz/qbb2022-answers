#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import sys
from vcfParser import parse_vcf


geno = sys.argv[1]
pheno = sys.argv[2]
geno = parse_vcf(geno)
pheno = np.loadtxt(pheno,dtype=str)

 

#what we have to do first is match the genotypes and the traits for rs17113501
SNP_geno=[]
for i in range(len(geno)):
    if geno[i][2] == 'rs17113501':
        SNP_geno = geno[i]
        
#['10', 104230536, 'rs17113501', 'A', 'T', '.', '.', {'PR': None}, 'GT', '0/0', '0/0', '0/1', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/1', '0/1', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/1', '0/0', '0/1', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/1', '0/1', '0/0', '0/0', '0/0', '0/0', './.', '0/1', '0/1', '0/0', '0/0', '0/0', '0/0', '0/0', '0/1', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/1', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/0', '0/1', '0/0', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.', './.']     

geno_pheno = []

for i in range(1,len(pheno)):
    geno_pheno.append([SNP_geno[i+8],pheno[i][2]])
for i in geno_pheno:
    if i[1] == 'NA':
        geno_pheno.remove(i)
for i in geno_pheno:
    i[1]=float(i[1])
    
ref=[]
heter=[]
alter=[]
for i in geno_pheno:
    if i[0]=='0/0':
        ref.append(i[1])
    if i[0]=='0/1':
        heter.append(i[1])
    else:
        alter.append(i[1])


ref= np.array(ref)
heter = np.array(heter)
alter = np.array(alter)
data = [ref,heter,alter]
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
ax = fig.add_axes([0, 0, 1, 1])
bp = ax.boxplot(data)

plt.title("rs17113501")
plt.show()

