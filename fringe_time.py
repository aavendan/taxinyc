#coding:latin-1
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

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
        plt.savefig("C:\\Users\\aavendan\\PycharmProjects\\taxinyc\\resultados\\firsttop5_day_fringe\\" + getMonth(
            file) + ".png")
        plt.show()

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
        plt.savefig("C:\\Users\\aavendan\\PycharmProjects\\taxinyc\\resultados\\lasttop5_day_fringe\\" + getMonth(
            file) + ".png")
        plt.show()

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
        plt.savefig("C:\\Users\\aavendan\\PycharmProjects\\taxinyc\\resultados\\day_dropoff\\" + getMonth(file) + ".png")
        plt.show()


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
            "C:\\Users\\aavendan\\PycharmProjects\\taxinyc\\resultados\\top5hour_fringe\\" + getMonth(file) + ".png")
        plt.show()


def plotAllMonths():

    df = pd.read_csv(mypath + '/' + onlyfiles[0])

    grouped = df.groupby(['dropoff_date', 'DayOfWeek','HourFringe'])[["trip_distance"]].sum()
    ungrouped = grouped.reset_index()

    for file in onlyfiles[1:]:
        df = pd.read_csv(mypath+'/'+file)

        grouped = df.groupby(['DayOfWeek', 'HourFringe'])[["trip_distance"]].sum()
        ungrouped.append(grouped.reset_index())

    ordered = ungrouped.sort_values(['trip_distance'], ascending=[False]).head(5)
    ax1 = plt.subplot(1, 1, 1)
    ordered.plot(kind='bar', ax=ax1, legend=False, x=['dropoff_date', 'DayOfWeek','HourFringe'], y='trip_distance')

    ax1.set_title("Hour Fringe on " + getMonth(file))

    for i, child in enumerate(ax1.get_children()[:ordered.index.size]):
        ax1.text(i, child.get_bbox().y1 + 10, ordered['trip_distance'][ordered.index[i]],
                 horizontalalignment='center')

    plt.tight_layout()
    plt.subplots_adjust(hspace=1)
    plt.savefig(
        "C:\\Users\\aavendan\\PycharmProjects\\taxinyc\\resultados\\top5_allmonths\\" + getMonth(file) + ".png")
    plt.show()

def plotLinesEachMonth():
    f, axs = plt.subplots(7, sharex=True, sharey=True)

    for index in range(len(onlyfiles)):
        df = pd.read_csv(mypath+'/'+onlyfiles[index])

        grouped = df.groupby(['dropoff_date', 'NumberHourFringe'])[["trip_distance"]].sum()
        ungrouped = grouped.reset_index()
        ordered = ungrouped.sort_values(['dropoff_date','NumberHourFringe'], ascending=[True, True])
        ordered.set_index('dropoff_date', inplace=True)
        print(ordered)
        ordered['trip_distance'].plot(ax=axs[index], legend=False,subplots=True, x=['dropoff_date', 'NumberHourFringe'], y='trip_distance')


    plt.tight_layout()
    plt.subplots_adjust(hspace=1)
    plt.show()



top5_ByDay()
plotAllMonths()