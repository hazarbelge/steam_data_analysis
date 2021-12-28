import seaborn as sns
from matplotlib import pyplot as plt


def show_box_plot(data_set):
    data_set = data_set[data_set.owners > 500000]

    fig = sns.boxplot(
        x="categories_first",
        y="owners",
        data=data_set,
    )

    fig.axis(ymin=0, ymax=8000000)

    plt.title('Categories / Owners Box Plot')
    plt.xlabel('Categories')
    plt.ylabel('Owners')
    plt.show()
