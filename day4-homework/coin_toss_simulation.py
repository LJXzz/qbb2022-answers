#!/usr/bin/env python


import numpy
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt
import seaborn as sns

def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads])
    return (results_arr)
    
#print(numpy.sum(simulate_coin_toss(10)))
#print(numpy.sum(simulate_coin_toss(10,seed=4)))

#hypo test
def perform_hypothesis_test(n_heads, n_tosses):
    binom_result = binomtest(n_heads, n_tosses)
    pval = binom_result.pvalue #grabbing the pvalue attribute from the binom_result instance
    return(pval)
    
#print(perform_hypothesis_test(2,5))

def correct_pvalues(pvals): 
    correct_pvalues = multipletests(pvals, method='bonferroni')
    return(correct_pvalues[1])
    

#print(correct_pvalues([0.005, 0.04, 0.03,0.003,0.000001]))
    
#
def interpret_pvalues(pvals):
    interpreted = numpy.array(pvals) < 0.05  #check evrey pvals in the array
    return(interpreted) # an arry of true and false

#print(interpret_pvalues([0.06,0.5,0.05,0.03]))


def compute_power(n_rejected_correctly, n_tests):
    power = n_rejected_correctly / n_tests
    return(power)


def run_experiment(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):
    numpy.random.seed(seed)  #n-iters是做了多少次实验，n_toss是每一次扔多少次
    pvals=[]
    for i in range(n_iters):
        results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
        n_success = numpy.sum(results_arr)
        pvals.append(perform_hypothesis_test(n_success, n_toss))
    if correct_the_pvalues:
        pvals = correct_pvalues(pvals)
    pvals_translated_to_bools = interpret_pvalues(pvals)
    power = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
    #power_arr = numpy.zeros((len(prob_heads), len(n_toss)))  
    #for i, prob in enumerate(prob_heads):
        #for j,toss in enumerate(n_toss):
            #power_arr[i,j] = prob + toss  #用这样的方法储存array，没有实际意义
    return(power)

probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
tosses = numpy.array([10, 50, 100, 250, 500, 1000])

power_arr = numpy.zeros((len(probs), len(tosses)))
for i in range(len(probs)):
    for j in range(len(tosses)):
        power=run_experiment(probs[i],tosses[j], correct_the_pvalues = True )
        #for a, prob in enumerate(probs):
            #for b,toss in enumerate(tosses):
        power_arr[i,j] =power  
#print(power_arr)

fig, ax = plt.subplots()
xticklabels = tosses
yticklabels = probs
ax = sns.heatmap(power_arr,vmin=0, vmax=1, xticklabels = xticklabels, yticklabels=yticklabels)
plt.xlabel('num of tosses')
plt.ylabel('possibilities')
plt.show()

#power1 = run_experiment(0.6, 500)
#power2 = run_experiment(0.95, 10, correct_the_pvalues = True)
#print(power1)
#print(power2)



        
        
        
        
        
        

    