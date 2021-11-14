import pandas as pd

from matplotlib import rcParams
import seaborn as sns


def initialize_data_set():
    data_set = pd.read_csv('C:/Users/hazar/PycharmProjects/steam_data_analysis/assets/steam.csv')
    print(f'Number of games in dataset: {len(data_set)}')

    data_set.head()

    data_set = data_set.assign(**{'overall_reviews': data_set.positive_ratings + data_set.negative_ratings})
    data_set = data_set.assign(**{'positive_rate': data_set.positive_ratings / data_set.overall_reviews})

    data_set = data_set.assign(**{'has_achievements': data_set.achievements > 0})
    data_set = data_set.assign(**{'free': data_set.price == 0})

    data_set['release_date'] = pd.to_datetime(data_set['release_date'])


def configure_table():
    rcParams['figure.figsize'] = 8, 6
    rcParams['axes.titlesize'] = 20
    rcParams['axes.labelsize'] = 16
    rcParams['xtick.labelsize'] = 16
    rcParams['ytick.labelsize'] = 16
    rcParams['legend.fontsize'] = 12

    palette = sns.color_palette("Blues_d")
    default_color = palette[2]
