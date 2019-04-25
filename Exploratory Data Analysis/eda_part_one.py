import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

"""
    1 - Get the data
    2 - Examine the data types, convert as needed; rename columns as desired
    3 - Stats about the data
    4 - Handling missing values
    5 - Count plots and box plots
"""

"""
    1 - Get the data
    
    Steps:
        Get the file path
            
            directory = os.path.dirname(__file__)
            path = os.path.join(directory, 'file_name.extension')
            
                NOTE: this will find the directory of this python file, so keep all files you'll need within the same 
                directory.  If you don't have the file in the project folder, take this approach instead: 
                    path = (r'full_file_path')
                    
        Append the file name to the path
        Use read_excel to pull data into a pandas data frame
            
            dataframe_name = pd.read_excel(path, sheet_name='sheet_name', index_col='column_name')
            
                NOTE: if you don't know which column you want as an index, omit the index_col argument and pandas will
                create an index column for you with the row number as the index
"""

directory = os.path.dirname(__file__)
path = os.path.join(directory, 'PandoraAllData.xlsx')
df_leads = pd.read_excel(path, sheet_name='Leads', index_col='LeadKey')

""""""
"""
    2 - Examine the data types, convert as needed
    Steps:
        .head(n) - returns the top n number of rows (default is five if you don't specify)
        .shape - returns the dimensions of your data frame (rows x columns)
        .columns - returns a list of the column names
        .dtypes - returns the column name and the data type of the values in that column
            NOTE: objects are most commonly strings / nvarchar values when seen in a data frame
                  booleans are most commonly int64 when seen in a data frame
        
        To rename a column: 
            dataframe_name.rename(columns={'old_column_name_one' : 'new_column_name_one', 
                                           'old_column_name_two':'new_column_name_two'}, inplace=True)
        
        To convert to a new data type: 
            object to date:
                dataframe_name['column_name'] = pd.to_datetime(dataframe_name['column_name'], format='format_style')
                NOTE: FORMAT EXAMPLES
                    existing value              format
                    12/01/2019                  '%m/%d/%Y'
                    30/01/2019                  '%d/%m/%Y'
                    12-01-2019                  '%m-%d-%Y'
            other data types:
                dataframe_name['column_name'] = dataframe_name['column_name'].astype(new_data_type)
        
"""

print('\nTop ten Leads: ')
print(df_leads.head(10))
print('\nShape of data frame: ')
print(df_leads.shape)
print('\nColumn Names: ')
print(df_leads.columns)
print('\nData Types: ')
print(df_leads.dtypes)

#Rename Column 'ConvertedOpportunityKey' to 'ConvertedOppKey'
df_leads['ConvertedOpportunityKey'].rename(column={'ConvertedOpportunityKey': 'ConvertedOppKey',
                                                   'LeadConvertedDate': 'ConvertedDate'}, inplace=True)
print('\nRenamed Column Names: ')
print(df_leads.columns)

#Change LeadConverted int64 -> LeadConverted float64
df_leads['LeadConverted'] = df_leads['LeadConverted'].astype(float)
print('\nNew Data Types: (LeadConverted should have changed from int to float)')
print(df_leads.dtypes)

#Change back
df_leads['LeadConverted'] = df_leads['LeadConverted'].astype(int)
print('\nNew Data Types: (LeadConverted should have changed back to int)')
print(df_leads.dtypes)

"""
    3 - Stats about the data: .describe()
    Steps:
        Look at the descriptive statistics for the whole dataframe
            dataframe_name.describe()
        Look at the descriptive statistics for one column
            dataframe_name['column_name'].describe()
        Look at the descriptive statistics for numeric types only
            dataframe_name.describe(include=[np.number])
        Look at the descriptive statistics for categorical types only
            dataframe_name.describe(include=[np.object])
        Find out how many unique values exist within a column
            dataframe_name['column_name'].nunique()
        Look at the number of records by column value
            dataframe_name['column_name'].value_counts()
        NOTES:
            count: count of rows with a value (excludes nulls or NANs)
            mean: average of all rows with a value
            std: standard deviation
            min: lowest value (excludes nulls)
            25%: value for 25th percentile
            50%: value for 50th percentile
            75%: value for 75th percentile
            max: largest value
            unique: number of unique values
            top: value that occurs the most 
            feq: number of times the most frequent value is present
        
"""
print('\nDescriptive statistics for whole data set: ')
print(df_leads.describe())
print('\nDescriptive statistics for LeadAnnualRevenue: ')
print(df_leads['LeadAnnualRevenue'].describe().apply(lambda x: format(x, 'f')))
print('\nDescriptive statistics for numeric values only: ')
print(df_leads.describe(include=[np.number]))
print('\nDescriptive statistics for categorical values only: ')
print(df_leads.describe(include=[np.object]))

print('\nNumber of unique industries: ')
print(df_leads['LeadIndustry'].nunique())
print('\nNumber of leads by industry: ')
print(df_leads['LeadIndustry'].value_counts())
print('\nNumber of leads owned by rep: ')
print(df_leads['LeadOwner'].value_counts())

"""
    4 - Handling missing values
        Steps:
            Check for null values
                Do nulls exist in the whole data frame?
                    dataframe_name.isnull().values.any()
                Do nulls exist in a column?
                    dataframe_name['column_name'].isnull().values.any()
                How many nulls exist in the whole dataframe?
                    dataframe_name.isnull().sum()
                How many nulls exist in a column?
                    dataframe_name['column_name'].isnull().sum() 
            Decide how to handle: 
                Drop
                    drop all records with null values
                        dataframe_name.dropna(subset=['column_name_1', 'column_name_2', 'column_name_n'], inplace=True)
                Fill
                    fill empty values with zero
                        fill all empty values:
                            dataframe_name.fillna(0)
                        fill empty values in given column:
                            dataframe_name['column_name'].fillna(0)
                    fill empty values with the most frequently occuring value
                    fill empty values with the average value
"""

print('Are there any null values our dataset?: ', df_leads.isnull().values.any())
print('Are there any null values in the LeadStatus column?: ', df_leads['LeadStatus'].isnull().values.any())
print('Are there any null values in the LeadScore column?: ', df_leads['LeadScore'].isnull().values.any())
print('How many null values exist in the LeadScore column?: ', df_leads['LeadScore'].isnull().sum())

""" Make a copy of our dataframe
    Drop all rows with null values in LeadAnnualRevenue
    Delete dataframe because we're good stewards of memory"""
drop_null_annual_revenue = df_leads.copy()
drop_null_annual_revenue.dropna(subset=['LeadAnnualRevenue'], inplace=True)
print(drop_null_annual_revenue) #Should get 5844 rows x 12 columns
del drop_null_annual_revenue

""" Make a second copy of our dataframe
    Drop all rows with null values in LeadAnnualRevenue, LeadNumEmployees, and / or LeadIndustry
    Delete dataframe"""
drop_null_multiple_columns = df_leads.copy()
drop_null_multiple_columns.dropna(subset=['LeadAnnualRevenue', 'LeadNumEmployees', 'LeadIndustry'], inplace=True)
print(drop_null_multiple_columns) #Should get 5827 rows x 12 columns
del drop_null_multiple_columns

""" Make another copy....
    Fill all null values with zero
    Delete dataframe"""
fill_all = df_leads.copy()
fill_all.fillna(0, inplace=True)
print('Do any null values exist in the entire dataframe?: ', fill_all.isnull().values.any())
del fill_all

""" Make a copy
    Fill all null values in specific column with zero
    Delete dataframe"""
fill_specific = df_leads.copy()
fill_specific['LeadNumEmployees'].fillna(0, inplace=True)
print('Do any null values exist in LeadNumEmployees? : ', fill_specific['LeadNumEmployees'].isnull().values.any())
del fill_specific

""" Make a copy
    Find the mode of the column we want to fill
    Fill nulls with mode value
    Delete dataframe"""
fill_with_mode = df_leads.copy()
print('\nFind the mode: \n', fill_with_mode['LeadScore'].value_counts())
fill_with_mode['LeadScore'].fillna(float(0.00), inplace=True)
print('Counts by score after fill with mode: \n', fill_with_mode['LeadScore'].value_counts())
del fill_with_mode

""" Make a copy
    Find the average of the column we want to fill
    Fill nulls with average value
    Delete dataframe"""
fill_with_mean = df_leads.copy()
print('\nFind the mean: \n', fill_with_mean['LeadScore'].describe())
print('\nValue counts: \n', fill_with_mean['LeadScore'].value_counts())
fill_with_mean['LeadScore'].fillna(float(5.23), inplace=True)
print(fill_with_mean['LeadScore'].value_counts())
del fill_with_mean

"""
    5 - Count plots and box plots
        Steps:
            BAR CHART
                Count by variable 
                    chart_name = sns.catplot(y=column_name OR x=column_name, data=dataframe_name, kind="count")
                    plt.show(chart_name)
                    NOTE: for lots of variable options (reps, industries, status, etc.), aligning the variable along
                        the y-axis is helpful.  When placed on the x-axis, the variable names will be squished together
                        and overlap if there are too many variable names. 
            BOX AND WHISKER
                    chart_name = sns.boxplot(x='column_name', y='column_name', hue='column_name', data=dataframe_name)
                    plt.show(chart_name)
                    NOTE: X or Y needs to be a categorical column, and the other needs to be a numeric value. 
                        Hue needs to be a categorical value.  When you add hue, it will give you n number of box 
                        charts per x or y category, where n is the number of categories in the hue.
            BOXEN PLOT
                    chart_name = sns.boxenplot(x='column_name', y='column_name', hue='column_name', data=dataframe_name)
                    plt.show(chart_name)
"""

print('\nShow number of leads by industry: ')
count_by_industry = sns.catplot(y='LeadIndustry', data=df_leads, kind="count")
plt.show(count_by_industry)

print('\nShow number of leads by rep: ')
leads_by_rep = sns.catplot(y='LeadOwner', data=df_leads, kind="count")
plt.show(leads_by_rep)

print('\nShow leads by status: ')
leads_by_status = sns.catplot(x='LeadStatus', data=df_leads, kind="count")
plt.show(leads_by_status)

print('\nShow number of converted leads: ')
converted_leads = sns.catplot(x='LeadConverted', data=df_leads, kind="count")
plt.show(converted_leads)

print('\nShow lead score by owner and converted: ')
converted_by_rep = sns.boxplot(y='LeadOwner', x='LeadScore', hue='LeadConverted', data=df_leads, linewidth=2.5)
plt.show(converted_by_rep)

print('\nShow lead score by status and converted: ')
converted_by_rep = sns.boxenplot(x='LeadStatus', y='LeadScore', hue='LeadConverted', data=df_leads, linewidth=2.5)
plt.show(converted_by_rep)

corr = df_leads.corr()
correlation_heatmap = sns.heatmap(corr)
plt.show(correlation_heatmap)

