#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys

freq = sys.argv[1]
freq =np.loadtxt(freq,dtype=str)
AF = []
for i in range(1,len(freq)):
    AF.append(float(freq[i][4]))
#print(AF)

plt.hist(AF)
plt.xlabel('allele frequency')
plt.ylabel('density')

plt.show()