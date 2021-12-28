import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    g = sns.scatterplot(
        x="platforms",
        y="owners",
        data=data_set,
    )

    g.set_yscale('log')

    plt.title('Platforms / Owners Scatter Plot')
    plt.xlabel('Platforms')
    plt.ylabel('Owners')
    plt.show()
