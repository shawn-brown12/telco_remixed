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
    the numerical columns.
    '''
    # Collects the dataframe
    df = get_telco_data()
    
    # Creating empty lists for numerical and categorical columns
    cat_cols = []
    num_cols = []
    
    # Changing all of the yes's and no's to numerical values 
    df = df.replace('Yes', 1)
    df = df.replace('No', 0)
    
    # For if you want to payment types to be categorical
    # df['payment_type'] = df['payment_type'].replace('Electronic check', 'manual')
    # df['payment_type'] = df['payment_type'].replace('Mailed check', 'manual')
    # df['payment_type'] = df['payment_type'].replace('Bank transfer (automatic)', 'auto')
    # df['payment_type'] = df['payment_type'].replace('Credit card (automatic)', 'auto')
    
    # Setting all of the payments to 0 for manual payments and 1 for automatic payments
    df['payment_type'] = df['payment_type'].replace('Electronic check', '0')
    df['payment_type'] = df['payment_type'].replace('Mailed check', '0')
    df['payment_type'] = df['payment_type'].replace('Bank transfer (automatic)', '1')
    df['payment_type'] = df['payment_type'].replace('Credit card (automatic)', '1')
    # Changing the gender columns to numerical values
    df['gender'] = df['gender'].replace('Male', 1)
    df['gender'] = df['gender'].replace('Female', 0)
    # Making the column to a numerical dtype
    df['payment_type'] = df['payment_type'].astype(int)
    # Setting the churn column to a numerical
    df['churn'] = df['churn'].astype(int)
        
    # Dropping unneeded columns
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'])
    # Removing the rows where the total charges were blank
    # tenure was at 0, so I can only imagine customer canceled account before being charged
    df = df[df['total_charges'] != ' ']
    # Converting dtype to float
    df['total_charges'] = df['total_charges'].astype(float)
    
    # Changing back the 1s and 0s in the categorical columns to yes's and no's
    for col in df.columns:
    if df[col].dtypes == 'object':
        df[col] = df[col].replace(1, 'Yes')
        df[col] = df[col].replace(0, 'No')

    # Loop to get numericl and categorical columns
    for col in df.columns:
    
        if df[col].dtypes == 'object':
            cat_cols.append(col)
        else:
            num_cols.append(col)
            
    return df, cat_cols, num_cols
    

#-----------------------------------------------------------

def split_train_test(df, col, seed=42):
    '''
    This function will split a dataset into train, validate, and test variables to model with. Make sure to assign to three 
    variables when running.
    '''
    train, val_test = train_test_split(df, train_size=.6, random_state=seed, stratify=df[col])
    validate, test = train_test_split(val_test, train_size=.6, random_state=seed, stratify=val_test[col])
    
    return train, validate, test

#-----------------------------------------------------------
