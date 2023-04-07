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



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------
    
def Xy_validate(validate, target):
    '''
    This function will take in a validate df and target column from that df and create X and y subsets.
    '''  
    # Creating the validate subsets 
    X_val = validate.drop(columns=target)
    y_val = validate[target]
 
    # Resetting indexes
    X_val = X_val.reset_index(drop= True)
    y_val = y_val.reset_index(drop= True)
        
    return X_val, y_val
    
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

def create_dummies(df, cols):
    '''
    This function will, quite simply, create dummy variables for a dataframe, remove the columns used to create them, 
    and then concat the dummies back onto the dataframe
    '''
    # This will create the dummy variables from our categorical columns list
    dummies = pd.get_dummies(df[cols], drop_first=True)
    # This will drop the original categorical columns from the df
    df = df.drop(columns=cols)
    # This will concatenate the dummies onto the current df
    df = pd.concat([df, dummies], axis=1)
            
    return df

#------------------------------------------------------------

def Xy_validate(validate, target):
    '''
    This function will take in a validate df and target column from that df and create X and y subsets.
    '''  
    # Creating the validate subsets 
    X_val = validate.drop(columns=target)
    y_val = validate[target]
 
    # Resetting indexes
    X_val = X_val.reset_index(drop= True)
    y_val = y_val.reset_index(drop= True)
        
    return X_val, y_val

#------------------------------------------------------------

def Xy_train_test(train, test, target):
    '''
    This function will take in a train and test df as well as the target column for each and create X and y subsets.
    '''
    # creating train and test (x and y) subsets
    X_train = train.drop(columns= target)
    y_train = train[target]
        
    # creating train and test (x and y) subsets
    X_test = test.drop(columns= target)
    y_test = test[target]
    
    # Resetting indexes
    X_train = X_train.reset_index(drop= True)
    y_train = y_train.reset_index(drop= True)
    X_test = X_test.reset_index(drop= True)
    y_test = y_test.reset_index(drop= True)
        
    return X_train, y_train, X_test, y_test

#------------------------------------------------------------

def subsets(train, test, validate, target):
    '''
    This function will call the two functions to create validate subsets and the train/test subsets in one 
    to streamline the creation of all three subsets at once.
    '''
    X_val, y_val = Xy_validate(validate, target)
    
    X_train, y_train, X_test, y_test = Xy_train_test(train, test, target)
    
    return X_train, y_train, X_val, y_val, X_test, y_test

#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------
