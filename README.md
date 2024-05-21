# Introduction/Motivation
Our main objective is to gain a deep understanding of the factors and methods that
generate high graduation rates, test scores, and low absenteeism in Virginia Public
School systems. Education is generally viewed as one of the most important institutions
for creating a prosperous, safe, and healthy society.
Specifically, there is a strong correlation between education and income. The
difference in average income between those with a high school education and those
without is nearly $10,000, and the difference between those with a college degree and
those without a high school education is nearly $50, 000 (Northeastern University),
showing the prosperity that education brings. There is a strong negative correlation
between education and crime, with a 1 year increase in education on average reducing
an individual’s likelihood of committing a violent crime by nearly 30% (Justice Policy
Institute), showing how a more educated society creates a more safe society. Finally,
there is a strong correlation between education and lifespan, where finishing a high
school education on average increases life expectancy by 8.3 years compared to not
finishing high school (Grand Valley State University). These facts clearly justify the
importance of education in increasing general quality of life in Virginia.
By understanding what creates better circumstances for students to learn, we can
propose solutions that will lead to better academics in Virginia and improve the quality
of life in the state overall. The specific setting we are considering is the Virginia Public
School system, as we live in Virginia and thus are uniquely concerned with the
economic, safety, and overall quality of life outcomes that are produced from a strong
public school system. The relationships that we discover among the various factors may
be different for other states, but that’s not what we’re concerned with, which is why we
are using Virginia schools’ data.


# Method and Data
### Data
We are making use of a Kaggle dataset on Virginia Public Schools. This dataset
includes information on every public school in Virginia, including their location, funding
information, test scores, graduation, absenteeism and dropout rates, aggregated teacher
information, and demographics. The dataset can be found [here](https://www.kaggle.com/datasets/zsetash/virginia-public-schools/data).
We encountered two problems with our data. First of all, the data, rather than being
in one large spreadsheet, was split up across several different spreadsheets. Additionally,
the format of some of the data was inconsistent, making it difficult to combine.
However, we were able to combine the spreadsheets and process the data appropriately.
The second problem we encountered was that information on absenteeism, graduation
rates, and dropout rates, which we considered relatively important, was only present in
high schools. The whole dataset featured 1700 samples, while high schools only made
up about 350 of these. We decided to test with both a sample of all schools with these
columns excluded and with just the high schools with all columns included.
### Regression
Our project makes use of two models: regression models and K-means models.
We use a regression model because regression models are simple and often accurate
when predicting a continuous output variable based on input variables. These models
mathematically minimize the MSE (mean squared error), a measure of the expected
error between a predicted and true value. Another advantage of using these models is
that it is relatively simple to analyze the results and rank how important different
features are. This model will be most effective if the relationship between the inputs
and the output underlying the data is linear. However, regressions are susceptible to
independent variables being too heavily correlated with each other and outliers, which
we had to address in our data cleaning. Since SOL pass rates are a continuous number,
it is appropriate to predict with our regression model.
To undergo this testing, we tried the following regression models: linear regression,
decision tree, random forest, elastic net, gradient boosting, SGD regressor, and Bayesian
ridge. We tested all of these with both the full school sample and the high schools only.
We took the combination of model and dataset with minimum MSE ran over a 5-fold
cross validation and then ran a randomized 5-fold cross validation parameter search to
further minimize the MSE.
### K-Means
We are also using K-Means models. These models use the input space to ”cluster”
different data points together. This way, we can partition the sample space into groups
of schools and see which groups, or which ”types” of schools, produce the best SOL pass
rates. This allows us to view the problem as one consisting of different tiers or classes of
schools, and will let us to extract the exact characteristics of these different groups of
schools. In examining these characteristics we can then look at what correlates with
better performance in schools. As data about dropouts is only available for high schools,
we decided to use two different K-Means models. One uses data for all schools (Model 1) and the other only uses data for high schools (Model 2).
For these K-Means models, specific features were selected for each model as we
thought either that these were relevant features that could be changed in order to
increase student performance or those features were a good way to determine student
performance. For Model 1, these features were ”SOL Pass Rate”, ”English: Reading”,
”History and Social Sciences”, ”Mathematics”, ”Science”, ”Chronic Absenteeism Rate”,
”Percent of Inexperienced Teachers”, ”Percent of Out of Field Teachers”, ”Percent of
Out of Field and Inexperienced Teachers”, ”Bachelor Degree Percent”, ”Master Degree
Percent”, ”Doctoral Degree Percent”. As for the model only looking at high schools, it
included all these features in addition to ”Graduation Completion Index” and a new
feature called ”Dropout Rate” which was created by dividing the each schools number
of dropouts by the end of year average membership rate.
To determine the best k value fore each model, the elbow method was used. Both
models were tested using k values of 2 to 10 and the sum squared error per k value was
graphed as shown by ”Figure 1: Model 1” and ”Figure 2: Model 2”. You can see in
Figure 2 that there is a clear elbow at k value of 7. As a result, we decided a k value of
7 would be the best option for Model 2. As shown in Figure 1, there is no obvious elbow
so we were forced to use a different method for determining the best k value for this
model. Through testing different k values, a k value of 7 for Model 1 gave us the best
results so this was the chosen k value for this model.
Figure 1. Model 1 Figure 2. Model 2
# Analysis and Interpretation
## Regression
We ran a regression on all the models we considered as well as the two different datasets. The regressor with the lowest error was Gradient
Boosting with the full feature space and samples limited to high school. We then ran
the 5-fold cross validation randomized parameter search, which found that the minimum
error regressor used the hyperparameters maxdepth = 3, maxf eatures = 5,
maxleaf nodes = 146, minsamplesleaf = 3, estimators = 237 and got a mean MSE of
56.28, standard deviation of 10.35, and R2 of 0.5474. These results are mediocre, with a
relatively low R2 and high MSE, but good enough to analyze the important features
and conclude that prediction of SOL pass rates is difficult. These features
indicate that schools where students need free lunches (an indication of community
income) and where students consistently skip class or drop out do worse, whereas size of
school and Title 1 code status are not as important.
## K-Means
For K-Means Model 1, the best performing group by a significant distance, had on
average a 9% higher pass rate than the rest of the groups. The biggest difference
between this school group and the rest was the percentage of Teachers with a Masters
degree. It’s 20% higher than the next highest group. Additionally, The two groups
with the highest SOL Pass Rates both have less than 4.5% of teachers inexperienced
and less than 2.5% of Teachers out of field. No other schools have this combination of
low percentage of inexperienced teachers and low percentage of teachers out of field. As
for Model 2, the feature that best correlates with a low Dropout rate is Absenteeism.
Across the board groups with higher rates of Absenteeism have lower dropout rates.

# Features & Policy Recommendations
Through our investigation and experimentation, we’ve discovered a few things about the
importance of various factors on influencing positive academic outcomes. First of all,
unfortunately, is the importance of community income. As can be seen from the
regression analysis, eligibility for free and reduced lunches, a key indicator of the
financial situation of students in the school, is the most important feature for academic
success. Additionally, we found that funding for schools is important, with state level
funding being the most important and federal level funding being less important.
Division level expenditures were also more impactful than school level expenditures. We
discovered, unsurprisingly, that students going to school is important for good test
scores. Schools with a high absenteeism rate, high dropout rate, and low graduation
rate, had significantly worse test scores. Finally, while for the overall dataset teacher
qualifications don’t have a large importance, they clearly separate the top tier schools
from the mid-top tier schools, indicating that teacher qualifications only matter when a
school is already high quality.
These conclusions present some possible policy recommendations. As it should be
clear at this point, improving academic outcomes is no easy task. However, there are
some lessons we can learn from our analysis. First of all, funding helps. While it’s not
an end-all be-all approach to improving education, there is a clear positive impact of
giving a school more resources, and the most important source of funding is division
level state expenditures. Additionally, keeping kids in school is important. Students
must be in class to get the benefits of school and policies targeted at reducing
absenteeism and truancy rates, like flexible scheduling, parental involvement, and
transportation support, should be considered to ensure that kids are actually being
educated. Finally, for schools that are already decent but looking to improve test scores
and become a top tier high school, targeting highly qualified and experienced teachers is
beneficial. Otherwise, there are more important areas to focus resources on. These
policy recommendations, which are drawn from our experiments, should help schools
improve SOL pass rates and create a positive impact on Virginia’s education system,
creating a better quality of life for us all.
# Reflections
Overall we were able to successfully make meaningful observations on what we can do
to improve students performance in schools, however we did encounter some problems in
the process. There is a significant amount of variation between schools when it came to
how well they performed on tests that couldn’t be explained by the features we had
available which made making predictions harder. This was even more prevalent when
looking at only high schools as this shrunk the data set by a considerable amount. Some
of our original predictions did match up with our findings as we did find that funding
and financial situation of the students were both important factors in determining how
well a student will perform in school. Additionally we were able to predict that
absenteeism would have a strong negative correlation with test scores. While we did
predict teacher experience/qualifications was a factor in students performance, we failed
to anticipate that it would not be a relevant factor for all schools, but only for
separating the top level schools from the rest. In the future, we would like to more
deeply look into finding out how to improve Virginia schools using a number of different
strategies. Firstly, we would like to find new data sets on Virginia schools with different
information that we can combine with the one we used here to so we could find other
possible factors that might affect student performance. We would also like to test this
current data set with different models such as SVM as we can use it for classification to
separate schools into groups.
