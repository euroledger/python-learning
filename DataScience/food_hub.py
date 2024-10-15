# import libraries for data manipulation
import numpy as np
import pandas as pd

# import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Write your code here to read the data
df = pd.read_csv('foodhub_order.csv')

# Write your code here to view the first 5 rows
print(df.head())

# Q.1
rows = len(df.axes[0])
cols = len(df.axes[1])
# print number of rows and columns
print("rows:", rows, "cols:", cols, "\n")

# Q.2
# print types of all columns in the dataset
print(df.info())

# Q.3
# extract missing values, and print number of missing values
print("missing values:", df.isnull())
print("missing values 2:", df.isnull().sum())
print("num rows with missing values:", sum([True for idx,row in df.iterrows() if any(row.isnull())]))

# Q.4
# calculate mean, min, max of food preparation time
result = df.agg({'food_preparation_time': ['mean', 'min', 'max']})
print("mean, min, max food preparation time:", result)

# Q.5
# count number of ratings not given
result = df['rating'].value_counts()['Not given']
print("num ratings not given:", result)

# Q.6
# Explore all the variables and provide observations on their distributions.
# (Generally, histograms, boxplots, countplots, etc. are used for univariate exploration.)
# df.hist(column='food_preparation_time')
# df.hist(column='delivery_time')
# plt.show()

# Q.7
# show top 5 restaurants by number of orders
top_restaurants= df['restaurant_name'].value_counts().nlargest(5)
print("restaurant with most orders:", top_restaurants)

# Q.8
# Which is the most popular cuisine on weekends?
result = df[df['day_of_the_week'].str.contains('Weekend')]
cuisine_count = result['cuisine_type'].value_counts().nlargest()
print("Data from weekends:", cuisine_count)

# Q.9
# What percentage of the orders cost more than 20 dollars?
# get the number of rows satisfying the condition
num_rows = len(df[df['cost_of_the_order'] > 20.0])

# Q.10
# calculate the percentage using num total rows retrieved earlier
# round to 2 d.p.
fraction_rows = num_rows / rows
percentage_rows = round(fraction_rows * 100, 2)
print("num orders > $20:", percentage_rows, "%")

# Q.11
# What is the mean order delivery time?
result = df.agg({'delivery_time': ['mean']})
print("mean order delivery time:", result)

top_customers = df['customer_id'].value_counts().nlargest(3)
print("top 3 customers=", top_customers)

# Q.12
ax1 = df.plot.scatter(x='cost_of_the_order',
                      y='food_preparation_time',
                      c='DarkBlue')
ax2 = df.plot.scatter(x='food_preparation_time',
                      y='delivery_time',
                      c='DarkBlue')

ax3 = df.plot.scatter(x='cuisine_type',
                      y='cost_of_the_order',
                      c='DarkBlue')

ax4 = df.plot.scatter(x='restaurant_name',
                      y='cost_of_the_order',
                      c='DarkBlue')

ax5 = df.plot.scatter(x='day_of_the_week',
                      y='delivery_time',
                      c='DarkBlue')
ax5.legend()
plt.show()
# ratings = df[df['rating'] != 'Not given'].sort_values('rating')
#
# ax6 = ratings.plot.scatter(x='rating',
#                       y='cost_of_the_order',
#                       c='DarkBlue')

# fig = plt.figure(figsize=(7,4))
# ax = fig.add_subplot(111)
# for i,name in enumerate(df.restaurant_name.unique()):
#     df[df.restaurant_name == name].plot.scatter('cost_of_the_order', 'delivery_time',
#                                                       ax=ax, color='C{}'.format(i),
#                                                       label=name)


# Q.13

# filter out non-numeric ratingss
filtered_ratings = df[df.rating.apply(lambda x: x.isnumeric())]
filtered_ratings.rating = pd.to_numeric(filtered_ratings.rating, errors='coerce')

# filter restaurants with mean > 4.0
df3 = filtered_ratings.groupby('restaurant_name').filter(lambda x: x['rating'].mean() > 4.)

# filter restaurants with fewer thn 50 ratings
df4 = df3[df3.groupby("restaurant_name")['rating'].transform('size') > 50]

# calculate mean of ratings of remaining restaurants
df5 = df4.groupby('restaurant_name').rating.mean().sort_values(ascending=False)
print("TOP RESTAURANTS BY AVG RATING=", df5)

# Q.14

# sum1 = df['cost_of_the_order'].transform('sum')

sum1 = df[(df[['cost_of_the_order']]>20)]
sum2 = df[(df['cost_of_the_order'] <=20) & (df['cost_of_the_order'] > 5)]

total1 = sum1['cost_of_the_order'].sum() * .25
total2 = sum2['cost_of_the_order'].sum() * .15

grand_total = total1 + total2
print(f"REVENUE OWED TO THE COMPANY = {grand_total:.2f}")

# Q.15

# get all total delivery times > 60
column_names = ['food_preparation_time', 'delivery_time']
filter1 = df[(df[column_names].sum(axis=1)>60)]

# get row count for this df
filtered_rows = len(filter1.axes[0])

# calculate percentage
percentage_long_orders = round((filtered_rows / rows) * 100, 2)
print("VERY LONG ORDER PERCENTAGE =", percentage_long_orders, "%")


# Q.16

# filter rows by day of the week
weekend_df = df[df['day_of_the_week'] == 'Weekend']
weekend_avg = round(weekend_df['delivery_time'].mean(), 1)
print("WEEKEND DELIVERY TIME AVERAGE=",weekend_avg, "MINS")

weekday_df = df[df['day_of_the_week'] == 'Weekday']
weekday_avg = round(weekday_df['delivery_time'].mean(), 1)
print("WEEKDAY DELIVERY TIME AVERAGE=",weekday_avg, "MINS")

# Q.17
cuisine_type = filtered_ratings.groupby('cuisine_type').rating.mean().sort_values(ascending=False)
print(cuisine_type)

# recommendation - Spanish, Thai and Indian are the most popular, go with these!

# Could do further analysis of cost vs cuisine type, or whether to focus on weekends










