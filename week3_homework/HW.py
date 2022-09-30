#!/usr/bin/env python3
from vcfParser import parse_vcf
import matplotlib.pyplot as plt
import numpy as np
import sys

variant = sys.argv[1]
vcf_read = parse_vcf(variant)


#a = vcf_read[1][7]['ANN'].split(',')
#for i in a:
    #each=i.split("|")
    #print(each[2])

#After read the vcf file, we have list for each variant
#Ex. ['chrI', 968, '.', 'C', 'T', 2.07762, '.', {'AB': 0.0, 'ABP': 0.0, 'AC': 3, 'AF': 0.3, 'AN': 10, 'AO': 10, 'CIGAR': '1X1M1X', 'DP': 120, 'DPB': 122.333, 'DPRA': 0.428571, 'EPP': 24.725, 'EPPR': 3.0103, 'GTI': 2, 'LEN': 1, 'MEANALT': 1.0, 'MQM': 53.8, 'MQMR': 52.0727, 'NS': 10, 'NUMALT': 1, 'ODDS': 0.546771, 'PAIRED': 0.0, 'PAIREDR': 0.0, 'PAO': 0.0, 'PQA': 0.0, 'PQR': 199.0, 'PRO': 7.0, 'QA': 346, 'QR': 3440, 'RO': 110, 'RPL': 0.0, 'RPP': 24.725, 'RPPR': 3.0103, 'RPR': 10.0, 'RUN': 1, 'SAF': 10, 'SAP': 24.725, 'SAR': 0, 'SRF': 110, 'SRP': 241.872, 'SRR': 0, 'TYPE': 'snp', 'ANN': 'T|upstream_gene_variant|MODIFIER|YAL067W-A|YAL067W-A|transcript|YAL067W-A_mRNA|protein_coding||c.-1512C>T|||||1512|,T|downstream_gene_variant|MODIFIER|YAL069W|YAL069W|transcript|YAL069W_mRNA|protein_coding||c.*319C>T|||||319|,T|downstream_gene_variant|MODIFIER|YAL068W-A|YAL068W-A|transcript|YAL068W-A_mRNA|protein_coding||c.*176C>T|||||176|,T|downstream_gene_variant|MODIFIER|PAU8|YAL068C|transcript|YAL068C_mRNA|protein_coding||c.*839G>A|||||839|,T|intergenic_region|MODIFIER|YAL068W-A-PAU8|YAL068W-A-YAL068C|intergenic_region|YAL068W-A-YAL068C|||n.968C>T||||||'}, ['GT', 'GQ', 'DP', 'RO', 'QR', 'AO', 'QA', 'GL'], ['0', '160.002', '10', '10', '352', '0', '0', '0,-31.9591'], ['1', '0.0941603', '2', '0', '0', '2', '64', '-6.06226,0'], ['0', '129.106', '6', '6', '165', '0', '0', '0,-7.32368'], ['0', '160.002', '27', '27', '862', '0', '0', '0,-73.3194'], ['1', '1.92965', '2', '0', '0', '2', '77', '-7.28565,0'], ['0', '160.002', '13', '10', '372', '3', '110', '0,-25.9895'], ['1', '0.000144861', '1', '0', '0', '1', '31', '-3.09914,0'], ['0', '160.002', '25', '25', '748', '0', '0', '0,-68.1948'], ['0', '160.002', '18', '16', '482', '2', '64', '0,-43.9896'], ['0', '160.002', '16', '16', '459', '0', '0', '0,-41.8132']]


#DP:read depth, [9][2]-[19][2] in line, call for DP
#GQ:Genotype Quality, [9][1]-[19][1] in line, 
#AF:allele frequency, [7] in line, call for AF
#ANN; Functional annotation, [7] in line, call for ANN. Annotation is the [1] in ANN list


read_depth=[]  # DP in the file 
quality=[]     #GQ for Genotype Quality in file 
frequency=[]   #AF for allele frequence in file 
effect={} # to store all possible effects and counts
effect_name=[]
effect_count=[]
    
for n,line in enumerate(vcf_read):
    if n == 0:
        continue
    for i in range(9,19):
        try:
            read_depth.append(int(line[i][2]))
        except:
            continue
        try:
            quality.append(float(line[i][1]))
        except:
            continue
    try: 
        frequency.append(float(line[7]['AF']))
    except:
        continue
    try:
        effect_list=line[7]['ANN'].split(',')
        for i in effect_list:
            a=i.split("|")
            if a[2] not in effect.keys():
                effect[a[2]]=1
            else:
                effect[a[2]]+=1
    except:
        continue

   
for i in effect.keys():
    effect_name.append(i)
    effect_count.append(effect[i])   
    
fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(48,24),squeeze=False)
ax[0][0].hist(read_depth)
ax[0][0].set_yscale("log")
ax[0][0].set_ylabel("Counts")
ax[0][0].set_xlabel("Read depths")
ax[0][0].title.set_text("Distribution of varient genotypes' read depth")

ax[1][0].hist(quality)
ax[1][0].set_ylabel("Counts")
ax[1][0].set_xlabel("Quality")
ax[1][0].title.set_text("Distribution of variant genotypes' quality")
ax[1][0].set_yscale("log")

ax[0][1].hist(frequency)
ax[0][1].set_ylabel("Counts")
ax[0][1].set_xlabel("Frequency")
ax[0][1].title.set_text("Distribution of variants' frequency")



x=np.array(effect_name)
y=np.array(effect_count)
ax[1][1].bar(x,y)
plt.xticks(fontsize=8,rotation=-30)
ax[1][1].set_ylabel("Counts")
ax[1][1].set_xlabel("Predicted effects")
ax[1][1].title.set_text("Summary of predicted effects")

fig.savefig("week3.png")
