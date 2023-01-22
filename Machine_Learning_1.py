## Machine Learning Python Guide

## Chapter 1

import os
import pandas as pd

# titanic data set import
# file_path = 'C:/Users/USER/Downloads/titanic_dataset/'
os.chdir('C:/Users/USER/Downloads/titanic_dataset/')
titanic_df = pd.read_csv('titanic_train.csv')
# titanic_df = pd.read_csv(file_path + 'titanic_train.csv')

## Data Handling
# print(titanic_df.info)
# print(titanic_df.shape)
# print(titanic_df.describe())

# value_counts = titanic_df['Pclass'].value_counts()
# print(value_counts)
# print(titanic_df.columns)

## create columns


# titanic_drop_df = titanic_df.drop('Age_0', axis=1)
# print(titanic_drop_df)