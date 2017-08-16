#coding:latin-1
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from os import listdir
from os.path import isfile, join
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


#time series analysis arima
#métdoo de correlación espacial


#como van cambiando de una franja de tiempo a la otra van cambiando
#cuántas personas están llegando a este sitio
#change point en una serie de tiempo
#topic modeling: celdas con features

pd.options.mode.chained_assignment = None

def getMonth(file):
    months = ["January", "February", "March", "April", "May","June", "July"]
    return months[int(file.split("-")[0])-1]


mypath = 'dataset-bymonth'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def top5_DayWeek_HourFringe():
    for index in range(len(onlyfiles)):
        file = onlyfiles[index]

        df = pd.read_csv(mypath + '/' + file)

        grouped = df.groupby(['DayOfWeek', 'HourFringe'])[["trip_distance"]].sum()
        ungrouped = grouped.reset_index()
        ordered = ungrouped.sort_values(['trip_distance'], ascending=[False]).head(5)

        print(ordered)

        ax1 = plt.subplot(1, 1, 1)
        ordered.plot(kind='bar', ax=ax1, legend=False, x=['DayOfWeek', 'HourFringe'], y='trip_distance')

        ax1.set_title("Trip Distance by DayOfWeek and HourFringe on " + getMonth(file))

        for i, child in enumerate(ax1.get_children()[:ordered.index.size]):
            ax1.text(i, child.get_bbox().y1 + 5, "%.2f" % ordered['trip_distance'][ordered.index[i]],
                     horizontalalignment='center')

        plt.tight_layout()
        plt.subplots_adjust(hspace=1)
        plt.savefig("resultados/firsttop5_day_fringe/" + getMonth(
            file) + ".png")
        plt.show()

#top5_DayWeek_HourFringe()

def last5_DayWeek_HourFringe():
    for index in range(len(onlyfiles)):
        file = onlyfiles[index]

        df = pd.read_csv(mypath + '/' + file)

        grouped = df.groupby(['DayOfWeek', 'HourFringe'])[["trip_distance"]].sum()
        ungrouped = grouped.reset_index()
        ordered = ungrouped.sort_values(['trip_distance'], ascending=[False]).tail(5)

        print(ordered)

        ax1 = plt.subplot(1, 1, 1)
        ordered.plot(kind='bar', ax=ax1, legend=False, x=['DayOfWeek', 'HourFringe'], y='trip_distance')

        ax1.set_title("Trip Distance by DayOfWeek and HourFringe on " + getMonth(file))

        for i, child in enumerate(ax1.get_children()[:ordered.index.size]):
            ax1.text(i, child.get_bbox().y1 + 5, "%.2f" % ordered['trip_distance'][ordered.index[i]],
                     horizontalalignment='center')

        plt.tight_layout()
        plt.subplots_adjust(hspace=1)
        plt.savefig("resultados/lasttop5_day_fringe/" + getMonth(
            file) + ".png")
        plt.show()

#last5_DayWeek_HourFringe()

def top5_ByDay():
    for file in onlyfiles:
        df = pd.read_csv(mypath+'/'+file)

        grouped = df.groupby(['DayOfWeek','dropoff_date'])[["trip_distance"]].sum()
        ungrouped = grouped.reset_index()
        ordered = ungrouped.sort_values(['trip_distance'], ascending=[False]).head(5)

        print(ordered)

        ax1 = plt.subplot(1, 1, 1)
        ordered.plot(kind='bar', ax=ax1, legend=False, x=['DayOfWeek', 'dropoff_date'], y='trip_distance')

        ax1.set_title("Trip Distance on " + getMonth(file))

        for i, child in enumerate(ax1.get_children()[:ordered.index.size]):
            ax1.text(i, child.get_bbox().y1+10, ordered['trip_distance'][ordered.index[i]], horizontalalignment='center')

        plt.tight_layout()
        plt.subplots_adjust(hspace=1)
        plt.savefig("resultados/day_dropoff/" + getMonth(file) + ".png")
        plt.show()

#top5_ByDay()


def byFringe():

    for file in onlyfiles:
        df = pd.read_csv(mypath+'/'+file)

        grouped = df.groupby(['HourFringe'])[["trip_distance"]].sum()
        ungrouped = grouped.reset_index()
        ordered = ungrouped.sort_values(['trip_distance'], ascending=[False]).head(5)

        print(ordered)

        ax1 = plt.subplot(1, 1, 1)
        ordered.plot(kind='bar', ax=ax1, legend=False, x=['HourFringe'], y='trip_distance')

        ax1.set_title("Hour Fringe on " + getMonth(file))

        for i, child in enumerate(ax1.get_children()[:ordered.index.size]):
            ax1.text(i, child.get_bbox().y1 + 10, ordered['trip_distance'][ordered.index[i]],
                     horizontalalignment='center')

        plt.tight_layout()
        plt.subplots_adjust(hspace=1)
        plt.savefig(
            "resultados/top5hour_fringe/" + getMonth(file) + ".png")
        plt.show()

#byFringe()

def plotAllMonths():

    df = pd.read_csv(mypath + '/' + onlyfiles[0])

    grouped = df.groupby(['dropoff_date', 'DayOfWeek','HourFringe'])[["trip_distance"]].sum()
    ungrouped = grouped.reset_index()

    for file in onlyfiles[1:]:
        df = pd.read_csv(mypath+'/'+file)

        grouped = df.groupby(['dropoff_date','DayOfWeek', 'HourFringe'])[["trip_distance"]].sum()
        ungrouped.append(grouped.reset_index())

    ordered = ungrouped.sort_values(['trip_distance'], ascending=[False]).head(5)
    ax1 = plt.subplot(1, 1, 1)
    ordered.plot(kind='bar', ax=ax1, legend=False, x=['dropoff_date', 'DayOfWeek','HourFringe'], y='trip_distance')

    ax1.set_title("Hour Fringe on all months")

    for i, child in enumerate(ax1.get_children()[:ordered.index.size]):
        ax1.text(i, child.get_bbox().y1 + 10, ordered['trip_distance'][ordered.index[i]],
                 horizontalalignment='center')

    plt.tight_layout()
    plt.subplots_adjust(hspace=1)
    plt.savefig(
        "resultados/top5_allmonths/allMonths.png")
    plt.show()

#plotAllMonths()

# def applyZscore(vector, ungrouped):
#     df = ungrouped[(ungrouped['HourFringe'] == vector[0]) & (ungrouped['dropoff_date'] == vector[1])]
#     mean1 = df[('trip_distance','mean')]
#     std1 = df[('trip_distance','std')]
#
#     return float(vector[2]) - mean1 / std1


def zscore_FringeDay():
    for file in [onlyfiles[0]]:
        df = pd.read_csv(mypath+'/'+file)

        agg = df.groupby(['NumberHourFringe','dropoff_date'])[["trip_distance"]].agg(['mean','std'])
        ungrouped = agg.reset_index()

        new_df = pd.merge(df, ungrouped, how='inner', left_on=['NumberHourFringe','dropoff_date'], right_on=['NumberHourFringe','dropoff_date'])
        new_df['trip_distance_zscore'] = (new_df['trip_distance'] - new_df[('trip_distance', 'mean')] ) / new_df[('trip_distance', 'std')]


        print(new_df[['dropoff_date','NumberHourFringe','trip_distance','trip_distance_zscore']])

        new_df = new_df.sort_values(['dropoff_date', 'NumberHourFringe'], ascending=[True, True])

        impressions = new_df['trip_distance_zscore']
        days = new_df['dropoff_date']

        plt.plot_date(x=days, y=impressions, fmt="r-")
        plt.grid(True)
        plt.show()

        #df['trip_distance_zscore'] = df[['HourFringe','dropoff_date','trip_distance']].apply(lambda x: applyZscore(x, ungrouped), axis=1)
        #print(df[['trip_distance','trip_distance_zscore']].head(10))


#zscore_FringeDay()

def plotLinesEachMonth():
    # f, axs = plt.subplots(7, sharex=True, sharey=True)
    #
    # for index in range(len(onlyfiles)):
    #     df = pd.read_csv(mypath+'/'+onlyfiles[index])
    #
    #     grouped = df.groupby(['dropoff_date', 'NumberHourFringe'])[["trip_distance"]].sum()
    #     ungrouped = grouped.reset_index()
    #     ordered = ungrouped.sort_values(['dropoff_date','NumberHourFringe'], ascending=[True, True])
    #     ordered.set_index('dropoff_date', inplace=True)
    #     print(ordered)
    #     ordered['trip_distance'].plot(ax=axs[index], legend=False,subplots=True, x=['dropoff_date', 'NumberHourFringe'], y='trip_distance')
    #
    #
    # plt.tight_layout()
    # plt.subplots_adjust(hspace=1)
    # plt.show()

    fig, ax = plt.subplots(6, sharex=False, sharey=False)

    for index in range(len(onlyfiles)):

        file = onlyfiles[index]

        df = pd.read_csv(mypath+'/'+file)

        agg = df.groupby(['dropoff_date'])[["trip_distance"]].agg(['mean', 'std'])
        ungrouped = agg.reset_index()

        new_df = pd.merge(df, ungrouped, how='inner', left_on=['dropoff_date'], right_on=['dropoff_date'])
        new_df['trip_distance_zscore'] = (new_df['trip_distance'] - new_df[('trip_distance', 'mean')]) / new_df[
            ('trip_distance', 'std')]

        new_df = new_df.sort_values(['dropoff_date', 'NumberHourFringe'], ascending=[True, True])

        grouped = new_df.groupby(['dropoff_date'])[["trip_distance_zscore"]].sum()
        ungrouped = grouped.reset_index()

        dates = ungrouped['dropoff_date']
        nums = ungrouped['trip_distance_zscore']

        plotdf = pd.DataFrame({'date': dates, 'trip_distance': nums})
        plotdf['date'] = pd.to_datetime(plotdf['date'])
        plotdf = plotdf.set_index('date')

        #fig, ax = plt.subplots()
        ax[index].plot(plotdf.index, plotdf['trip_distance'])
        # df.plot(y='gizmos', ax=ax)
        # ax.xaxis.set_major_locator(mdates.MonthLocator(interval=8))
        ax[index].xaxis.set_major_locator(mdates.DayLocator(interval=7))
        ax[index].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        fig.autofmt_xdate()
    plt.show()


plotLinesEachMonth()