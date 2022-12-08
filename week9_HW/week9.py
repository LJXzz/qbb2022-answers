#!/usr/bin/env python
import sys
import math
import numpy as np
import numpy.lib.recfunctions as rfn
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import seaborn as sns
import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

#Step 0a: Read in the data
input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = list(input_arr.dtype.names)
row_names = input_arr["t_name"]

#print(col_names)

fpkm_values=np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8', usecols = (1,2,3,4,5,6,7,8,9,10))
#print(fpkm_values)


#Step 0b: Process input data   
fpkm_values_2D = rfn.structured_to_unstructured(fpkm_values,dtype=np.float)
mean = np.median(fpkm_values_2D, axis=1, out=None, overwrite_input=False, keepdims=False)
position = np.where(mean <= 0)
filtered_fpkm_values = np.delete(fpkm_values_2D, position, axis=0)
transformed_fpkm = np.log2(filtered_fpkm_values+0.1)
#print(transformed_fpkm)

#Step 1:Clustering
#row for genes and col for samples
gene_cluster = scipy.cluster.hierarchy.linkage(transformed_fpkm, method='single', metric='euclidean')
sample_cluster = scipy.cluster.hierarchy.linkage(transformed_fpkm.T, method='single', metric='euclidean')
genes_id = scipy.cluster.hierarchy.leaves_list(gene_cluster)
samples_id = scipy.cluster.hierarchy.leaves_list(sample_cluster)
row_rearr = transformed_fpkm[genes_id]
col_rearr = row_rearr.T[samples_id]
samples_name = np.array(col_names[1:])[samples_id]
#print(col_re_pos)

fig,ax = plt.subplots(figsize=(10,8))
ax = sns.heatmap(col_rearr.T)
ax.set_xticklabels(labels=samples_name, fontsize= 8)
ax.set_xlabel("stages")
ax.set_ylabel("samples")
plt.tight_layout()
#plt.show()

fig,ax = plt.subplots(figsize=(10,8))
dn = scipy.cluster.hierarchy.dendrogram(sample_cluster, labels = samples_name)
plt.tight_layout()
#plt.show()




#Step 2: Differential Gene Expression
#log data: transformed_fpkm

#1.
sex = []
stage = []
for i in col_names[1:]:
	sex.append(i.split("_")[0])
	stage.append(i.split("_")[1])

#print(sex)
#print(stage)

p = []
beta = []
for i in range(transformed_fpkm.shape[0]):
	list_of_tuples = []
	for j in range(len(col_names[1:])):
		list_of_tuples.append((row_names[i],transformed_fpkm[i,j], sex[j], stage[j]))
	longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
	transcript = ols(formula = 'fpkm ~ stage + 1', data = longdf, subset=None, drop_cols=None).fit()
    #p = []
    #beta = []	
	p.append(transcript.pvalues['stage'])
	beta.append(transcript.params["stage"])
#print(p)
#print(beta)

#2.
fix,ax= plt.subplots()
ax = sm.qqplot(np.array(p), dist = scipy.stats.uniform, line = "45", fit = True)
plt.tight_layout()
#plt.show()

#3.

test = statsmodels.stats.multitest.multipletests(p, alpha=0.1, method='sidak', is_sorted=False, returnsorted=False)
#print(test[0])
diff_stage=[]
        
for i in range(len(test[0])):
    if test[0][i] == True:
        diff_stage.append(row_names[i])        

#4.      
p_sex = []
beta_sex = []
for i in range(transformed_fpkm.shape[0]):
	list_of_tuples = []
	for j in range(len(col_names[1:])):
		list_of_tuples.append((row_names[i],transformed_fpkm[i,j], sex[j], stage[j]))
	longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
	transcript = ols(formula = 'fpkm ~ stage + sex + 1', data = longdf, subset=None, drop_cols=None).fit()
    #p = []
    #beta = []	
	p_sex.append(transcript.pvalues['stage'])
	beta_sex.append(transcript.params["stage"])
    

#5.
test_sex = statsmodels.stats.multitest.multipletests(p_sex, alpha=0.1, method='sidak', is_sorted=False, returnsorted=False)
diff_sex=[]

for i in range(len(test_sex[0])):
    if test_sex[0][i] == True:
        diff_sex.append(row_names[i])        
        
# 6.
print(len(diff_stage))
print(len(diff_sex))
overlap = [value for value in diff_sex if value in diff_stage]
#print(overlap)
print(len(overlap))
    

#7.
# betas on the x axis and -log10(p-value) on the y-axis
x_sign = []
y_sign = []
x_insign =[]
y_insign = []
for i in range(len(p_sex)):
    a = -math.log(p_sex[i],10)
    if a>1:
        y_sign.append(a)
        x_sign.append(beta_sex[i])
    else:
        x_insign.append(beta_sex[i])
        y_insign.append(a)
        
        
        
plt.scatter(x_insign,y_insign,label='insignificant')
plt.scatter(x_sign,y_sign,label='significant')
plt.tight_layout()
#plt.show()









