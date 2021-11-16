import seaborn as sns
from matplotlib import pyplot as plt


def show_pie_chart(data_set):
    not_played_dict = dict((data_set.average_playtime == 0).value_counts())
    labels = 'Have playtime', 'Nobody played it'
    sizes = [not_played_dict[False], not_played_dict[True]]
    colors = ['gold', 'red']
    explode = (0.15, 0)

    with sns.color_palette('colorblind'):
        plt.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            shadow=True,
            startangle=120,
        )

    plt.title("Have Played")
    plt.axis('equal')
    plt.show()


def show_dist_plot(data_set):
    g = sns.distplot(data_set.average_playtime, kde=False, rug=False)
    g.set_yscale('log')

    plt.title('Avg Playtime / Game Count')
    plt.ylabel("Game Count")
    plt.xlabel("Average Playtime (hours)")
    plt.show()
