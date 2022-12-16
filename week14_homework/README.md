# Step1
## 1A
git clone https://github.com/marbl/Krona.git
cd Krona/KronaTools/
sudo ./install.pl

## 1B

I used the given python code to generate 8 KRAKEN files

## 1C

ktImportText -q SRR492183_krona.txt -o SRR492183_krona.html

Question 1: In your README, briefly comment on the trends you see in the gut microbiota throughout the first week.

According to the data(from day 0 to day 8), we can see that gut is mostly dominated by E. faecalis during the first weel. Actinobacteria(mainly cutibacterium) disappears after first day of birth and return after 5day and continuely increase its proportion. Bacillales show a decrease after birth

# Step2

Question 2: In your README, comment on what metrics in the contigs could we use to group them together?


## 2A
bwa index assembly.fasta

## 2B
I used simialr command for all the files:
For example:
bwa mem -t 8 assembly.fasta SRR492193_1.fastq SRR492193_2.fastq | samtools sort -@8 -o SRR492193.bam


## 2C
cp ~/miniconda3/envs/metabat2/lib/libdeflate.so ~/miniconda3/envs/metabat2/lib/libdeflate.0.dylib

conda activate metabat2


## 2D

jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam
metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bins

### Question 3A: In your README, answer: How many bins did you get?
6 bins

### Question 3B: In your README, comment on roughly what percentage of the assembly do they represent?

using the pythoncode, I get the length for each bin file:

bin1: 2705023
bin2: 2251850
bin3: 1656034
bin4: 1227903
bin5: 2483660
bin6: 2862852

And the assembly file: 38071686

So the presentage for each file is:

bin1: 2705023/38071686=7.1%
bin2: 2251850/38071686=5.9%
bin3: 1656034/38071686=4.3%
bin4: 1227903/38071686=3.2%
bin5: 2483660/38071686=6.5%
bin6: 2862852/38071686=7.5%

### Question 3C: In your README, comment on whether you think the sizes of each bin look about right, based on what you know about the size of prokaryotic genomes?

I think the size of each bin looks about right since the size of prokaryotic genomes of about ~5000000

### Question 3D:In your README, describe how you might estimate how complete and how contaminated each bin is?

We can assess the quality of genome bins by identifing and counting universal single copy genes (SCGs).Completeness is the number of unique SCGs present within the bin / the number of unique SCGs in the list. Contamination is estimated by looking at how many SCGs are present in multiple copies, as only one copy should be present of each SCG per genome. 


# Step 3

I used my own python script to do this steps 

## Question 4(A)

Bin 1: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1

Bin 2: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis RP62A

Bin 3: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548

Bin 4: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435

Bin 5: root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067

Bin 6: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis OG1RF or V583

## Question 4(B)

I read some paper about binning methods. To improve the accurracy and the robusty, some paper suggest to do a fast approximation of evolutionary neighborhoods. 




 
