import seaborn as sns
import pandas as pd

from matplotlib import pyplot as plt


def show_pie_chart(data_set):
    not_played_dict = dict((data_set.average_playtime == 0).value_counts())
    labels = 'Have playtime', 'Nobody played it'
    sizes = [not_played_dict[False], not_played_dict[True]]
    colors = ['gold', 'red']
    explode = (0.15, 0)

    with sns.color_palette('colorblind'):
        plt.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            shadow=True,
            startangle=120,
        )

    plt.title("Have Played")
    plt.axis('equal')
    plt.show()


def show_hist_plot(data_set):
    average_playtime = pd.Series(data_set[data_set.average_playtime > 0].average_playtime)

    sns.histplot(
        average_playtime,
        kde=True,
        color='purple',
        bins=100,
        fill=True,
    )

    plt.title('Histogram of Average Playtime')
    plt.xlabel('Average Playtime\nMean : {:.2f} Median : {:.2f} Mode : {:.2f} Max : {:.2f}'
        .format(
            average_playtime.mean(),
            average_playtime.median().mean(),
            average_playtime.mode().mean(),
            average_playtime.max(),
        )
    )
    plt.ylabel('Game Count')
    plt.show()
