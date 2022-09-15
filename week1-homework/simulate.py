import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 


start = np.random.randint(1, 999901, size = 150000) # set up start point for each reads and we need 150000 reads
    
arr=np.zeros(1000000) # set up the array to record the reads for each position

for i in start:
    for j in range(100):
        num=i+j
        arr[num]=arr[num]+1  #read calculation
 
 
# find the probility under poisson distribution for each coverage.        
x = np.unique(arr)
y=[]
for i in x:
    p= stats.poisson.pmf(i,15)
    y.append(p)


#calculate how many positions have 0 coverage
a = 0    
for i in range(len(arr)):
    if arr[i] == 0:
        a=a+1
print(a)



# draw the plot

fig, ax = plt.subplots()
plt.hist(arr, density = True)
plt.plot(x,y)
ax.set_xlabel("reads")
ax.set_ylabel("frequency")
ax.set_title("simulate sequencing 15x coverage of a 1Mbp genome with 100bp reads")
ax.legend()
plt.show()
        

