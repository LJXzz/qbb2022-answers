## 2. Using plink, perform PCA on the genotypes of the cell lines

Firstly, covert vcf file into plink format:
plink --vcf genotypes.vcf --recode --out genotypes --const-fid --allow-extra-chr

Then, generate the .bed file:
plink --allow-extra-chr --file genotypes --noweb --make-bed --out genotypes

Then, do PCA:
plink --allow-extra-chr --threads 20 -bfile genotypes --pca 20 --out genotypes

I run PCA 20 times and I now have a .eigenvec to record the eigenvector. I use the first two PCA to draw the plot.


## 3. 

To calculate the allele frequence, I use: 
plink --bfile genotypes --freq --out filefrquency

which outputs a filefrquency.frq file with frequence

## 4. 

First we have to :
sed 's/_/ /g'< genotypes_copy.eigenvec >final.eigenvec
cut -c3- final.eigenvec > geno.eigenvec


Then run

plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar geno.eigenvec --allow-no-sex --out CB_phenotype_gwas_results

plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar geno.eigenvec --allow-no-sex --out GS_phenotype_gwas_results


## 6 

for CB, the most significant SNP is rs17113501 . So I do boxplot for this SNP.

            CHR         SNP         BP A1  ...    STAT          P  -LOG10_P        i
    633297    2  rs10170982  101592772  T  ...  -5.206  6.201e-07  6.207538   633297
    633318    2  rs10186803  101594055  C  ...  -5.089  1.104e-06  5.957031   633318
    633360    2  rs12622974  101600032  G  ...  -5.044  1.273e-06  5.895172   633360
    633381    2  rs17025871  101600219  T  ...  -5.112  9.389e-07  6.027381   633381
    633402    2  rs13394005  101600574  G  ...  -5.026  1.394e-06  5.855737   633402
    665826    2    rs934755  118986661  G  ...  -4.715  5.652e-06  5.247798   665826
    1419390   4   rs4975102   80804407  G  ...  -5.145  8.095e-07  6.091783  1419390
    1859382   5   rs4434376  124245896  G  ...   4.719  5.314e-06  5.274578  1859382
    2387322   7   rs1993246   17443702  T  ...   4.968  1.895e-06  5.722391  2387322
    2387427   7    rs606056   17467607  A  ...  -4.904  2.523e-06  5.598083  2387427
    3430413  10  rs17113501  104230536  T  ...   5.589  4.691e-07  6.328735  3430413
    3466071  10  rs10886150  119580089  C  ...  -5.137    8.4e-07  6.075721  3466071
    4037208  13   rs1777631   20954111  T  ...   5.214  2.249e-06  5.648011  4037208
    4182171  13   rs1538063   85138591  A  ...   4.641  7.413e-06  5.130006  4182171
    5059194  19  rs10413538   20370690  T  ...      -5  4.735e-06  5.324680  5059194
    5059215  19   rs7257475   20372113  T  ...  -5.133  2.713e-06  5.566550  5059215



## 7

For bot CB and GS, the most significant SNP rs17113501
Accroding to UCSC browser, this location of SNP is near a region encoing promoter-associated histone mark(H3K4Me1/H3K4Me3) in differencet cell ines.
So that might be the genes we want to study.
