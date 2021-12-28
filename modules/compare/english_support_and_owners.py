import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    g = sns.scatterplot(
        x="english_support",
        y="owners",
        data=data_set,
    )

    g.set_yscale('log')

    plt.title('English Support / Owners Scatter Plot')
    plt.xlabel('English Support')
    plt.ylabel('Owners')
    plt.show()
