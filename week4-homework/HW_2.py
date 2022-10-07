#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys

PCA_full = sys.argv[1]
PCA_full =np.loadtxt(PCA_full, dtype=str)
PCA_1 = []
PCA_2 = []
PCA = []
for i in range (len(PCA_full)):
    #PCA_1.append(float(PCA_full[i][2]))
    #PCA_2.append(float(PCA_full[i][3]))
    PCA.append((float(PCA_full[i][2]),float(PCA_full[i][3])))
#for i in range (len(PCA_1)):
    #A = np.array(float(PCA_1[i]),float(PCA_2[i]))
#A = np.array(PCA_1,PCA_2)
PCA_plot = np.array(PCA)

for i in range(len(PCA_plot)):
    x = PCA_plot[i][0]
    y = PCA_plot[i][1]
    #print(x)
    plt.scatter(x,y)
#print(PCA_plot)
#plt.scatter(PCA_plot[0])
    
plt.xlabel('PCA_1')
plt.ylabel('PCA_2')

plt.show()