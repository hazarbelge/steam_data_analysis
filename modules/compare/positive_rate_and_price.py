import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    g = sns.scatterplot(
        x="price",
        y="positive_rate",
        data=data_set[(data_set.price <= 200) & (data_set.overall_reviews > 500)],
    )
    y_ticks = g.get_yticks()
    g.set_yticklabels(['{:,.0%}'.format(x) for x in y_ticks])

    plt.title('Price / Positive Rate Scatter Plot')
    plt.xlabel('Price')
    plt.ylabel('Positive Rate (>500 reviews)')
    plt.show()
