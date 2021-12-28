import seaborn as sns
from matplotlib import pyplot as plt


def show_box_plot(data_set):
    data_set = data_set[data_set.owners > 10000000]

    fig = sns.boxplot(
        x="developer",
        y="owners",
        data=data_set,
    )

    fig.axis(ymin=0, ymax=8000000)

    plt.title('Developer / Owners Box Plot')
    plt.xlabel('Developer')
    plt.ylabel('Owners')
    plt.show()
