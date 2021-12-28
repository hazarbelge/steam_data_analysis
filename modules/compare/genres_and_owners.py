import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    g = sns.scatterplot(
        x="genres",
        y="owners",
        data=data_set,
    )

    g.set_yscale('log')

    plt.title('Genres / Owners Scatter Plot')
    plt.xlabel('Genres')
    plt.ylabel('Owners')
    plt.show()
