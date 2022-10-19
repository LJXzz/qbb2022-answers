# Week 1 Genome Assembly -- Feedback

1 + 0.5 + 0.5 + 1 + 0.75 + 1 + 1 + 1 + 1 + 1 = 8.75 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * good --> +1

2. Question 1.2, 1.4 simulation script(s)

  * given that Python has 0-based indexing, I would recommend that you use 0 to 999901 rather than the 1 and 999901 in your code `start = np.random.randint(1, 999901, size = 150000)`. This current code doesn't allow for you ever have a read on the first genomic loci.
  * your code is setup for 15x coverage simulation, but not 5x --> +0.5


3. Question 1.2, 1.4 plotting script(s)
  * overall, very good.
  * Also only set up for 15x coverage
  * Rather than using `density = True` within the `hist` function, you needed to fit/overlay specifically a poisson curve. You could use the scipy `stats.poisson.pmf` function, together with `plt.plot` to accomplish this. That way you're fitting a specific Poisson function with a known `mu` or `lambda`.
  * --> +0.5

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * good plots --> +1

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * Are those the frequency or probability of a location having 0 read coverage?
  * --> +0.75

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size --> +0.5

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> +0.33

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.5
  * length of novel insertion --> +0.5

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.5
  * secret message --> +0.5
