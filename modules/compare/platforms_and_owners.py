import seaborn as sns
from matplotlib import pyplot as plt


def show_box_plot(data_set):
    sns.boxplot(
        x="platforms_first",
        y="owners",
        data=data_set,
    )

    plt.title('Platforms / Owners Box Plot')
    plt.xlabel('Platforms')
    plt.ylabel('Owners')
    plt.show()
