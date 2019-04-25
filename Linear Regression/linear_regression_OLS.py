import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import model_selection
from sklearn import linear_model
from scipy import stats
"""
Linear Regression Basics: 
        y = mx + b
        
        A linear regression finds the line of best fit between plotted points.  You can use the slope equation of 
        a line of best fit to predict the dependent variable given a dependent variable value.  In this example, our
        dependent variable is the amount spent, and the independent variable is the total activities. (This is not a 
        very strong linear relationship, but it works well enough to demonstrate a linear regression.)  That's all a 
        linear regression really is: finding the line of best fit.
        
        There are a few ways to optimize a linear regression.  This example uses the ORDINARY LEAST SQUARES approach.
        
        Steps:
            1 - Collect data
            2 - EDA and prep
            3 - Split training and test
"""

""" 
    Step 1 - collect our data 
"""
directory = os.path.dirname(__file__)
path = os.path.join(directory, 'SamsungSpend.xlsx')
samsung_spend_activities = pd.read_excel(path, sheet_name='MonthlySpend')

"""
    Step 2 - EDA and prep
        Delete columns we don't need (necessary to use z-score later)
        Fill null values with 0
        Look at the statistics for the TotalSpend column
        X = Total Activities
        Y = Total Spend
        Put together some charts / graphs / plots
            Scatter plot: x = total activities, y = total spend
            boxenplot: one for each activities and spend
            distribution: combined histogram and density, one for each activity and spend
        Remove outliers
            Use z-score method to remove outliers based on their z-score
            z-score: the number of standard deviations away from the mean
            We want data within 3 standard deviations, which will cut off the outliers
        Look at charts again to see if removing outliers helped

"""

"""
    Delete columns we don't need
"""
del samsung_spend_activities['FiscalYear']
del samsung_spend_activities['FiscalMonth']
del samsung_spend_activities['CustomerKey']
del samsung_spend_activities['CustomerName']
del samsung_spend_activities['ITorCarrier']
del samsung_spend_activities['DormantOrActive']
del samsung_spend_activities['Industry']

"""
    Fill null values with 0 for TotalSpend and TotalActivities
"""
samsung_spend_activities['TotalSpend'] = samsung_spend_activities['TotalSpend'].fillna(0.00)
samsung_spend_activities['TotalActivities'] = samsung_spend_activities['TotalActivities'].fillna(0)
print(samsung_spend_activities.dtypes)
print(samsung_spend_activities.head())

"""
    Look at stats for TotalSpend
"""
print(samsung_spend_activities['TotalSpend'].describe().apply(lambda x: format(x, 'f')))
print('\n', samsung_spend_activities['TotalActivities'].describe())

X = samsung_spend_activities['TotalActivities']
Y = samsung_spend_activities['TotalSpend']
plt.scatter(X, Y)
plt.show()

"""
    Box plots to look for outliers
"""
tot_spend = sns.boxenplot(x='TotalSpend', data=samsung_spend_activities)
plt.show(tot_spend)

tot_activities = sns.boxenplot(x='TotalActivities', data=samsung_spend_activities)
plt.show(tot_activities)

X = samsung_spend_activities['TotalActivities']
Y = samsung_spend_activities['TotalSpend']

"""
    Handle outliers using z-score
"""
z = np.abs(stats.zscore(samsung_spend_activities))
samsung_spend_activities = samsung_spend_activities[(z < 3.0).all(axis=1)]

"""
    Reset X and Y
"""
X = samsung_spend_activities['TotalActivities']
Y = samsung_spend_activities['TotalSpend']

"""
    Box plots to verify there are fewer outliers
"""
tot_spend = sns.boxenplot(x='TotalSpend', data=samsung_spend_activities, label='TotalSpend')
plt.show(tot_spend)

tot_activities = sns.boxenplot(x='TotalActivities', data=samsung_spend_activities, label='TotalActivities')
plt.show(tot_activities)

"""
    Scatter plot to look for linear relationship
"""
plt.scatter(X, Y)
plt.xlabel('Total Activities')
plt.ylabel('Total Spend')
plt.show()

"""
    Step 3 - split data into training and testing subsets
"""
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=4)


"""
    Step 3 - create and train the model
"""
x_train = np.array(x_train).reshape(677, 1)
y_train = np.array(y_train).reshape(677, 1)
ols_linear_regression = linear_model.LinearRegression()
ols_linear_regression.fit(x_train, y_train)


"""
    Step 4 - use the model to predict
"""
x_test = np.array(x_test).reshape(-1, 1)
predictions = ols_linear_regression.predict(x_test)

"""
    Step 5 - plot / visualize
"""

plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(predictions), max(predictions)], color='red')
plt.show()
