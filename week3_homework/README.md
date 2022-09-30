#!/bin/bash


bwa index sacCer3.fa 

for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
	bwa mem \
	-R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" \
	-t 4 \
	-o ${SAMPLE}.sam \
	sacCer3.fa ${SAMPLE}.fastq
done

for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
	samtools sort -@4 -O bam -o ${SAMPLE}.bam ${SAMPLE}.sam
done

for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
	samtools index ${SAMPLE}.bam > ${SAMPLE}.bam.bai
done


freebayes --genotype-qualities -p 1 -f sacCer3.fa \
	A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam > variants.vcf

vcffilter -f "QUAL > 0.99" variants.vcf > results.vcf

vcfallelicprimitives -k -g results.vcf > v.vcf

snpeff ann R64-1-1.99 v.vcf > final.vcf
