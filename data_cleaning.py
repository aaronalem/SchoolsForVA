'''
Script for data collection and cleaning for use in other scripts
'''

import pandas as pd
import os
from math import floor

DATASET_DIR = 'Dataset'

'''
Simple helper function to load csv file from the dataset folder.
'''
def load_csv(folder: str, file: str): 
    path = os.path.join(DATASET_DIR, folder, file)
    return pd.read_csv(path)

'''
Helper function to get the teachers education file and process it to fit with other files.
'''
def process_teachers_education(folder: str, file: str): 
    education_teachers = load_csv(folder, file)
    cols = {'School': [], 'Division': [], 'Bachelor_Degree_Percent': [], 'Master_Degree_Percent': [], 'Doctoral_Degree_Percent': [], 'Sch_Div': []}
    new_pd = pd.DataFrame(cols)
    for i in range(education_teachers.shape[0]): 
        if i % 3 == 0: 
            new_pd.loc[floor(i / 3)] = [education_teachers.at[i, 'School'], education_teachers.at[i, 'Division'], education_teachers.at[i, 'Degree_Percent'], education_teachers.at[i+1, 'Degree_Percent'], education_teachers.at[i+2, 'Degree_Percent'], education_teachers.at[i, 'Sch_Div']]
    return new_pd


'''
Return a Pandas DataFrame with each row corresponding to a school and as many factors as possible included. 
NOTE: this uses an outer join, so there will be one row for each school; however, the fields may be null if data doesn't exist for that school. 
This is the case for dropout rates as only 314 of the ~1700 schools have data on dropout rates, so for the other schools the data is null. 
This means you need to decide how to use the data afterwards (e.g. leave out the dropout rates). 
'''
def get_total_dataset(): 
    demographics_path = 'Demographics'
    economics_path = 'Economic Factors'
    behavior_path = 'Student Behaviors'
    teachers_path = 'Teachers'
    testing_path = 'Testing'
    funding = load_csv(economics_path, 'Funding.csv')
    free_lunches = load_csv(economics_path, 'Free_and_Reduced_Lunch.csv')
    absenteeism = load_csv(behavior_path, 'Absenteeism.csv')
    dropout = load_csv(behavior_path, 'Dropout.csv')
    graduation = load_csv(behavior_path, 'Graduation.csv')
    licensure_teachers = load_csv(teachers_path, 'Licensure.csv')
    experience_teachers = load_csv(teachers_path, 'Experience.csv')
    education_teachers = process_teachers_education(teachers_path, 'Education_Level.csv')
    sols = load_csv(testing_path, 'SOL_Pass_Rate.csv').drop('Division', axis=1) # division for this one is not the same as the other dataframes
    addresses = load_csv('', 'School Addresses.csv').rename(columns={'Sch_div': 'Sch_Div'}) # change name of column to 'Sch_Div' to match with the rest of the data

    # adding the data from 'school-by-subject-2022'
    sbs = pd.read_excel(os.path.join(DATASET_DIR, 'Testing', 'school-by-subject-2022.xlsx')).drop(
        ['Level', 'Div Num', 'Div Name', 'Sch Num', 'Sch Type', 'Low Grade', 'High Grade'], axis=1).rename(columns={'Sch Name': 'School'})
    sbs = sbs[sbs['Subgroup'] == 'All Students']

    sbs = sbs.pivot_table(index='School', columns='Subject',
                          values='2021-2022 Pass Rate', aggfunc='first').reset_index()

    # add more sheets if desired

    df_list = [funding, free_lunches, absenteeism, dropout, graduation, licensure_teachers, experience_teachers, education_teachers, sols, addresses, sbs]
    total_df = funding
    for df in df_list[1:]: 
        total_df = pd.merge(total_df, df, how='outer')
    total_df['Title1_Code'] = total_df['Title1_Code'].map({'Title I': True, 'Non-Title I': False})
    # total_df.to_excel('test.xlsx')

    return total_df

get_total_dataset()