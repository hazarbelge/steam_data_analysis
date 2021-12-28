import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    g = sns.scatterplot(
        x="categories",
        y="owners",
        data=data_set,
    )

    g.set_yscale('log')

    plt.title('Categories / Owners Scatter Plot')
    plt.xlabel('Categories')
    plt.ylabel('Owners')
    plt.show()
