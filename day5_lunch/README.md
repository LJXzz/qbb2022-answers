
# Exercise 1

For each prohand， the number of de novo mutations is:
proband ID   num of mutation 
86863 82
78675 57
86868 51
35677 76
7017 77
70509 62
11120 82
50034 82
117628 45
99197 48
58242 74
93058 71
13191 111
15247 77
119700 60
45976 65
136092 75
37789 34
93086 49
64417 41
119719 87
111528 58
62377 56
33711 59
146353 96
154565 75
46025 52
48073 72
9165 64
101332 88
72669 58
29678 38
109551 55
123888 70
5116 61
154621 50
148486 70
80905 97
33816 58
109597 85
56354 62
146476 70
93229 57
136238 67
87089 87


# Exercise 2

## 3.
      
      OLS Regression Results                            
      ==============================================================================
      Dep. Variable:               num_of_M   R-squared:                       0.680
      Model:                            OLS   Adj. R-squared:                  0.680
      Method:                 Least Squares   F-statistic:                     838.5
      Date:                Wed, 07 Sep 2022   Prob (F-statistic):           1.31e-99
      Time:                        20:08:15   Log-Likelihood:                -1076.0
      No. Observations:                 396   AIC:                             2156.
      Df Residuals:                     394   BIC:                             2164.
      Df Model:                           1                                         
      Covariance Type:            nonrobust                                         
      ==============================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
      ------------------------------------------------------------------------------
      Intercept      6.5044      0.739      8.805      0.000       5.052       7.957
      M_age          0.6726      0.023     28.956      0.000       0.627       0.718
      ==============================================================================
      Omnibus:                        5.107   Durbin-Watson:                   1.863
      Prob(Omnibus):                  0.078   Jarque-Bera (JB):                6.859
      Skew:                          -0.028   Prob(JB):                       0.0324
      Kurtosis:                       3.642   Cond. No.                         127.
      ==============================================================================

According to the output P, the relationship between maternal age and maternally inherited de novo mutations is significant.

The size fits the equation: 
0.6726 * Mother age + 6.5044 = maternally inherited de novo mutations

## 4.

     OLS Regression Results                            
    ==============================================================================
    Dep. Variable:               num_of_F   R-squared:                       0.680
    Model:                            OLS   Adj. R-squared:                  0.680
    Method:                 Least Squares   F-statistic:                     838.5
    Date:                Wed, 07 Sep 2022   Prob (F-statistic):           1.31e-99
    Time:                        20:06:30   Log-Likelihood:                -1156.8
    No. Observations:                 396   AIC:                             2318.
    Df Residuals:                     394   BIC:                             2325.
    Df Model:                           1                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept      3.2654      0.977      3.342      0.001       1.344       5.187
    F_age          1.0114      0.035     28.956      0.000       0.943       1.080
    ==============================================================================
    Omnibus:                       34.162   Durbin-Watson:                   1.890
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               52.805
    Skew:                           0.584   Prob(JB):                     3.42e-12
    Kurtosis:                       4.354   Cond. No.                         121.
    ==============================================================================


According to the output P, the relationship between paternal age and paternally inherited de novo mutation is significant 

The size fits the equation: 
1.0114 * paternal age + 3.2654 = paternally inherited de novo mutation

## 6.

     OLS Regression Results                            
    ==============================================================================
    Dep. Variable:               num_of_F   R-squared:                       0.143
    Model:                            OLS   Adj. R-squared:                  0.141
    Method:                 Least Squares   F-statistic:                     65.71
    Date:                Wed, 07 Sep 2022   Prob (F-statistic):           6.66e-15
    Time:                        20:12:44   Log-Likelihood:                -1567.0
    No. Observations:                 396   AIC:                             3138.
    Df Residuals:                     394   BIC:                             3146.
    Df Model:                           1                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept     39.1337      1.712     22.855      0.000      35.767      42.500
    num_of_M       1.0079      0.124      8.106      0.000       0.763       1.252
    ==============================================================================
    Omnibus:                       34.430   Durbin-Watson:                   2.005
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               47.747
    Skew:                           0.633   Prob(JB):                     4.28e-11
    Kurtosis:                       4.137   Cond. No.                         37.1
    ==============================================================================

According to the output P, the relationship is significant 


## 7.
50.5 * 1.0114 + 3.2654 = 54
