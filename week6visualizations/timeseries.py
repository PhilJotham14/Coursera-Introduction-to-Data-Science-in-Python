# Time Series is any data set or data frame where values are measured in different points of time.
import pandas as pd
import matplotlib.pyplot as plt
ax = plt.gca()

# movie_data = pd.read_csv('IMDB.csv')
movie_data = pd.read_csv('avocado.csv')
print(movie_data.head(2))

# changing the data type from integer to date time
movie_data['Date'] = pd.to_datetime(movie_data['Date'])
print(movie_data.dtypes)

# print(movie_data[["Runtime (Minutes)"]])

# .set_index('Year') makes us rearrange our data starting from Year as first reference point
movie_data = movie_data.set_index('Date')
print(movie_data)

# my_dataframe = movie_data[['Year', 'Director', 'Genre', 'Rating']]
my_dataframe = movie_data[['AveragePrice', 'type', 'region']]

print(my_dataframe.loc['2015-12'])

my_dataframe['AveragePrice'].plot()
# my_dataframe = my_dataframe.set_index('Year')
# print(my_dataframe)

# print(my_dataframe.index)  # prints a data series
# print(my_dataframe.dtypes)

# print(my_dataframe.sample(5, random_state=0))
