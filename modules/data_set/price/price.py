import seaborn as sns
import pandas as pd

from matplotlib import pyplot as plt


def show_pie_chart(data_set):
    free_dict = dict(data_set.free.value_counts())
    labels = 'Free', 'Paid'
    sizes = [free_dict[True], free_dict[False]]
    colors = ['gold', 'pink']
    explode = (0.2, 0)

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

    plt.title("Free/Paid Games")
    plt.axis('equal')
    plt.show()


def show_hist_plot(data_set):
    prices = pd.Series(data_set[data_set.price >= 0].price)

    sns.histplot(
        prices,
        kde=True,
        color='purple',
        bins=100,
        fill=True,
    )

    plt.title('Histogram of Price')
    plt.xlabel('Price\nMean : {:.2f} Median : {:.2f} Mode : {:.2f} Max : {:.2f}'
               .format(prices.mean(), prices.median().mean(), prices.mode().mean(), prices.max()))
    plt.ylabel('Game Count')
    plt.show()
