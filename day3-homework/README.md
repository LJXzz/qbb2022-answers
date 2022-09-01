# QBB2022 - Day 3 - Homework Exercises Submission

##exercise 1
plink --ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --recode --out testacc --const-fid --allow-extra-chr #create three files with .map, .nosex, .ped

plink --allow-extra-chr --file testacc --noweb --make-bed --out testacc #create a bed file based on .ped file

plink --allow-extra-chr --threads 20 -bfile testacc --pca 3 --out testacc #have PLINK return the first 3 principal components

The Output is 

	#name pac1 pac2 pac3
	HG00096 -0.0109316 -0.0249319 0.00534958
	HG00097 -0.0121359 -0.0290234 0.0192942
	HG00099 -0.0127633 -0.0249592 0.00975894
	HG00100 -0.0121159 -0.0242888 0.0161956
	HG00101 -0.013234 -0.0269284 0.0143007
	HG00102 -0.0120975 -0.0244644 0.0132588
	HG00103 -0.0127035 -0.0265615 0.0113604
	HG00104 -0.012511 -0.0246463 0.0102946
	HG00105 -0.0120922 -0.0274567 0.0116058
	HG00106 -0.0127748 -0.0209314 0.0106013
	HG00107 -0.0132975 -0.0256615 0.0133886
	HG00108 -0.0118509 -0.0222125 0.0121708
	HG00109 -0.0113553 -0.0251803 0.0114703
	HG00110 -0.0113544 -0.0267575 0.012259
	HG00111 -0.0116209 -0.0272237 0.0166021
	HG00112 -0.0115444 -0.0212839 0.0112869
	HG00113 -0.0123868 -0.0232283 0.0156025
	HG00114 -0.012524 -0.0246461 0.00937325
	HG00115 -0.0113614 -0.0242317 0.00758859
	HG00116 -0.0111558 -0.0252679 0.00847206
	HG00117 -0.0129985 -0.0240182 0.0138965
	HG00118 -0.0116277 -0.0257633 0.0116365
	HG00119 -0.0121709 -0.0240149 0.0145125
	...
	

##exercise 2

The code: 
	
  #!/usr/bin/env python
	import matplotlib.pyplot as plt
	import numpy as np
	import sys

	PCAfile=sys.argv[1] 
	arr= np.genfromtxt(PCAfile, dtype = None, delimiter=' ', names = ["col1_name", "col2_pac1", "col3_pac2", "col4_pac3" ], encoding = None)

	#create list to sort data from different PAC
	pac1=[]
	pac2=[]
	pac3=[]
	for i in range(len(arr)):
	    pac1.append(arr[i][1])
	    pac2.append(arr[i][2])
	    pac3.append(arr[i][3])


	#here I show how I get the figure for PAC1 vs PAC2
	x = pac1
	y = pac2

	plt.scatter(x,y)
  
	plt.title("PC1 vs. PC2")
	plt.xlabel("PAC1")
	plt.ylabel("PAC2")
  
	plt.show()
	plt.savefig("Pex2_a.png")

##exercise 3

The code:
	
  #!/usr/bin/env python
	import numpy as np
	from matplotlib import pyplot as plt
	import sys

	fname=sys.argv[1]
	arr= np.genfromtxt(fname, dtype = None, delimiter=' ', names = ["name", "pac1", "pac2", "pac3","pop", "super_pop","gender" ], encoding = None)

	#prepare the data into different list we want
	scatter_x = arr['pac1']
	scatter_y = arr['pac2']
	group_p = arr['pop']
	group_sup = arr['super_pop']
	group_g = arr['gender']
	group_p_u = np.unique(arr['pop']) #find out how many kinds of population is in the date
	group_sup_u=np.unique(arr['super_pop'])#find out how many kinds of super population is in the date
	group_g_u=np.unique(arr['gender']) #find out how many kinds of gender is in the date


	# here is a  example about how I create my figure by sorting with super pop
	cdict={} #dictionary to match different super pop with different colour
	colors = [plt.cm.tab10(i/float(len(group_sup_u)-1)) for i in range(len(group_sup_u))] # generate colurs type we want #generate as much as colors we need(same num compared to the amount of different super pop we have) 
	for i in range(len(group_sup_u)):
	    cdict[group_sup_u[i]]=colors[i] #match  different super pop with different colour

	# create the figure
	fig, ax = plt.subplots()
	for g in np.unique(group_sup): 
	    ix = np.where(group_sup == g)
	    ax.scatter(scatter_x[ix], scatter_y[ix], c = cdict[g], label = g, s = 10)
            

	#label, show and save
	plt.title("PC1 vs. PC2 by sup_pop")
	plt.xlabel("PAC1")
	plt.ylabel("PAC2")
	plt.legend(loc="upper right", ncol = 4)
	plt.show()
	fig.savefig("PCA1 VS PCA2 with sup_pop.png")

