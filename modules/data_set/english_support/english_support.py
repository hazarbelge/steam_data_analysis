import seaborn as sns
from matplotlib import pyplot as plt


def show_pie_chart(data_set):
    english_dict = dict(data_set.english.value_counts())
    labels = 'Non-English', 'English'
    sizes = [english_dict[0], english_dict[1]]
    colors = ['blue', 'red']
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

    plt.title('English Support')
    plt.axis('equal')
    plt.show()
