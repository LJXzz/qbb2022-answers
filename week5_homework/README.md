# Part1
## 1.
    samtools view -bq 10 D2_Sox2_R12_input.bam > F_D2_Sox2_R2_input.bam 
    samtools view -bq 10 D2_Sox2_R1_input.bam > F_D2_Sox2_R1_input.bam 

## 2.
    macs2 callpeak -t F_D2_Sox2_R1.bam -cF_D2_Sox2_R1_input.bam -f BAM -g 1.87e+9 -B
    macs2 callpeak -t F_D2_Sox2_R2.bam -cF_D2_Sox2_R2_input.bam -f BAM -g 1.87e+9 -B

## 3.
    bedtools intersect -a sox2_R1_peaks.narrowPeak -b Sox2_R2peaks.narrowPeak > overlaps.bed

651 peaks appear in both replicates

## 4.
    bedtools intersect -a overlaps.bed -b D2_Klf4_peaks.bed >SK_overlaps.bed

There are 651 peaks for Sox2 and 60peaks for Klf4 and 39 overlaps for these two sample.
Klf4 has 60 peaks in total so 39/60 = 65% of Klf4 peaks colocalized with Sox2.



# Part 2

## 1. 
    sort -k5 sox2_R1_peaks.narrowPeak > R1_Ex2.1.narrowpeak
    sort -k5 sox2_R2_peaks.narrowPeak > R2_Ex2.1.narrowpeak

## 2. 
    head -n 300 R2_Ex2.1.narrowpeak > R2_Ex2.2.narrowpeak
    head -n 300 R1_Ex2.1.narrowpeak > R1_Ex2.2.narrowpeak

## 3. 
    awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' R1_Ex2.2.narrowpeak > R1_Ex2.3.narrowpeak
    awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' R2_Ex2.2.narrowpeak > R2_Ex2.3.narrowpeak

## 4. 
    samtools faidx mm10.fa -r R2_Ex2.3.narrowpeak > R2_Ex2.4.peak
    samtools faidx mm10.fa -r R1_Ex2.3.narrowpeak > R1_Ex2.4.peak

## 5. 
     meme-chip --maxw 7 R1_Ex2.4.peak 
    meme-chip --maxw 7 R2_Ex2.4.peak
 
I get three motifs for sox2 and one motif for Klf4
 
    Sox2:
    
    MOTIF 1 CCCACCC-MEME-1

    letter-probability matrix: alength= 4 w= 7 nsites= 119 E= 3.4e-051
    0.000000	  0.789916	  0.000000	  0.210084	
    0.277311	  0.714286	  0.008403	  0.000000	
    0.000000	  0.966387	  0.033613	  0.000000	
    0.798319	  0.000000	  0.201681	  0.000000	
    0.000000	  1.000000	  0.000000	  0.000000	
    0.000000	  1.000000	  0.000000	  0.000000	
    0.000000	  1.000000	  0.000000	  0.000000	

    MOTIF 2 CCCTSCC-MEME-2

    letter-probability matrix: alength= 4 w= 7 nsites= 52 E= 5.6e-006
    0.000000	  0.942308	  0.000000	  0.057692	
    0.000000	  1.000000	  0.000000	  0.000000	
    0.000000	  1.000000	  0.000000	  0.000000	
    0.019231	  0.000000	  0.000000	  0.980769	
    0.153846	  0.557692	  0.288462	  0.000000	
    0.000000	  1.000000	  0.000000	  0.000000	
    0.000000	  1.000000	  0.000000	  0.000000
 
    MOTIF 3 GGGTGKG-MEME-1

    letter-probability matrix: alength= 4 w= 7 nsites= 149 E= 2.4e-084
    0.000000	  0.000000	  1.000000	  0.000000	
    0.000000	  0.000000	  1.000000	  0.000000	
    0.000000	  0.000000	  1.000000	  0.000000	
    0.234899	  0.093960	  0.000000	  0.671141	
    0.000000	  0.000000	  0.979866	  0.020134	
    0.000000	  0.000000	  0.664430	  0.335570	
    0.241611	  0.000000	  0.758389	  0.000000
    
    Klf4:
    
    MOTIF 1 GGGYGKG-MEME-1

    letter-probability matrix: alength= 4 w= 7 nsites= 53 E= 9.5e-008
      0.207547	  0.000000	  0.792453	  0.000000	
      0.000000	  0.000000	  1.000000	  0.000000	
      0.037736	  0.000000	  0.962264	  0.000000	
      0.056604	  0.320755	  0.000000	  0.622642	
      0.000000	  0.000000	  1.000000	  0.000000	
      0.018868	  0.000000	  0.509434	  0.471698	
      0.283019	  0.000000	  0.698113	  0.018868

   
 
# Part 3

    Through tomtom .html results file for Sox2:
    For CCCACCC, we have 37 matches
    For CCCTSCC, we have 33 matches.
    For GGGTGKG, we have 38 matches

    For motif GGGYGKG of Klf4, we have 33 matches.
    
