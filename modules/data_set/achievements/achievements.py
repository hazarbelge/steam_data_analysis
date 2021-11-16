import seaborn as sns
from matplotlib import pyplot as plt


def show_pie_chart(data_set):
    achievement_dict = dict(data_set.has_achievements.value_counts())
    labels = 'Has Achievements', 'No Achievements'
    sizes = [achievement_dict[0], achievement_dict[1]]
    colors = ['lightskyblue', 'gold']
    explode = (0, 0.1)

    with sns.color_palette("colorblind"):
        plt.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            shadow=True,
            startangle=45,
        )

    plt.title('Achievements')
    plt.axis('equal')
    plt.show()
