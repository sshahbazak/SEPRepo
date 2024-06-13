import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

## define variable for data & have panda read using file path

data = pd.read_csv(r"C:\Users\Porte\Desktop\notredame_files\L1_TESTS_FINAL_SUBMISSION.csv")

## displays the first 5 lines of the data

##print(data.head())

## prints the number of records, and fields

##print(data.shape)

## summary of the structure of the data

##print(data.info())

## sorting data by mission_complete

##print(data.sort_values(by=['mission_complete'], inplace = False, ascending = True))

## count all not null data values

##print(pd.notnull(data).sum())

##

##print(data.sort_values(by=['throttle'], inplace = False, ascending = True))

##

##print(data.sort_values(by=['Wind'], inplace = False, ascending = True))

##

##print(data.sort_values(by=['GFPRED'], inplace = False, ascending = True))

##

##print(data.sort_values(by=['GFACT'], inplace = False, ascending = True))

## changing the format of columns

##data['NAME'] = data['NAME'].astype('TYPE')

##data['NAME'] = data['NAME'].astype('TYPE')

## Create a new column, correcting the year

##data['releasedyyyy'] = data['released'].str.extract(pat='([0-9]{4})').astype(int)

## Drop duplicates shows all mode types used

##print(data['Mode'].drop_duplicates().sort_values(ascending = False))

##does not work

##print(data.corr(method = 'pearson'))

##does not work

##pd.set_option('display.max_rows', None)
##cor_mat = data.corr()
##correlations = cor_mat.unstack()
##correlations = correlations.sort_values()
##correlations.head()

## information about unnamed, throttle, max_deviation, & max_altitude

##print(data.describe())

##shows unique values for throttle

##print(data['throttle'].unique())

##does not work

##print(data.groupby('y').mean())

##does not work

##print(data.groupby('throttle').mean())

##not sure this did what I wanted

##data1 = data.copy()
##data11 = pd.get_dummies(data1, columns=['throttle','GF','GFACT','GFPRED'])
##print(data11)

##find how to display columns not shown in the middle

##find how to change NaN to 0

##find how to change No to False and Yes to True

##find how to change data types

##find how to fill nulls

##find how to find and delete duplicate records

##find how to change MSN State column name to MSN_State

##ask aout GFPRED_NO & GFPRED_YES being opposites?

##

##data = np.random.rand(100,3)

## scatter plot (throttle vs max_deviation)

# plt.scatter(x=data['throttle'], y =data['max_deviation'])
# plt.title('throttle vs max_deviation')
# plt.xlabel('throttle')
# plt.ylabel('mission_complete')
# print(plt.show())
