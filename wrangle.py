# os, to see if a file exists
import os
# tabular data manipulation
import numpy as np
import pandas as pd
# train test split
from sklearn.model_selection import train_test_split

def acquire_student_grades():
    if os.path.exists('student_grades.csv'):
        return pd.read_csv('student_grades.csv')
    else:
        print('Good luck next time')
        return None
os.path.exists('student_grades.csv')

def clean_student_grades(df):
    '''
    takes in a single pandas dataframe with the expected formatting observed in student_grades
    It will remove the student id column
    It will remove any records containing null values
    and it will cast any floats into integers
    
    argument: df, a pandas DataFrame
    return: df, a pandas Dataframe (cleaned)
    '''
    
    # drop the student id column
    df = df.drop(columns='student_id')
    
    # drop the missing/null
    df = df.dropna()
    
    # cast the two series with floats into ints
    df = df.astype(int)
    return df

def split_my_students(df):
    '''
    Arguments: df, a single pandas dataframe
    Returns: train, validate, test - Three Pandas DataFrames
    '''
    
    train_val, test = train_test_split(df, 
                                       random_state=1423,
                                       train_size=0.7) # no stratify needed
    
    train, validate = train_test_split(train_val, 
                                       random_state=1423, 
                                       train_size=0.8)
    
    return train, validate, test
    
def wrangle_grades():
    '''
    wrangle goes through process of 
    acquiring students grades,
    clean students grades,
    and split students grades into
    train, validate and test pandas DataFrames
    '''
    return split_my_students(clean_student_grades(acquire_student_grades()))
    