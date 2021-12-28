import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    g = sns.scatterplot(
        x="developers",
        y="owners",
        data=data_set,
    )

    g.set_yscale('log')

    plt.title('Developers / Owners Scatter Plot')
    plt.xlabel('Developers')
    plt.ylabel('Owners')
    plt.show()
