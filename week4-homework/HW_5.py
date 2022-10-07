#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import sys

data = sys.argv[1]
data = np.loadtxt(data,dtype=str)
index=[0]
data_p = np.delete(data,index,0) #delete the first line for further use 
    

gwas_data = pd.DataFrame(data_p,columns=data[0]) #change the data into pandas format
gwas_PCA1 = gwas_data.drop_duplicates(subset=["SNP"],keep="first") #get only PCA1
gwas_PCA1["-LOG10_P"]=-np.log10(gwas_PCA1["P"].astype('float')) #change P valve into log
gwas_PCA1["i"]= gwas_PCA1.index #a index for X axes in ploting
list_=[i for i in range(1,23)]
xtick = ['chr'+c for c in map(str,list_)]



#print(gwas_data)

plot = sns.relplot(data=gwas_PCA1, x='i', y='-LOG10_P',\
                   hue='CHR', palette = 'dark', s=4, legend=None) 
# for the plot, we should use chromosome numebrs to group varaibales and give different groups different colors. X should be the SNPs and Y should be the P values


# Find the median position of SNP in each chromosome, give X label at this site       
chrom_df=gwas_PCA1.groupby('CHR')['i'].median()
plot.ax.set_xticks(chrom_df)
plot.ax.set_xticklabels(chrom_df.index)

#label X and Y and give the figure a name
plot.ax.set_xlabel('CHR')
plot.fig.suptitle('Manhattan plot for GS451')
plot.ax.axhline(y=5, linewidth = 2,linestyle="--",color="orange")
plot.ax.set_ylim(0,20)

#every SNP with p-values less than 10^-5
gwas_PCA1_1 = gwas_PCA1[(gwas_PCA1['-LOG10_P'] > 5)]
print(gwas_PCA1_1)
#plot.annotate(gwas_PCA1_1['SNP'],xy=(gwas_PCA1_1['i'],gwas_PCA1_1['-LOG10_P']))

plt.show()
 
