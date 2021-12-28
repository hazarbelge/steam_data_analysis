import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    g = sns.scatterplot(
        x="publishers",
        y="owners",
        data=data_set,
    )

    g.set_yscale('log')

    plt.title('Publisher / Owners Scatter Plot')
    plt.xlabel('Publisher')
    plt.ylabel('Owners')
    plt.show()
