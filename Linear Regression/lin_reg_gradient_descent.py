import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn import model_selection
from sklearn import linear_model
import os

"""Set figure size for charts"""
plt.rcParams['figure.figsize'] = (12.0, 9.0)

"""
    Linear Regression Basics: 
        y = mx + b
        
        A linear regression finds the line of best fit between plotted points.  You can use the slope equation of 
        a line of best fit to predict the dependent variable given a dependent variable value.  In this example, our
        dependent variable is the amount spent, and the independent variable is the total activities. (This is not a 
        very strong linear relationship, but it works well enough to demonstrate a linear regression.)  That's all a 
        linear regression really is: finding the slope of the line of best fit.
        
        There are a few ways to optimize a linear regression.  This example uses GRADIENT DESCENT, which takes partial
        derivatives to find the lowest point of a curve.  That lowest point is where the error is lowest, or where
        the sum of the distance from all points to the line is lowest.
         
"""

""" 
    Step 1 - collect our data 
"""
directory = os.path.dirname(__file__)
path = os.path.join(directory, 'SamsungSpend.xlsx')
samsung_spend_activities = pd.read_excel(path, sheet_name='MonthlySpend')


"""
    Step 2 - EDA and prep
        Look at column names
        Delete those we don't need
        Verify the remaining columns are the ones we need
        Verify the remaining columns are numeric 
        Fill null values with 0
        Look at the statistics for the TotalSpend column
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

print('\nColumns: ', samsung_spend_activities.columns)
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
    Look at the remaining columns
"""
print(samsung_spend_activities.head())
print(samsung_spend_activities.columns)
print(samsung_spend_activities.dtypes)

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
    Look at distribution for our two variables
"""
dist_activities = sns.distplot(samsung_spend_activities['TotalActivities'], rug=True)
plt.show(dist_activities)

"""
    Look at distribution for our two variables
"""
dist_spend = sns.distplot(samsung_spend_activities['TotalSpend'], rug=True)
plt.show(dist_spend)

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
    Look at distribution for our adjusted data
"""
dist_activities = sns.distplot(samsung_spend_activities['TotalActivities'], rug=True)
plt.show(dist_activities)

dist_spend = sns.distplot(samsung_spend_activities['TotalSpend'], rug=True)
plt.show(dist_spend)

"""
    Scatter plot to look for linear relationship
"""
plt.scatter(X, Y)
plt.show()

"""
    Step 3 - Build the model
    
    Components of a linear regression: 
        m: slope of the line of best fit
        b: a constant value
    
    Components for gradient descent optimization:
        learning_rate: how quickly we want the model to converge. 0.0001 is standard.
        epochs: the number of times we want to train the model
        n: the number of observations in our dataset 
        error: the sum of the differences of the distances between points and the line 
"""

"""Initialize components"""
m = 0
b = 0
learning_rate = 0.0001
epochs = 1000
n = float(len(X))

"""
    Build the model:
    
        For as many iterations as specified in epochs: 
            predicted_value = value on the line of best fit given slope, X values, and constant
            take the partial derivative of the slope using the equation: (-2/n) * sum(X * (Y - predicted_value)) 
            take the partial derivative of the constant using the equation: (-2/n) * sum(Y - predicted_value))
            adjust slope based on the partial derivative of the slope we just calculated
            adjust the constant based on the partial derivative of the constant we just calculated
            adjust the error 
            
    After the model is trained, set the y_predicted_value to the final model, plot it, and show
    
"""
for i in epochs:
    y_predicted_value = m * X + b
    derivative_m = (-2/n) * sum(X * (Y - y_predicted_value))
    derivative_b = (-2/n) * sum(Y - y_predicted_value)
    m = m - learning_rate * derivative_m
    b = b - learning_rate * derivative_b
print('Slope: {0}, \nConstant: {1}'.format(m, b))

y_predicted_value = m * X + b
plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(y_predicted_value), max(y_predicted_value)], color='red')
plt.show()


"""
    Using libraries...
"""

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=4)

x_train = np.array(x_train).reshape(677, 1)
y_train = np.array(y_train).reshape(677, 1)
ols_linear_regression = linear_model.LinearRegression()
ols_linear_regression.fit(x_train, y_train)

x_test = np.array(x_test).reshape(-1, 1)
predictions = ols_linear_regression.predict(x_test)

plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(predictions), max(predictions)], color='red')
plt.show()
