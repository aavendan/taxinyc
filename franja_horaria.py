import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('dataset/nyc-taxi-mh-bk.csv')

df["bucket"] = pd.qcut(df["dropoff_time"], 100)
df2 = df[['dropoff_time','bucket']].groupby(['bucket']).count()


df3 = pd.DataFrame({'bucket':df2['dropoff_time'].index, 'count':df2['dropoff_time'].values})