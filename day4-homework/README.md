
## A
- The output with the required tosses and probs is as follows: (the first column is prob, the second is toss, and the third is the output from function "run_exerpiment()")
	1.0 10 1.0
	1.0 50 1.0
	1.0 100 1.0
	1.0 250 1.0
	1.0 500 1.0
	1.0 1000 1.0
	0.95 10 1.0
	0.95 50 1.0
	0.95 100 1.0
	0.95 250 1.0
	0.95 500 1.0
	0.95 1000 1.0
	0.9 10 1.0
	0.9 50 1.0
	0.9 100 1.0
	0.9 250 1.0
	0.9 500 1.0
	0.9 1000 1.0
	0.85 10 0.6
	0.85 50 1.0
	0.85 100 1.0
	0.85 250 1.0
	0.85 500 1.0
	0.85 1000 1.0
	0.8 10 0.4
	0.8 50 1.0
	0.8 100 1.0
	0.8 250 1.0
	0.8 500 1.0
	0.8 1000 1.0
	0.75 10 0.4
	0.75 50 1.0
	0.75 100 1.0
	0.75 250 1.0
	0.75 500 1.0
	0.75 1000 1.0
	0.7 10 0.0
	0.7 50 1.0
	0.7 100 1.0
	0.7 250 1.0
	0.7 500 1.0
	0.7 1000 1.0
	0.65 10 0.0
	0.65 50 0.6
	0.65 100 1.0
	0.65 250 1.0
	0.65 500 1.0
	0.65 1000 1.0
	0.6 10 0.0
	0.6 50 0.2
	0.6 100 0.8
	0.6 250 1.0
	0.6 500 1.0
	0.6 1000 1.0
	0.55 10 0.0
	0.55 50 0.2
	0.55 100 0.2
	0.55 250 0.8
	0.55 500 0.8
	0.55 1000 1.0
- numpy.arange(0.55, 1.05, 0.05) : 0.55 is the starting value for this array, 1.05 is the end values(but it will not be included in the array), 0.05 is the spacing value.
  The output from print(numpy.arange(0.55, 1.05, 0.05)) is 
  [0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]
- numpy.around( ,decimals=2): numpy.around is used to creates an array with uniformly distributed values ​​in the specified interval, deciamls is used to show how many deciamls we should keep for every element after approximation in the array.
  The output is: [0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]
  We may want to use numpy.arrange when we want to round an array of floats to a given number of decimals
- With [::-1], the output becomes: [1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55], which means [::-1] is actually a way to reverse the array.


## B
The power matrix is 
 [1.   1.   1.   1.   1.   1.  ]
 [0.93 1.   1.   1.   1.   1.  ]
 [0.78 1.   1.   1.   1.   1.  ]
 [0.6  1.   1.   1.   1.   1.  ]
 [0.42 1.   1.   1.   1.   1.  ]
 [0.3  0.95 1.   1.   1.   1.  ]
 [0.2  0.86 0.96 1.   1.   1.  ]
 [0.14 0.53 0.85 0.99 1.   1.  ]
 [0.06 0.26 0.48 0.91 0.99 1.  ]
 [0.01 0.05 0.12 0.32 0.57 0.87]
 
 
 
## C

- As the probability or number of toss parameters, the power will continue to increase, which means that as the number of coin tosses in each experiment increases or the coin is more unfair, the results we see will be closer to the theoretical results, which means we reject more fales test.

## D

- This paper focuses on  “transmission distortion” (TD), a phenomenon that “selfish” alleles disproportionately transmitted to the next generation regardless of Mendel’s Law of Segregation.


- Both the simulation experiment heatmap performed for Figure S13 shows high power with more samples. The difference is that when we do multiple testing correction in simulation, the higher threshold results in higher confidence level with lower samples. 

- prob_heads corresponds to the transmission rate axis.

- number of tosses corresponds to the Number of sperm axis

- The binomial test is used when an experiment has two possible outcomes and we have an idea about what the probability of success is. We want to see if observed test results differ from what was expected. For both simulations, we all only have two possible outcomes and we are trying to compare if the true data(given data) fits a specific laws or rules. 
  
