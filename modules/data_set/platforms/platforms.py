import seaborn as sns
from matplotlib import pyplot as plt


def show_bar_plot(data_set):
    platforms_set = set()
    for i in data_set.platforms.str.split(';'):
        platforms_set.update(i)
    d = dict()
    platform_set = data_set.platforms.str.split(';').apply(set)
    for platform in platforms_set:
        d[platform] = platform_set.apply(lambda row: platform in row)
    ds = data_set.assign(**d)
    platform_count = ds[ds.columns.intersection(platforms_set)].sum()
    platform_count = platform_count.sort_values(ascending=False)

    print(platform_count/len(ds))

    g = sns.barplot(y=platform_count.index, x=platform_count/len(ds), color='gold')
    vals = g.get_xticks()
    g.set_xticklabels(['{:,.0%}'.format(x) for x in vals])
    plt.title('Platforms\' Percentages in All Games')
    plt.xlabel('Percentage')
    plt.ylabel('Platforms')
    plt.show()
