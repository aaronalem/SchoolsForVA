# from statistics import LinearRegression
import data_cleaning
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression


def regression_no_null(limited_columns=False): 
    school_data = data_cleaning.get_total_dataset()
    if limited_columns: 
        school_data = school_data.drop(['Dropouts', 'Students_in_the_Cohort', 'Cohort_Dropout_Rate', 'Diplomas', 'GEDs', 'Certificates_of_Completion', 'Still_Enrolled', 'Graduation_Completion_Index'], axis=1)
    school_data = school_data.dropna()
    school_data = school_data.drop(['Title_1_Code'], axis=1)
    y = school_data['SOL Pass Rate'].values
    df = school_data.drop(['School', 'Division', 'Sch_Div', 'SOL Pass Rate', 'Poverty_Level', 'Sch_Type', 'Street', 'City', 'State', 'Zip', 'Latitude', 'Longitude', 'English: Reading', 'English: Writing', 'History and Social Sciences', 'Mathematics', 'Science'], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)
    linear_model = LinearRegression()
    cv_scores = cross_val_score(linear_model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    mean_cv_mse = -np.mean(cv_scores)
    std_cv_mse = np.std(cv_scores)
    variance_y = np.var(y_train)
    r_squared = 1 - (mean_cv_mse / variance_y)
    print("Mean CV Accuracy: {:.2f}".format(mean_cv_mse))
    print("Standard Deviation: {:.2f}".format(std_cv_mse))
    print("R_squared: {:.2f}".format(r_squared))

'''
Main script to run the regression for the school data.
'''
def run_regression(): 
    print("----- WITH FULL COLUMNS, LESS SAMPLES -----")
    regression_no_null()
    print("\n")
    print("----- WITH LIMITED COLUMNS, MORE SAMPLES -----")
    regression_no_null(limited_columns=True)

if __name__ == "__main__": 
    run_regression()