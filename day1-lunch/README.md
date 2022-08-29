# QBB2022 repository

2. 
code: 
cp ~/data/bed_files/genes.chr21.bed qbb2022-answers/day1-lunch
cp ~/data/bed_files/exons.chr21.bed qbb2022-answers/day1-lunch
cd qbb2022-answers/day1-lunch
less exons.chr21.bed
wc exons.chr21.bed  
13653   40959  327672 exons.chr21.bed   #num of exons = 13653 
wc genes.chr21.bed 
 219     657    5256 genes.chr21.bed     #num of genes = 219
     
b. The mean number of exons per gene is 62.34

c. To find the median, first we have to match each exons to the genes, which means we have to use the genes'  location to compare with the exons's location. So I think the code should firstly compares the start point and the end point of each exons with each genes in order until it finds where the exon locates. And then, the code should count how many exons each gene has and then list in oder. Then we can find the median since we know how many genes in the document.


3. 
b.
First we have to know how many state is there: 
cut -f4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq

we found there is 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

Then we calculate the regions for each state
cut -f4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w(state number )| wc

For state 1: 305
For state 2: 678
For state 3: 79
For state 4: 377
For state 5: 808
For state 6: 148
For state 7: 1050
For state 8: 156
For state 9: 654
For state 10: 17
For state 11: 17
For state 12: 30
For state 13: 62
For state 14: 228
For state 15: 992

c. To determine which state comprises the largest fraction of the genome, we should know the length of each state. To make the calculation easier, we can firstly sort all the data in group by the state. Then we can calculate the length with each line's start point and end point and finally add them all together. Then we have to compare the length of each state to find which has the longest length.





4. 
b. cut -f 2,3 integrated_call_samples.panel | grep AFR| cut -f1| sort|uniq -c 
    
 123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI

c. Firstly, we can 'sort' and 'unqi' the third line to know what the all five populations are. Then we use the same command in 4b by just switching the pop name.




5. 
b. 
cut -f 1,2,3,4,5,6,7,8,9,13 random_snippet.vcf > HG00100.vcf

c. 
 0|0 : 9514
 0|1 : 127
 1|0 : 178
 1|1 : 181
 
 d.
 15
 
 e.
 We can just directly use the command: cut -d ";" -f 7 HG00100.vcf, which split those frequency data with ; and then go to line 7 which is "AFR="
 
 
 
 



     
     
     

