# Logistic Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


def logistic_regression(loan_amount, interest_rate, emp_length, annual_inc, dti, delinq_2yrs, revol_util, total_acc, longest_credit_length):
    
    # Importing the dataset
    dataset = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),'loan_data.csv'))
    #dataset = pd.read_csv('NewData.csv')
    
    #to check dataset for any empty entries (if all false then OK)
    dataset.isnull().any()
    dataset = dataset.fillna(method='ffill')
    
    #to format all numeric values upto two decimal points
    pd.options.display.float_format = '{:,.2f}'.format
    dataset.describe()
    
    X = dataset.iloc[:, [0, 2, 3, 5, 7, 8, 9, 10, 12]].values
    
    
    #X = dataset.iloc[:, range(1, 12)].values
    #y = dataset.iloc[:, 4].values
    y = dataset.iloc[:, 11].values
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    
    
    test_input = np.array([[loan_amount, interest_rate, emp_length, annual_inc, dti, delinq_2yrs, revol_util, total_acc, longest_credit_length]])
    
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    #X_test = sc.transform(X_test)
    
    X_test = sc.transform(test_input)
    
    # Fitting Logistic Regression to the Training set
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state = 0)
    classifier.fit(X_train, y_train)
    
    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    return y_pred[0]
