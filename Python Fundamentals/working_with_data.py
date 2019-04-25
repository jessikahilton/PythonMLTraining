import pandas as pd
import os
#import pyodbc

#----------------------------------------------------------------------------------------------------------------------#
###GETTING DATA###
#----------------------------------------------------------------------------------------------------------------------#
#CSV
#Get the path for the working directory
dir = os.path.dirname(__file__)
#Find the leads file in the working directory
filepath = os.path.join(dir, 'PandoraLeads.csv')
#Load the file to a pandas data frame using read_csv
df_pandora_leads = pd.read_csv(filepath, index_col='LeadKey')
#Show the top five rows
print(df_pandora_leads.head())
#Show the names of each column
print(df_pandora_leads.columns)
#Rename 'ConvertedOpportunityKey' to 'OpportunityKey'
df_pandora_leads.rename(columns={'ConvertedOpportunityKey': 'OpportunityKey'}, inplace=True)
print(df_pandora_leads.columns)
#Show the data types of each column
print(df_pandora_leads.dtypes)
#Manipulate the data types
df_pandora_leads['LeadCreatedDate'] = pd.to_datetime(df_pandora_leads['LeadCreatedDate'], format='%m/%d/%Y')
df_pandora_leads['LeadConvertedDate'] = pd.to_datetime(df_pandora_leads['LeadConvertedDate'], format='%m/%d/%Y')
print(df_pandora_leads.dtypes)

#Find the opps file in the working directory
filepath = os.path.join(dir, 'PandoraOpps.csv')
#Load the file to a pandas data frame using read_csv
df_pandora_opps = pd.read_csv(filepath, index_col='OpportunityKey')
#Show the top five rows
print(df_pandora_opps.head())
print(df_pandora_opps.columns)
print(df_pandora_opps.dtypes)
#Manipulate the data types
df_pandora_opps['OppCreatedDate'] = pd.to_datetime(df_pandora_opps['OppCreatedDate'], format='%m/%d/%Y')
df_pandora_opps['OppClosedDate'] = pd.to_datetime(df_pandora_opps['OppClosedDate'], format='%m/%d/%Y')
print(df_pandora_opps.dtypes)

#----------------------------------------------------------------------------------------------------------------------#
#EXCEL FILE (.xlsx)
filepath = os.path.join(dir, 'PandoraAllData.xlsx')
#Load the file to a pandas data frame using read_csv
df_excel_leads = pd.read_excel(filepath, sheet_name='Leads', index_col='LeadKey')
print(df_excel_leads.head())
print(df_excel_leads.columns)
print(df_excel_leads.dtypes)
df_excel_opps = pd.read_excel(filepath, sheet_name='Opps', index_col='OpportunityKey')

#----------------------------------------------------------------------------------------------------------------------#
#SQL Integration
#query = '''SELECT
#               L.CreatedDate
#	            ,L.ConvertedDate
#	            ,L.LeadKey
#	            ,L.Converted
#	            ,L.AnnualRevenue
#	            ,L.LeadScore
#	            ,L.[Status]
#	            ,L.Industry
#	            ,E.FullName
#	            ,L.PreQualified
#	            ,L.Employees
#	            ,L.Unqualified
#	            ,L.ConvertedOpportunityKey
#       FROM [Reporting_Pandora].[dbo].[Leads] L
#	    LEFT JOIN Reporting_Pandora.dbo.Employees E ON L.CurrentOwnerUserKey = E.CrmKey'''

#conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=SqlReportProd1;DATABASE=Imports;Trusted_Connection=yes;')

#df_sql = pd.io.sql.read(query, conn)
#df_sql = pd.read_sql(query, conn)
#print(df_sql.head)


#----------------------------------------------------------------------------------------------------------------------#
#Join two data frames together
#INNER JOIN
#df_inner = pd.merge(df_pandora_leads, df_pandora_opps, on='OpportunityKey', how='inner')
#print(df_inner.columns)
#print(df_inner.head())
#Write the data to a csv file
#df_export_inner = df_inner.to_csv(r'Q:\Market Analysis\000ADAMSTEWART000\USER_LOCAL_REPOS\JessikaHuntLocalRepo\_PersonalWorkspace\MBO\ML Projects\04_17_19_prep\inner_join_export.csv')

#LEFT JOIN
#df_left = pd.merge(df_pandora_leads, df_pandora_opps, on='OpportunityKey', how='left')
#print(df_left.columns)
#print(df_left.head())
#df_export_left = df_left.to_csv(r'Q:\Market Analysis\000ADAMSTEWART000\USER_LOCAL_REPOS\JessikaHuntLocalRepo\_PersonalWorkspace\MBO\ML Projects\04_17_19_prep\left_join_export.csv')

#RIGHT JOIN
#df_right = pd.merge(df_pandora_leads, df_pandora_opps, on='OpportunityKey', how='right')
#print(df_right.columns)
#print(df_right.head())
#df_export_right = df_right.to_csv(r'Q:\Market Analysis\000ADAMSTEWART000\USER_LOCAL_REPOS\JessikaHuntLocalRepo\_PersonalWorkspace\MBO\ML Projects\04_17_19_prep\right_join_export.csv')
