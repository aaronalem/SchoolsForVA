import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

'''
Using K means to group school performance based on test pass rates, teacher experience,
and level of education teachers have had

'''

# preprocess the data
school = pd.read_excel('test.xlsx')
school_tr = school[
    ['SOL Pass Rate', 'English: Reading', 'History and Social Sciences', 'Mathematics', 'Science',
     'Chronic_Absenteeism_Rate','Dropouts', 'Graduation_Completion_Index', 'End_of_Year_Average_Daily_Membership',
     'Percent_of_Inexperienced_Teachers', 'Percent_of_Out_of_Field_Teachers',
     'Percent_of_Out_of_Field_and_Inexperienced_Teachers', 'Bachelor_Degree_Percent',
     'Master_Degree_Percent', 'Doctoral_Degree_Percent']].dropna()

school_tr = school_tr[school_tr['History and Social Sciences'] != '<']
school_tr = school_tr[school_tr['Science'] != '<']
school_tr['Dropout_Rate'] = (school_tr['Dropouts']/school_tr['End_of_Year_Average_Daily_Membership'])*100

# Drop unneeded columns
school_tr = school_tr.drop('Dropouts', axis=1)

# Set up pipeline
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median"))
])

# scale outside the pipeline so I can unscale the data later on
scalar = StandardScaler()

school_scaled = scalar.fit_transform(school_tr)

# Set up Data set
X_train = num_pipeline.fit_transform(school_scaled)

# Using K means
print('sse: ')
# two centroids
k2 = KMeans(n_clusters=2, random_state=0, n_init="auto")
k2.fit(X_train)
sse2 = k2.inertia_
print('2 clusters:', sse2)

# three centroids
k3 = KMeans(n_clusters=3, random_state=0, n_init="auto")
k3.fit(X_train)
sse3 = k3.inertia_
print('3 clusters:', sse3)

# four centroids
k4 = KMeans(n_clusters=4, random_state=0, n_init="auto")
k4.fit(X_train)
sse4 = k4.inertia_
print('4 clusters:', sse4)

# five centroids
k5 = KMeans(n_clusters=5, random_state=0, n_init="auto")
k5.fit(X_train)
sse5 = k5.inertia_
print('5 clusters:', sse5)

# six centroids
k6 = KMeans(n_clusters=6, random_state=0, n_init="auto")
k6.fit(X_train)
sse6 = k6.inertia_
print('6 clusters:', sse6)

# seven centroids
k7 = KMeans(n_clusters=7, random_state=0, n_init="auto")
k7.fit(X_train)
sse7 = k7.inertia_
print('7 clusters:', sse7)

# eight centroids
k8 = KMeans(n_clusters=8, random_state=0, n_init="auto")
k8.fit(X_train)
sse8 = k8.inertia_
print('8 clusters:', sse8)

# nine centroids
k9 = KMeans(n_clusters=9, random_state=0, n_init="auto")
k9.fit(X_train)
sse9 = k9.inertia_
print('9 clusters:', sse9)

# ten centroids
k10 = KMeans(n_clusters=10, random_state=0, n_init="auto")
k10.fit(X_train)
sse10 = k10.inertia_
print('10 clusters:', sse10, '\n\n')


print('stats per centroid for 7 clusters:\n')

features = ['SOL Pass Rate', 'English: Reading', 'History and Social Sciences', 'Mathematics', 'Science',
            'Chronic_Absenteeism_Rate', 'Graduation_Completion_Index',
            'End_Of_Year_Average_Daily_Membership', 'Percent_of_Inexperienced_Teachers',
            'Percent_of_Out_of_Field_Teachers', 'Percent_of_Out_of_Field_and_Inexperienced_Teachers',
            'Bachelor_Degree_Percent', 'Master_Degree_Percent', 'Doctoral_Degree_Percent', 'Dropout_Rate']

for i in range(len(scalar.inverse_transform(k7.cluster_centers_))):
    for j in range(len(scalar.inverse_transform(k7.cluster_centers_)[0])):
        print(features[j], ': ', scalar.inverse_transform(k7.cluster_centers_)[i][j])
    print('\n')

# Plot
y = scalar.inverse_transform(X_train)
y_xaxis = (y[:, 14])
y_yaxis = y[:, 5]
fig, (ax6) = plt.subplots(1, 1, figsize=(12, 12))
fig.supxlabel("Dropout Rate")
fig.supylabel("Chronic Absenteeism Rate")
fig.suptitle("Virginia High Schools Dropout Rate vs Absenteeism Rate")


colors6 = ['blue', 'red', 'green', 'grey', 'orange', 'brown']
ax6.scatter(y_xaxis, y_yaxis, c=k6.labels_, cmap=matplotlib.colors.ListedColormap(colors6), alpha=0.8)
ax6.set_xlim([0, 6])
plt.show()

