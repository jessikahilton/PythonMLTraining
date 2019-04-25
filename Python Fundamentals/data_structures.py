import numpy as np
import os
import pandas as pd

#----------------------------------------------------------------------------------------------------------------------#
###Data Structures
#LISTS
#Key features:
#   create using square brackets
#   lists can contain items of different data types
#   items in a list can be changed after creation (mutable)
listOne = ['a', 'b', 'c', 'd', 0, 1, 2, 3, 4]
listTwo = ['apple', 'orange', 'banana']
listThree = [100, 200, 300, 400]

#Accessing elements in lists
varOne = listOne[3]
print(varOne)
sublistOne = listOne[1:5]
print(sublistOne)

#Updating elements in a list
listTwo[0] = 'pineapple'
print(listTwo[0])

#Adding elements to a list
listTwo.append('tangerine')
listTwo.append('kiwi')
veggies = ['cauliflower', 'peppers', 'cucumber', 'tomato']
listTwo.append(veggies)
print(listTwo[5])
print(listTwo)

#Deleting elements from a list
del listThree[0]
print(listThree)

#Basic functions of lists
print('Length of listOne: ' + str(len(listOne)))
print('listTwo + listThree: ' + str((listOne + listTwo)))
print('Repetition of listTwo[1] five times: ' + str(listTwo[1]*5))
print('Does cucumber exist in listTwo?: ' + str(('cucumber' in listTwo)))
print('Iteration: ')
for item in listTwo:
    print(item)

#----------------------------------------------------------------------------------------------------------------------#
#TUPLES
#Key features:
#   similar to a list except that you cannot change a tuple after creation (immutable)
#   create using parenthesis
tupleOne = ('A', 'B', 1, 2, 3)
tupleTwo = ('reptile', 'amphibian', 'mammal')

#Accessing elements in a tuple
elementOne = tupleOne[0]
print('\nFirst element of tupleOne: ' + str(elementOne))
lastElement = tupleOne[-1]
print('Last element of tupleOne: ' + str(lastElement))
middleElements = tupleOne[1:4]
print('Middle elements of tupleOne: ' + str(middleElements))

#Updating elements in a tuple
tupleThree = tupleOne + tupleTwo
print(tupleThree)

#Deleting elements in a tuple - NOT POSSIBLE!
#Deleting an entire tuple
del tupleThree

#Basic functions of tuples
print('Length of tupleOne: ' + str(len(tupleOne)))
print('Concatenation of tupleOne and tupleTwo' + str(tupleOne + tupleTwo))
print('Does fish exist in tupleTwo? ' + str('fish' in tupleTwo))
print('Iteration: ')
for item in tupleTwo:
    print(item)

#----------------------------------------------------------------------------------------------------------------------#
#DICTIONARIES
#Key features:
#   create using curly braces
#   dictionaries are composed of unique keys with any number and type of values

simpleDictionary = {'Name': 'Loki', 'Breed': 'Ragdoll Siamese', 'Age': 7}
#Accessing elements in a dictionary
print('\nPet name: ' + str(simpleDictionary['Name']))
print('Breed: ' + str(simpleDictionary['Breed']))
print('Age: ' + str(simpleDictionary['Age']))

#Finding the keys of a dictionary
print('Keys: ' + str(simpleDictionary.keys()))

#Updating and adding values in a dictionary
simpleDictionary['Age'] = 6
simpleDictionary['Food'] = 'Blue Buffalo'
print(simpleDictionary)

#Deleting values in a dictionary
del simpleDictionary['Breed']
print(simpleDictionary)

#----------------------------------------------------------------------------------------------------------------------#
#NESTED DICTIONARIES
#Key features
#   A dictionary of dictionaries
#   One unique value maps to a dictionary of features
nestedDictionary = {1: {'Breed': 'Rottweiler', 'Name': 'Frankie', 'Age': 0, 'DaysAtShelter': 4, 'isHouseTrained': False},
                    2: {'Breed': 'Greyhound', 'Name': 'Rupert', 'Age': 7, 'DaysAtShelter': 21, 'isHouseTrained': True}}

print('\nShelter pet 1: ')
print(nestedDictionary[1])

print(str(nestedDictionary[1]['Name']) + ' has been at the shelter ' + str(nestedDictionary[1]['DaysAtShelter']) + ' days.')

#Adding an element
nestedDictionary[3] = {'Name': 'Titan', 'DaysAtShelter': 0}
print(nestedDictionary[3])

#Updating a value
nestedDictionary[3]['DaysAtShelter'] = 2
print(nestedDictionary[3])

#Deleting a value
del nestedDictionary[3]['DaysAtShelter']
print(nestedDictionary[3])


#----------------------------------------------------------------------------------------------------------------------#
#NUMPY ARRAYS
list = ['Algeria', 'Kazakhstan', 'Argentina', 'India', 'Australia', 'Brazil', 'China', 'USA', 'Canada', 'Russia']
largestCountries = np.array(list)
print(largestCountries)

print('Data type: ', largestCountries.dtype)
print('Item size: ', largestCountries.itemsize)
print('nbytes: ', largestCountries.nbytes)

print('Largest Country: ', largestCountries[-1])
print('Fifth largest country: ', largestCountries[-5])
print('Tenth largest country: ', largestCountries[0])

#----------------------------------------------------------------------------------------------------------------------#
#PANDAS DATA FRAMES
#Get data and put it into a dataframe
dir = os.path.dirname(__file__)
filepath = os.path.join(dir, 'PandoraLeads.csv')
#Load the file to a pandas data frame using read_csv
df_pandora_leads = pd.read_csv(filepath)

#Show the top five rows
print('\nTop five rows: ')
print(df_pandora_leads.head())

#Show the top ten rows
print('\nTop ten rows: ')
print(df_pandora_leads.head(10))

#Show the last five rows
print('\nLast five rows: ')
print(df_pandora_leads.tail())

#Show descriptions
print('\nDescriptive statistics: ')
print(df_pandora_leads.describe())

#Show the names of each column
print('\nColumn names: ')
print(df_pandora_leads.columns)

#Show the data types of each column
print('\nData types: ')
print(df_pandora_leads.dtypes)

#Access a row of data
#.iloc takes a numeric index, or the position you want to return
print('\nSelect the first row: ')
print(df_pandora_leads.iloc[0])

#Access data in a column
#.loc takes an explicit name and will return the data with the corresponding column name
print('\nSelect all from the column, Lead Scores: ')
print(df_pandora_leads.loc[:, 'LeadScore'])

#Access one column for a given row
#To combine a specific record and column name, use .loc
print('\nSelect the Lead Score for the 8024 row: ')
print(df_pandora_leads.loc[8024, 'LeadScore'])
