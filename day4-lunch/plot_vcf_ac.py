#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

fig, ax = plt.subplots()
ax.hist( ac, density=True, log=True )
plt.title(vcf +"figure")
plt.xlabel("allele counts")
plt.ylabel("log(density)")
fig.savefig( vcf + ".png" )

fs.close()

