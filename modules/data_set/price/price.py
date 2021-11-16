import seaborn as sns
from matplotlib import pyplot as plt


def show_pie_chart(data_set):
    free_dict = dict(data_set.free.value_counts())
    labels = 'Free', 'Paid'
    sizes = [free_dict[True], free_dict[False]]
    colors = ['gold', 'pink']
    explode = (0.2, 0)

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

    plt.title("Free/Paid Games")
    plt.axis('equal')
    plt.show()


def show_dist_plot(data_set):
    sns.distplot(data_set[data_set.price <= 200].price, kde=False).set_yscale('log')
    plt.title('Price / Game Count')
    plt.xlabel('Price')
    plt.ylabel('Game Count')
    plt.show()
