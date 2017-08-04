import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('dataset/nyc-taxi-mh-bk.csv')
# ['pickup_date' 'pickup_time' 'pickup_day' 'pickup_latitude'
#  'pickup_longitude' 'trip_distance' 'passenger_count' 'dropoff_date'
#  'dropoff_time' 'dropoff_day' 'dropoff_latitude' 'dropoff_longitude'
#  'fare_amount' 'tolls_amount' 'taxes_amount' 'tip_amount' 'payment_amount'
#  'payment_type']

#día de la semana que se recorre más [12-1830] [1830-0] [0-5] [5-12]

df["bucket"] = pd.qcut(df["trip_distance"], 100)
df2 = df[['trip_distance','bucket']].groupby(['bucket']).count()

df3 = pd.DataFrame({'bucket':df2['trip_distance'].index, 'count':df2['trip_distance'].values})

topTenUp = df3.sort(['count'], ascending=[0]).head(10)
topTenDown = df3.sort(['count'], ascending=[0]).tail(10)

print(topTenUp)
print(topTenDown)

#
ax1 = plt.subplot(1,2,1)
topTenUp.plot(kind='bar', title ="Top Ten Up", ax=ax1, legend=False, x='bucket', y='count')
ax1.set_title("TopTen Up")

#
ax2 = plt.subplot(1,2,2)
topTenDown.plot(kind='bar', title ="Top Ten Down", ax=ax2, legend=False, x='bucket', y='count')
ax2.set_title("TopTen Down")


plt.tight_layout()
plt.subplots_adjust(hspace=1)
plt.show()



# count = df.groupby(['bucket']).size()
# count.hist()
#
# max = count.max()
# min = count.min()
# mean = count.mean()
# std = count.std()
# sum = count.sum()
#
# print(count)
# print("Max ", max)
# print("Min ", min)
# print("Mean ", mean)
# print("Std ", std)
# print("Suma ", sum)
#
# plt.title("Trip Distance")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

#newdf = df[['bucket']].groupby(['bucket']).count()
#print(newdf)
# newdf.plot(kind='bar')
# plt.title("Trip Distance")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()




# resultado = np.histogram(df['trip_distance'], bins=[df['trip_distance'].min(), df['trip_distance'].max()])
# print(resultado)
# results = df['trip_distance'].hist(bins=[df['trip_distance'].min(), df['trip_distance'].max()])
# plt.title("Trip Distance")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

#print(df['trip_distance'].head(10))
#print(results)

# print(df['trip_distance'].max())
# print(df['trip_distance'].min())