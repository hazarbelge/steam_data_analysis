import seaborn as sns
from matplotlib import pyplot as plt


def show_bar_plot(data_set):
    categories_set = set()
    for i in data_set.categories.str.split(';'):
        categories_set.update(i)
    d = dict()
    category_set = data_set.categories.str.split(';').apply(set)
    for category in categories_set:
        d[category] = category_set.apply(lambda row: category in row)
    ds = data_set.assign(**d)
    category_count = ds[ds.columns.intersection(categories_set)].sum()
    category_count = category_count.sort_values(ascending=False)

    g = sns.barplot(y=category_count.index, x=category_count/len(ds), color='gold')
    vals = g.get_xticks()
    g.set_xticklabels(['{:,.0%}'.format(x) for x in vals])
    plt.title('Categories\' Percentages in All Games')
    plt.xlabel('Percentage')
    plt.ylabel('Categories')
    plt.show()
