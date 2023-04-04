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




#--------------------------------------------




#--------------------------------------------




#--------------------------------------------




#--------------------------------------------




#--------------------------------------------




#--------------------------------------------
