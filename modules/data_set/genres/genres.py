import seaborn as sns
from matplotlib import pyplot as plt


def show_bar_plot(data_set):
    genres = data_set['genres'].apply(lambda x: x.split(';')[0]).value_counts()

    g = sns.barplot(y=genres.index, x=genres/len(data_set), color='gold')
    vals = g.get_xticks()
    g.set_xticklabels(['{:,.0%}'.format(x) for x in vals])
    plt.title('Genres\' Percentages in All Games')
    plt.xlabel('Percentage')
    plt.ylabel('Premier Genres of Games')
    plt.show()
