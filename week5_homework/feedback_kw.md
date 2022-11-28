## Week 5 -- 10 points possible

1 + 1 + 0 + 0 + 1 + 1 + 1 + 1 + 1 + 0.5  = 7.5 points out of 10

1. Filter reads, Call peaks, and intersect peaks across Sox2 replicates (0.33 points each)

* Should filter the reads for the non-input bam files as well. Looks like you did based on the mac2 commands, but I don't see the commands listed.
* the genome size for mac2 callpeak should be different, [as seen here for chr17](https://github.com/igvteam/igv/blob/master/genomes/sizes/mm10.chrom.sizes)

2. Find the number of total peaks and overlapping peaks for Klf4 and Sox2 (0.5 for commands, 0.5 for result)

* did you use `wc -l` commands to find number of peaks?

3. scale bedgraph files (4 different datasets, 0.25 each)

* don't see commands for this in the readme --> +0

4. crop bedgraph files (4 different datasets, 0.25 each)

* don't see commands for this in the readme --> +0

5. python script for plotting

* very good script!

6. 4 panel plot of read pile ups

* fantastic plot!

7. motif finding sort intersected sox2 replicate narrow peak by 5th columm, keep first 300 lines, awk command for reformatting (0.33 each)

8. use samtools faidx to extract peak sequences and meme-chip to perform motif finding (0.5 each)

9. download and unpack motif database

* code for having done this?

10. match profiles from tomtom for klf4 and sox2 (0.5 for commands, 0.5 for result)

* code for doing this? --> +0.5
