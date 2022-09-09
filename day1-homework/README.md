# QBB2022 - Day 1 - Homework Exercises Submission

## Excercise 1:

error message: 
Considering  A
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  C
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  G
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  T
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1


Then I tried to google, and google suggested that we have to get variable outside awk with -v and we also have to removing the `$` from the `for $nuc in A C G T`
output:
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G

The output suggests that A and G has more possibilities to mutant to each other as well as C and T. This is because of the similar construction.



## Exercise 2

Firstly, with the Core 15-state model, we have to define what kind of state is related to promoter. According to the paper of the state model, promoters can not be clearly and objectively defined, but  the active states (associated with expressed genes) consist of active transcription start site are mostly like to be the signature of promoter——TssA（state 1），TssAFlnk(state2),TssBiv(state 10), BivFlnk(state 11). 

So first we try to pick all the possible promoter region:

awk '{if ($4 == "1"||$4 == "2"||$4 == "10"||$4 == "11") {print}} ' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > genes.bed

Then we have to intersect the genes.bed with the random_snippet.vcf to list all the promoter region

genefile=/Users/cmdb/qbb2022-answers/day1-homework/genes.bed
vcffile=/Users/cmdb/data/vcf_files/random_snippet.vcf
bedtools intersect -a $vcffile -b $genefile > intersect_out.bed

Finally, we can count the most common alternate allele for a Cytosine reference allele for variants, which is T.
Considering  C
  12 A
  11 G
  39 T
  
The mutation leads to more A-T pairs in promoter. I think this is related to the function of promoter since the active expression is related to the unwinding of DNA and A-T combinantion is less strong than C-G.
  
  
## Exercise 3

"awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed" This code means:
1. skip the line with # at the beginning
2. printe the first variable(chromosome), the second variable minus 1 (st
art point-1), and the second variable(end point) in each row
3. create a file named variants.bed with the data from step 2


"sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed" This code means:
1. Sort the data first with each row's  first character(chromosome). If the first character is same, sort it with the value of second column(start postion). 
2. create a file named  genes.sorted.bed with the data from step 2

"bedtools closest -a variants.bed -b genes.sorted.bed" this code means: 
find A(variants.bed) the nearest (that is, least genomic distance from the start or end of A) feature in B(genes.sorted.bed)



First error: Error: unable to open file or unable to determine types for file variants.bed
Second error: Error: Sorted input specified, but the file variants.bed has the following out of order record
chr21	5218156	5218157

script: 

        awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
        perl -p -i -e 's/ /\t/g' variants.bed
        sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
        sort -k1,1 -k2,2n variants.bed > variants.sorted.bed
        bedtools closest -a variants.sorted.bed -b genes.sorted.bed

        bash exercise3.sh ~/data/vcf_files/random_snippet.vcf|cut -f7|wc-----10293  variants are returned
        bash exercise3.sh ~/data/vcf_files/random_snippet.vcf|cut -f7|sort|uniq -c|wc------200 unique genes

Therefor 51 variants on average are therefore connected to a gene with bedtools closest.

  





