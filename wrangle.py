import os
import pandas as pd
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
        return pd.read_csv('telco.csv')
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

def prep_telco(df):
    '''
    This function will prepare the telco_churn dataset for further use. It will convert the total_charges column into the float 
    data type, create various dummies and concatenate those dummies, and then drop unneeded columns.
    '''
    df['total_charges'] = df['total_charges'].replace(' ', '0')
    df['total_charges'] = df['total_charges'].astype(float)
    #df['churn'] = df['churn'].astype(int)
    
    to_dummy = ['churn', 'gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 
                'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
                'paperless_billing', 'contract_type', 'internet_service_type', 
                'payment_type']
    dummies = pd.get_dummies(df[to_dummy], drop_first=False)
    df = pd.concat([df, dummies], axis=1)
    
    drop = ['multiple_lines_No phone service', 'online_security_No internet service',
        'online_backup_No internet service', 'device_protection_No internet service',
        'tech_support_No internet service', 'streaming_tv_No internet service',
        'streaming_movies_No internet service', 'gender_Female', 'partner_No',
        'dependents_No', 'phone_service_No', 'multiple_lines_No',           'online_security_No', 'online_backup_No',
        'device_protection_No', 'tech_support_No', 'streaming_tv_No',
        'streaming_movies_No', 'paperless_billing_No', 'gender', 'partner', 
        'dependents', 'phone_service', 'multiple_lines', 'online_security', 
        'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
        'paperless_billing', 'payment_type', 'Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 
        'contract_type_id', 'churn', 'churn_No']
    df.drop(columns=drop, inplace=True)
                 
    return df

#-----------------------------------------------------------
    
def prep_telco(df):
    '''
    This function will prepare the telco_churn dataset for further use. It will convert the total_charges column into the float 
    data type, create various dummies and concatenate those dummies, and then drop unneeded columns.
    '''
    telco['total_charges'] = telco['total_charges'].replace(' ', '0')
    telco['total_charges'] = telco['total_charges'].astype(float)
    
    to_dummy = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 
                'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
                'paperless_billing', 'contract_type', 'internet_service_type', 
                'payment_type']
    dummies = pd.get_dummies(df[to_dummy], drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    
    drop = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 
                'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
                'paperless_billing', 'contract_type', 'internet_service_type', 
                'payment_type', 'Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
    df.drop(columns=drop, inplace=True)
                 
    return df

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

def chi2_report(df, col, target):
    '''
    This function is to be used to generate a crosstab for my observed data, and use that the run a chi2 test, and generate the report values from the test
    '''
    
    observed = pd.crosstab(df[col], df[target])
    
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    alpha = .05
    seed = 42
    
    print('Observed Values\n')
    print(observed.values)
    
    print('---\nExpected Values\n')
    print(expected.astype(int))
    print('---\n')

    print(f'chi^2 = {chi2:.4f}') 
    print(f'p     = {p:.4f}')

    print('Is p-value < alpha?', p < alpha)
    