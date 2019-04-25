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


"""
    Fill null values with 0 for TotalSpend and TotalActivities
"""


"""
    Look at stats for TotalSpend
"""


"""
    Initialize X and Y, and plot them
"""


"""
    Box plots to look for outliers
"""


"""
    Handle outliers using z-score
"""


"""
    Reset X and Y
"""


"""
    Box plots to verify there are fewer outliers
"""


"""
    Scatter plot to look for linear relationship
"""


"""
    Step 3 - split data into training and testing subsets
"""


"""
    Step 3 - create and train the model
"""


"""
    Step 4 - use the model to predict
"""


"""
    Step 5 - plot / visualize
"""
