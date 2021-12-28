import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def show_counter_plot(data_set):
    a = data_set[data_set.owners > 0]
    owners = pd.Series(a.owners)

    sns.histplot(
        owners,
        kde=True,
        color='purple',
        bins=1000,
        fill=True,
    )

    plt.title('Histogram of Owners')
    plt.xlabel('Owners\nMean : {:.2f} Median : {:.2f} Mode : {:.2f} Max : {:.2f}'
               .format(owners.mean(), owners.median().mean(), owners.mode().mean(), owners.max()))
    plt.ylabel('Game Count')
    plt.show()

