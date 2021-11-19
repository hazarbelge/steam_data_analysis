import seaborn as sns
import pandas as pd
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


def show_hist_plot(data_set):
    a = data_set[data_set.achievements >= 0]
    achievements = pd.Series(a[a.achievements < 500].achievements)

    sns.histplot(
        achievements,
        kde=True,
        color='purple',
        bins=100,
        fill=True,
    )

    plt.title('Histogram of Achievements')
    plt.xlabel('Achievements\nMean : {:.2f} Median : {:.2f} Mode : {:.2f} Max : {:.2f}'
               .format(achievements.mean(), achievements.median().mean(), achievements.mode().mean(), achievements.max()))
    plt.ylabel('Game Count')
    plt.show()
