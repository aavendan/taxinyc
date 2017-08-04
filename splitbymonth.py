import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('dataset/nyc-taxi-mh-bk.csv')


df['dropoff_date'] = pd.to_datetime(df['dropoff_date'])
print(df['dropoff_date'].head(10))