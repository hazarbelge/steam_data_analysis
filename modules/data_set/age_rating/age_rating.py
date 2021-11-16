import seaborn as sns
from matplotlib import pyplot as plt


def show_pie_chart_has_age_rating(data_set):
    age_dict = dict(data_set.has_age_rating.value_counts())
    labels = 'Without age rating', 'Have an age rating'
    sizes = [age_dict[0], age_dict[1]]
    colors = ['pink', 'lightskyblue']
    explode = (0, 0.3)

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

    plt.title("Age Rating Limitation")
    plt.axis('equal')
    plt.show()


def show_pie_chart_with_age_rating(data_set):
    age_dict = dict(data_set.required_age.value_counts())
    labels = '3+', '7+', '12+', '16+', '18+'
    sizes = [age_dict[3], age_dict[7], age_dict[12], age_dict[16], age_dict[18]]
    colors = ['lightskyblue', 'green', 'gold', 'pink', 'purple']
    explode = (0, 0.1, 0.075, 0.05, 0.025)

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

    plt.title("Age Rating")
    plt.axis('equal')
    plt.show()

