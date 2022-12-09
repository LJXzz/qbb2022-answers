#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from matplotlib.lines import Line2D


def allele_freq1(start_freq, p_size):
	initial = np.random.binomial(2*p_size, start_freq)
	freq = initial/(2*p_size)
	freq_a=1-freq
	allele_freq = [] #allele frequence for generations 
	allele_freq.append(freq)
	g=1
	while freq != 1 and freq_a != 1:
		g=g+1
		initial = np.random.binomial(2*p_size, freq)
		freq = initial/(2*p_size)
		freq_a = 1-freq
		allele_freq.append(freq)
	return allele_freq
    
fig, ax = plt.subplots()
freq = allele_freq1(0.5,200)
gen = []
for i in range(len(freq)):
	gen.append(i+1)
ax.plot(gen, freq)
ax.set_xlabel("generation")
ax.set_ylabel("allele frequency")
ax.set_title('p=0.5,N=2000')
#plt.savefig("allele frequency over generation")
#plt.show()

fix_time = []
i=0
while i != 1000:
	i=i+1
	fixallele_freq = allele_freq1(0.5, 100)
	fix_time.append(len(fixallele_freq))

fig, ax = plt.subplots()
ax.hist(fix_time, density=True)
ax.set_xlabel("fixation time")
ax.set_ylabel("density")
ax.set_title('Time to fixation over 1000 independent runs')
plt.show()



pop_size = []
pop = [100,300,500,700,900,1100]
for i in pop:
	fixallele_freq = allele_freq1(0.5, i)
	pop_size.append(len(fixallele_freq))

fig, ax = plt.subplots()
ax.plot(pop, pop_size)
ax.set_ylabel("fixation time")
ax.set_xlabel("population size")
ax.set_title('time to fixation with different population')
plt.show()



fix_time_5 = []
fixation_time_average = []
freq_5 = [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
for i in freq_5:
	fix_single_allele = []
	j=0
	while j != 100:
		j=j+1 
		fixallele_freq = allele_freq1(i, 100)
		fix_single_allele.append(len(fixallele_freq))
	fix_time_5.append(fix_single_allele)
	average = 0
	for i in fix_single_allele:
		average = average + i
	fixation_time_average.append(average/len(fix_single_allele))

# violin plot
fig, ax = plt.subplots()
plt.violinplot(fix_time_5)
ax.set_xticks([0,1,2,3,4,5,6,7,8,9], freq_5)
ax.set_ylabel("fixation time")
ax.set_xlabel("starting allele frequency")
ax.text(7,np.max(fix_time_5),'population size = 1000') #set the position
ax.set_title('Violin plot')
plt.show()

