import pandas as pd

#--------------------------------------------

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

#--------------------------------------------

def train_test(df, col, strat='Yes', seed=42):
    '''
    This function will split the data into a large train set, putting the rest into the test set. The reason you would use this over a 
    train, validate, and test split is for the purpose of using cross-validation. This function takes in a dataframe,
    a specific column that you're stratifying on, and a seed, which the default is set to 42. This function also takes the 
    optional argument for if you want to stratify at all, with it defaulting to yes.
    '''
    if strat == 'Yes':
        
        train, test = train_test_split(df, train_size=.8, random_state=seed, stratify=df[col])
    
        return train, test

    else:
        
        train, test = train_test_split(df, train_size=.8, random_state=seed)
        
        return train, test

#--------------------------------------------



#--------------------------------------------



#--------------------------------------------



#--------------------------------------------



#--------------------------------------------
