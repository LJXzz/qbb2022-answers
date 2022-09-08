## exercise 1

### 1.  
Subsetting exons.chr21.bed.vcf: Covering 1107407 bp
processed_pseudogene.chr21.bed.vcf: Covering 956640 bp
Subsetting protein_coding.chr21.bed.vcf: Covering 13780687 bp

### 2. 
To campare two images, we can use ImageMagick, whichis exatly a tools to do image comarasion.

### 3. 
I found different types: unprocessed_pseudogene, transcribed_unprocessed_pseudogene, lncRNA, miRNA. It's not easy to find what is intersting just look through the data by eyes but I feel that the account of pseudogene is much more than I expect.




## exercise 2
Improved script: 
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

I got five figure. The plot for protein soding shows the most similiar trend to random snippet. For processed__pseudogene and exons, the allele counts concentrate more on the low level(less than 3000).LncRNA shows relatively average density at relatively high allele countc

## exercise 3
SYNOPSIS
     bxlab/cmdb-plot-vcfs -- The scripts in this file are trying to output the allele count density histogram for specific feature from your vcf file.

USAGE 

     add specific feature(genetpye) you want in subset_regions.sh line 12thon 
     
     bash do_all.sh file1.vcf gencode.gtf
     
     python plot_vcf_ac.py file.vcf

 DESCRIPTION
1. Create .bed files for features of interest
- add feature you are intersted in subset_regions.sh
- Run subset_regions.sh Bash script
- Use grep to get the information for data with specific feature you are intrested in

2. Subsetting .vcf for each feature
- output .vcf file for each feature
3. calculate bp coverage 
4. create the plot for each vcf file
5. create the histogram for each file
