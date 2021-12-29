import seaborn as sns
from matplotlib import pyplot as plt


def show_scatter_plot(data_set):
    g = sns.scatterplot(
        x="overall_reviews",
        y="positive_rate",
        data=data_set,
    )

    y_ticks = g.get_yticks()
    g.set_yticklabels(['{:,.0%}'.format(x) for x in y_ticks])

    plt.title('Overall Reviews / Positive Rate Scatter Plot')
    plt.xlabel('Overall Reviews')
    plt.ylabel('Positive Rate')
    plt.show()
