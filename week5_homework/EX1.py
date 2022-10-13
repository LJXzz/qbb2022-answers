#!/usr/bin/env python

from bdg_loader import load_data
import sys
import matplotlib.pyplot as plt

#load all the bdg to get the x,y for each sample
#Ex. call sox2['X']
sox2=load_data(sys.argv[1])
Klf4=load_data(sys.argv[2])
H3K27ac_D0=load_data(sys.argv[3])
H3K27ac_D2=load_data(sys.argv[4])

#print(sox2['X'])

fig,ax = plt.subplots(4,1,sharex="all",sharey='all')
fig.subplots_adjust(hspace=1)
ax[0].fill_between(sox2['X'],sox2['Y'], label = 'sox2')
ax[1].fill_between(Klf4['X'],Klf4['Y'], label = 'Klf4')
ax[2].fill_between(H3K27ac_D0['X'], H3K27ac_D0['Y'], label = 'H3K27ac_D0')
ax[3].fill_between(H3K27ac_D2['X'], H3K27ac_D2['Y'], label = 'H3K27ac_D2')

ax[0].legend(loc='upper right')
ax[1].legend(loc='upper right')
ax[2].legend(loc='upper right')
ax[3].legend(loc='upper right')

plt.title('ChIP-seq analysis',y=-3)
plt.show()