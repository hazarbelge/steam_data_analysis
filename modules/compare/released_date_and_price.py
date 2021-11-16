import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    sns.scatterplot(
        x="release_date",
        y="price",
        data=data_set[data_set.release_date.dt.year & (data_set.price <= 200)],
    )

    plt.title('Release Date / Price Scatter Plot')
    plt.xlabel('Release Date')
    plt.ylabel('Price')
    plt.show()
