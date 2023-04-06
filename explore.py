import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

import warnings
warnings.filterwarnings("ignore")

np.set_printoptions(suppress=True)

seed = 42

#------------------------------------------------------------

 def df_splits(df, col, val='Yes', strat='Yes', seed=42):
    '''
    This function takes in a dataframe and a taget column, as well as several optional arguments. You can decide if you want a validate set and if you want to stratify. 
    By leaving those two variables alone you will stratify on the target column and get a validate subset. If you change them to anything when calling the function,
    you will not get a validate or stratification. There is also an argument for the seed, which is set to 42 by default.
    '''
    # If val is left alone at 'Yes', the function will run this loop and return a validate subset.
    if val == 'Yes':
        # If strat is left alone at 'Yes', the function will stratify by the column named when calling the function.
        if strat == 'Yes':
            # Train, validate, and test subsets created.
            train, val_test = train_test_split(df, train_size=.6, random_state=seed, stratify=df[col])
            validate, test = train_test_split(val_test, train_size=.6, random_state=seed, stratify=val_test[col])
            # Printing the shapes of each subset 
            print(train.shape, validate.shape, test.shape)
            return train, validate, test
        # If the strat argument is changed at all, it will default to not doing it and not stratify when splitting.
        else:
            #Splitting the data into train, validate, and test.
            train, val_test = train_test_split(df, train_size=.6, random_state=seed)
            validate, test = train_test_split(val_test, train_size=.6, random_state=seed)
            # Again, printing the subset
            print(train.shape, validate.shape, test.shape)
            return train, validate, test
    # This part of the loop is for if you changed the val argument to something other than 'Yes', which will make it not create a validate subset. 
    else:
        # If strat is left at 'Yes', the function will stratify on the column named when calling the function
        if strat == 'Yes':
            # Splitting the data into train and test subsets
            train, test = train_test_split(df, train_size=.8, random_state=seed, stratify=df[col])
            # Printing the shapes
            print(train.shape, test.shape)
            return train, test

        else:
            # Splitting the data into train and test
            train, test = train_test_split(df, train_size=.8, random_state=seed)
            # Printing the shapes
            print(train.shape, test.shape)
            return train, test
        
#------------------------------------------------------------

def mannwhitney_report(group1, group2):
    '''
    This function takes in two groups (columns), and will perform a mannwhitneyu test on them and print out 
    the test statistic and p-value, as well as determine if the p-value is lower than a predetermined (.05) alpha
    '''
    t, p = stats.mannwhitneyu(group1, group2)

    alpha = .05
    seed = 42

    print(f'T-Statistic = {t:.4f}') 
    print(f'p-value     = {p}')

    print('Is p-value < alpha? - ', p < alpha)
    
#------------------------------------------------------------

def ind_ttest_report(group1, group2):
    '''
    This function takes in two groups (columns), and will perform an independent t-test on them and print out 
    the t-statistic and p-value, as well as determine if the p-value is lower than a predetermined (.05) alpha
    '''
    t, p = stats.ttest_ind(group1, group2, equal_var=False)

    alpha = .05
    seed = 42

    print(f'T-statistic = {t:.4f}') 
    print(f'p-value     = {p}')

    print('Is p-value < alpha? - ', p < alpha)
    
#------------------------------------------------------------

def pearsonr_report(group1, group2):
    '''
    This function takes in two groups (columns), and will perform a pearsonr test on them and print out 
    the test statistic and p-value, as well as determine if the p-value is lower than a predetermined (.05) alpha
    '''
    corr, p = stats.pearsonr(group1, group2)

    alpha = .05
    seed = 42

    print(f'Correlation = {corr:.4f}') 
    print(f'p-value     = {p}')
    print('Is p-value < alpha? - ', p < alpha)
    
#------------------------------------------------------------

def spearmanr_report(group1, group2):
    '''
    This function takes in two groups (columns), and will perform a spearman r test on them and print out 
    the test statistic and p-value, as well as determine if the p-value is lower than a predetermined (.05) alpha
    '''
    corr, p = stats.spearmanr(group1, group2)

    alpha = .05
    seed = 42

    print(f'Correlation = {corr:.4f}') 
    print(f'p-value     = {p}')
    print('Is p-value < alpha? - ', p < alpha)
    
#------------------------------------------------------------

def chi2_report(df, col, target):
    '''
    This function is to be used to generate a crosstab for my observed data, and use that the run a chi2 test, and generate the report values from the test.
    '''
    alpha = .05
    seed = 42
    
    observed = pd.crosstab(df[col], df[target])
    
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    print('Observed Values\n')
    print(observed.values)
    print('-----------------------')
    print('---\nExpected Values\n')
    print(expected.astype(int))
    print('---\n')
    print('-----------------------')
    print(f'chi^2 = {chi2:.4f}') 
    print(f'p     = {p}')
    print('Is p-value < alpha?', p < alpha)
    
#------------------------------------------------------------

def chi_simple(group1, group2):
    
    alpha = .05
    seed = 42
    
    observed = pd.crosstab(group1, group2)
    
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    print(f'chi^2 = {chi2:.4f}')
    print(f'p.    = {p}')
    print('Is p-value < alpha? - ', p < alpha)

#------------------------------------------------------------

def anova_report(group1, group2, group3, group4, group5):
    '''
    This function takes in multiple groups (columns), and will perform an ANOVA test on them and print out 
    the f statistic and p-value, as well as determine if the p-value is lower than a predetermined (.05) alpha
    '''
    f, p = stats.f_oneway(group1, group2, group3, group4, group5)
    alpha = .05
    seed = 42

    print(f'f-statistic = {f:.4f}') 
    print(f'p-value     = {p}')
    print('Is p-value < alpha? - ', p < alpha)
    
#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------
