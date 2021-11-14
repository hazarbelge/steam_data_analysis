import seaborn as sns
from matplotlib import pyplot as plt


def show_bar_plot(data_set):
    yearly = data_set.groupby(data_set.release_date.dt.year.rename('release_year')) \
        .agg('count').appid.rename('count')

    sep_year = 2019

    yearly_part = yearly[yearly.index < sep_year]
    sns.barplot(y=yearly_part, x=yearly_part.index, color='red')
    plt.title(f'Total games released in 1997-{sep_year} years')
    plt.xlabel('Year')
    plt.ylabel('Total games')
    plt.show()
