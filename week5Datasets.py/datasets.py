import pandas as pd

# Read Data from the Data file
data = pd.read_csv('IMDB.csv')

# Read data with specific explicit index
indexed_data = pd.read_csv('IMDB.csv', index_col="Title")

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
# print(data["Rank"])

# Getting a Data Frame from our Data Serie
# print(data[["Metascore"]])

# Getting multiple data frames from the Data set
# print(data[["Year", "Rating"]])

# How to Access Rows / Specific Rows we want
# We use loc & iloc methods to achieve this
# We are focuing on the row Sucide Squad to get its Genre, Rating,
# loc u use the actual words not indexing (we are accessing the loc using the title of thje row)
suicdeSquadRow = indexed_data.loc[["Suicide Squad"]][[
    "Genre", "Rating", "Year", "Revenue (Millions)"]]
# print(suicdeSquadRow)

# iloc i means indexing by indexing for example rows 10:15 meaning indexxing location
imdbrange = data.iloc[10:15][[
    "Title", "Director", "Genre", "Rating", "Year", "Revenue (Millions)"]]
# print(imdbrange)

# Data Selection
# How we can filter our Data
# Getting data from the year between 2010 and 2011
# yearBetween = data[((data['Year'] >= 2010) & (data['Year'] <= 2011))]
# print(yearBetween)

# Getting data from the year between 2010 and 2011 with a rating less than 6
yearBetweenRate = data[((data['Year'] >= 2010) & (
    data['Year'] <= 2011) & (data['Rating'] < 6.0))]
print(yearBetweenRate)

# Group By Operation on the Data
directorData = data.groupby('Director')[['Rating']].mean().head()
print(directorData)

averageData = data.groupby('Director')[['Rating']].min().tail()
print(averageData)

# Sorting Operations on Our Data from Highest to Lowest
# Sorting Data from the last five rows of the Director with the least rating in Descending order
sorted_data = data.groupby('Director')[['Rating']].mean(
).sort_values(['Rating'], ascending=False).tail()
print(sorted_data)

# DEALING WITH MISSING VALUES IN YOUR DATASET
print(data.isnull().sum())

# DROPPING ROWS WITH NULL VALUES
# This can be achieved by using two methods first:drop method
# dropping the metascore column
# for example Inplace "print(data.drop('Metascore', axis=1,inplace=True).head())" temporaily deletes the column
print(data.drop('Metascore', axis=1).head())

# Second method for dropping values is dropna
# This deletes all columns and misssing valuesand null values
# print(data.dropna('Metascore', axis=1))

# If you dont specify the axis using dropna it will delete the rows with Null values
# data.dropna()

meanRevenue = indexed_data['Revenue (Millions)'].mean()
print("The mean Revenue is:", meanRevenue)

# Handle Missing values is the Revenue Column
indexed_data['Revenue (Millions)'].fillna(meanRevenue, inplace=True)
print(indexed_data.isnull().sum())
