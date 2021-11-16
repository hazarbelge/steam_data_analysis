import seaborn as sns
from matplotlib import pyplot as plt


def show_dist_plot(data_set):
    sns.distplot(
        data_set[data_set.overall_reviews > 100].positive_rate,
        kde=False,
    )

    plt.xlabel('Positive rate')
    plt.ylabel('Review Count')
    plt.title('Distribution of positive rate of user reviews for games with over 100 reviews')
    plt.show()
