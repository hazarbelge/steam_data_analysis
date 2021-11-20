import seaborn as sns
from matplotlib import pyplot as plt


def show_hist_plot(data_set):
    p_rate = data_set[data_set.overall_reviews > 100].positive_rate

    sns.histplot(
        p_rate,
        kde=True,
        bins=100,
    )

    plt.xlabel('Positive Rate\nMean : {:.4f} Median : {:.4f} Mode : {:.4f}'
               .format(p_rate.mean(), p_rate.median().mean(), p_rate.mode().mean()))
    plt.ylabel('Game Count')
    plt.title('Distribution of Positive Rate (>100 Review)')
    plt.show()
