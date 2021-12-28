import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    g = sns.scatterplot(
        x="has_age_rating",
        y="owners",
        data=data_set,
    )

    g.set_yscale('log')

    plt.title('Age Rating / Owners Scatter Plot')
    plt.xlabel('Age Rating')
    plt.ylabel('Owners')
    plt.show()
