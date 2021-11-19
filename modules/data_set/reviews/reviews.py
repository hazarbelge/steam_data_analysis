import seaborn as sns
from matplotlib import pyplot as plt


def show_dist_plot(data_set):
    p_rate = data_set[data_set.overall_reviews > 100].positive_rate

    sns.distplot(
        p_rate,
        kde=False,
    )

    plt.xlabel('Positive Rate\nMean : {:.2f} Median : {:.2f} Mode : {:.2f}'
               .format(p_rate.mean(), p_rate.median().mean(), p_rate.mode().mean()))
    plt.ylabel('Game Count')
    plt.title('Distribution of Positive Rate (>100 Review)')
    plt.show()
