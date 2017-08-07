#coding:latin-1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

def getMonth(s):
  return s.split("-")[1]

def getDay(s):
  return s.split("-")[2]

def getYear(s):
  return s.split("-")[0]

def getYearMonth(s):
  return s.split("-")[1]+"-"+s.split("-")[0]

def getDayWeek(s):
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    return dias[datetime.datetime(year=int(s.split("-")[0]),month=int(s.split("-")[1]),day=int(s.split("-")[2])).weekday()]

#d?a de la semana que se recorre m?s [12-1830] [1830-0] [0-5] [5-12]

def getDropOffHour(s):
    s = str(s)
    if len(s) == 4:
        return s[:2]

    if len(s) == 3:
        return s[:1]

    return "0"

def getDropOffMinute(s):
    s = str(s)
    if len(s) == 4:
        return s[2:]

    if len(s) == 3:
        return s[1:]

    return s

df = pd.read_csv('dataset/nyc-taxi-mh-bk.csv')

#convertir un str a date
#df['dropoff_date'] = pd.to_datetime(df['dropoff_date'])

#df['month']= df['dropoff_date'].apply(lambda x: getMonth(x))

df['YearMonth']= df['dropoff_date'].apply(lambda x: getYearMonth(x))
df['DayOfWeek']= df['dropoff_date'].apply(lambda x: getDayWeek(x))

df['HourDay']= df['dropoff_time'].apply(lambda x: getDropOffHour(x))
df['MinutesDay']= df['dropoff_time'].apply(lambda x: getDropOffMinute(x))

for key,g in df.groupby(['YearMonth']):
    g.to_csv('dataset-bymonth/'+key+'-nyc-taxi-mh-bk.csv', sep=',', encoding='utf-8')
