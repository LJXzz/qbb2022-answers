## part1: 

medaka_variant -i methylation.bam -f hg38.fa -r "chr11:1900000-2800000" -p chr11.vcf
medaka_variant -i methylation.bam -f hg38.fa -r "chr14:100700000-100990000" -p chr14.vcf
medaka_variant -i methylation.bam -f hg38.fa -r "chr15:23600000-25900000" -p chr15.vcf
medaka_variant -i methylation.bam -f hg38.fa -r "chr20:58800000-58912000" -p chr20.vcf


## Part2:
whatshap haplotag -o chr11.bam -r chr11:1900000:2800000 --reference hg38.fa --output-haplotag-list chr11_haplotag_list.txt medaka_variant_chr11/round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr14.bam -r chr14:100700000:100990000 --reference hg38.fa --output-haplotag-list chr14_haplotag_list.txt medaka_variant_chr14/round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr15.bam -r chr15:23600000:25900000 --reference hg38.fa --output-haplotag-list chr15_haplotag_list.txt medaka_variant_chr15/round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr20.bam -r chr20:58800000:58912000 --reference hg38.fa --output-haplotag-list chr20_haplotag_list.txt medaka_variant_chr20/round_0_hap_mixed_phased.vcf.gz methylation.bam


## part3: 
whatshap split --output-h1 chr11_h1.bam  --output-h2 chr11_h2.bam chr11.bam chr11_haplotag_list.txt 
whatshap split --output-h1 chr14_h1.bam  --output-h2 chr14_h2.bam chr14.bam chr14_haplotag_list.txt 
whatshap split --output-h1 chr15_h1.bam  --output-h2 chr15_h2.bam chr15.bam chr15_haplotag_list.txt 
whatshap split --output-h1 chr20_h1.bam  --output-h2 chr20_h2.bam chr20.bam chr20_haplotag_list.txt 

samtools cat -o h1.bam chr11_h1.bam chr14_h1.bam chr15_h1.bam chr20_h1.bam
samtools cat -o h2.bam chr11_h2.bam chr14_h2.bam chr15_h2.bam chr20_h2.bam
samtools index h1.bam > h1.bam.bai
samtools index h2.bam > h2.bam.bai 

## part 5: 
./igv.sh h1.bam
./igv.sh h2.bam

## part 6:

I don't think each region in H1 or H2 to correspond to the same parent of origin (i.e. the same haplotype) because when do the pervious step in whatshap, reads from different haplotype are combined.WhatsHap can phase multiple samples that are not related if provided with a multi-sample VCF file and WhatsHap switches to the combined read-based/pedigree phasing algorithm.

