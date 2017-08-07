#coding:latin-1
import pandas as pd
from os import listdir
from os.path import isfile, join

mypath = 'dataset-bymonth'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]



for file in [onlyfiles[0]]:
    df = pd.read_csv(mypath+'/'+file)

    for key, g in df.groupby(['DayOfWeek']):

        fechas = g['dropoff_date'].unique()
        fechas.sort()
        print(key,fechas)

# df["bucket"] = pd.qcut(df["dropoff_time"], 100)
# df2 = df[['dropoff_time','bucket']].groupby(['bucket']).count()
#
#
# df3 = pd.DataFrame({'bucket':df2['dropoff_time'].index, 'count':df2['dropoff_time'].values})