"""
    Implement a linear regression using sklearn, OLS model using your own data.  To do so, your data needs to be:
        - Numeric, continuous values
        - One dependent variable
        - One independent variable
        - Possible ideas:
            - count of activities and spend amount by partner
            - count of opportunities won and total activities per opp
            - total calls and opportunity closed amount
            - total leads to converted opps

        Steps:
            1 - import libraries
            2 - pull in your data
            3 - fill null values
            4 - look for outliers (box plots and distributions are good for this)
            5 - remove outliers based on z-score
            6 - look for linear relationship (scatter plots are good for this)
            7 - split your data into training and test sets (test_size=0.2 is standard)
            8 - create and train your model
            9 - use the model to predict
            10 - plot and visualize

"""

