import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def getDropOffHour(s):
    s = str(s)
    if len(s) == 4:
        return s[:2]

    if len(s) == 3:
        return s[:1]

    return "00"

def getDropOffMinute(s):
    s = str(s)
    if len(s) == 4:
        return s[2:]

    if len(s) == 3:
        return s[1:]

    return s


df = pd.read_csv('dataset/nyc-taxi-mh-bk.csv')
#print(df[['pickup_time','dropoff_time']].head(100))

df['HourDay']= df['dropoff_time'].apply(lambda x: getDropOffHour(x))
df['MinutesDay']= df['dropoff_time'].apply(lambda x: getDropOffMinute(x))

for key,g in df.groupby(['HourDay']):
    minutos = g['MinutesDay'].unique()
    minutos.sort()
    print(key,minutos)
    print(g['dropoff_time'].head(2))