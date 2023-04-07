import os
import pandas as pd
import numpy as np
from env import host, username, password
from scipy import stats
from sklearn.model_selection import train_test_split

#-----------------------------------------------------------

def get_connection(db, user=username, host=host, password=password):
    
    '''
    This function is to connect to the Codeup MySQL server, and by itself won't do anything. It works in conjunction with 
    the  other functions within this .py file.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#-----------------------------------------------------------

def get_telco_data():
    '''
    This function will check locally if there's a telco.csv file in the local directory, and if not, working with the 
    get_connection function, will pull the telco dataset from the Codeup MySQL server. After that, it will also save a copy of 
    the csv locally if there wasn't one, so it doesn't have to run the query each time.
    '''
    if os.path.isfile('telco.csv'):
        return pd.read_csv('telco.csv', index_col=0)
    else:
        url = get_connection('telco_churn')
        query = '''
                SELECT *
                FROM customers
                JOIN contract_types USING(contract_type_id)
                JOIN internet_service_types USING (internet_service_type_id)
                JOIN payment_types types USING(payment_type_id);
                '''
        telco = pd.read_sql(query, url)
        telco.to_csv('telco.csv')
        return telco
    
#-----------------------------------------------------------

def prep_telco_data():
    '''
    This function will use the above function to get the telco data, and then go through a series of commands to clean it up into
    something more useful. It will return the dataframe, as well as two lists, one of the categorical column names, and another of 
    the numerical columns(minus the target and the other numerical column we don't want to scale, gender).
    '''
    # Collects the dataframe
    df = get_telco_data()
    
    # Creating empty lists for numerical and categorical columns
    cat_cols = []
    num_cols = []
    
    # Changing all of the yes's and no's in the churn column to numerical values 
    df['churn'] = df['churn'].replace('Yes', 1)
    df['churn'] = df['churn'].replace('No', 0)
    # Setting the churn column to a numerical
    df['churn'] = df['churn'].astype(int)
    # Changing the senior citizen column to categorical
    df['senior_citizen'] = df['senior_citizen'].replace(0, 'No')
    df['senior_citizen'] = df['senior_citizen'].replace(1, 'Yes')
    
    # For if you want to payment types to be categorical
    df['payment_type'] = df['payment_type'].replace('Electronic check', 'manual')
    df['payment_type'] = df['payment_type'].replace('Mailed check', 'manual')
    df['payment_type'] = df['payment_type'].replace('Bank transfer (automatic)', 'auto')
    df['payment_type'] = df['payment_type'].replace('Credit card (automatic)', 'auto')
    
    # Setting all of the payments to 0 for manual payments and 1 for automatic payments
    #df['payment_type'] = df['payment_type'].replace('Electronic check', '0')
    #df['payment_type'] = df['payment_type'].replace('Mailed check', '0')
    #df['payment_type'] = df['payment_type'].replace('Bank transfer (automatic)', '1')
    #df['payment_type'] = df['payment_type'].replace('Credit card (automatic)', '1')
    # Making the column to a numerical dtype
    #df['payment_type'] = df['payment_type'].astype(int)
    
    # Changing the gender columns to numerical values
    df['gender'] = df['gender'].replace('Male', 1)
    df['gender'] = df['gender'].replace('Female', 0)
        
    # Dropping unneeded columns
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'])
    # Removing the rows where the total charges were blank
    # tenure was at 0, so I can only imagine customer canceled account before being charged
    df = df[df['total_charges'] != ' ']
    # Converting dtype to float
    df['total_charges'] = df['total_charges'].astype(float)

    # Loop to get numericl and categorical columns
    for col in df.columns:
    
        if df[col].dtypes == 'object':
            cat_cols.append(col)
        else:
            num_cols.append(col)
            
    # Removing churn and gender from the num_cols variable
    num_cols.remove('churn')
    num_cols.remove('gender')

    return df, cat_cols, num_cols
    

#-----------------------------------------------------------

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

#-----------------------------------------------------------
