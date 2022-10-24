# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 1 + 0.5 + 1 + 1 + 1 + 1 + 1 = 9.5 points out of 10 possible points

1. Index genome

  * --> +1

2. align reads

  * great for loop; --> +1

3. sort bam files and index sorted bam files (0.5 points each)

  * consider using a single for loop for questions 2 and 3 --> +1

4. variant call with freebayes

  * perfect! --> +1

5. filter variants

  * I see what you're going for here, but you want to use `QUAL > 20` as your filter criteria. [A PHRED score of 20 corresponds to a base call accuracy of 99%](https://en.wikipedia.org/wiki/Phred_quality_score)
  * --> +0.5

6. decompose complex haplotypes

  * great --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * good script and great comments! --> +1

9. 4 panel plot (0.25 points each panel)

  * good plot overall, but the text size is a little too small. Here are some examples in a [stackoverflow post](https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot) on how to increase the font size.
  * --> +1

10. 1000 line vcf

  * --> +1
