import pandas as pd

# Read Data from the Data file
data = pd.read_csv('avocado.csv')

# Read data with specific explicit index
indexed_data = pd.read_csv('avocado.csv', index_col="Date")

# View Data from the Source
# Head gives you thr firdt 5 rows of Data
print(data.head())

# if you want to print the last 5 rows you use data.tail
print(data.tail())

# Understood the Information about the Data
# print(data.info())

# Getting the number of rows and columns in the Data set
# print(data.shape)

# Getting Statistical Summary of our Data Frame
# print(data.describe())

# Getting a Data series from one Data Frame meaning concentrated on one column
# print(data["Total Bags"])

# Getting a Data Frame from our Data Serie
# print(data[["Total Volume"]])

# Getting multiple data frames from the Data set
# print(data[["Date", "AveragePrice"]])

# How to Access Rows / Specific Rows we want
# We use loc & iloc methods to achieve this
# We are focuing on the row 12/27/2015 to get its Average Price, Total Volume,
# loc u use the actual words not indexing (we are accessing the loc using the title of thje row)
# datesRow = data.loc[['2015-09-20']][[
#     "AveragePrice", "Total Volume", "Total Bags", "Small Bags"]]
# print(datesRow)

# iloc i means indexing by indexing for example rows 10:15 meaning indexxing location
daterange = data.iloc[10:15][[
    "Date", "AveragePrice", "Total Volume", "Total Bags", "Small Bags"]]
print(daterange)

# Getting data from the year between 2010 and 2011 with a Average Price less than 1.07
yearBetweenRate = data[((data['year'] >= 2015) & (
    data['year'] <= 2016) & (data['AveragePrice'] < 1.07))]
print(yearBetweenRate)

# Group By Operation on the Data
# incase use type & region
dateData = data.groupby('Date')[['AveragePrice']].mean().head()
print(dateData)

averageData = data.groupby('Date')[['AveragePrice']].min().tail()
print(averageData)

# Sorting Operations on Our Data from Highest to Lowest
# Sorting Data from the last five rows of the Date with the least Average Price in Descending order
sorted_data = data.groupby('Date')[['AveragePrice']].mean(
).sort_values(['AveragePrice'], ascending=False).tail()
print(sorted_data)

# DEALING WITH MISSING VALUES IN YOUR DATASET
print(data.isnull().sum())

# DROPPING ROWS WITH NULL VALUES
# This can be achieved by using two methods first:drop method
# dropping the Small Bags column
# for example Inplace "print(data.drop('Small Bags', axis=1,inplace=True).head())" temporaily deletes the column
print(data.drop('Small Bags', axis=1).head())

# Second method for dropping values is dropna
# This deletes all columns and misssing valuesand null values
# print(data.dropna('Small Bags', axis=1))

# If you dont specify the axis using dropna it will delete the rows with Null values
# data.dropna()

meanVolume = indexed_data['Total Volume'].mean()
print("The mean Total Volume is:", meanVolume)

# Handle Missing values is the Total Volume Column
indexed_data['Total Volume'].fillna(meanVolume, inplace=True)
print(indexed_data.isnull().sum())
