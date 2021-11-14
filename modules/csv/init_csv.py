from matplotlib import rcParams
import seaborn as sns
import pandas as pd


def initialize_data_set():
    data_set = pd.read_csv('C:/Users/hazar/PycharmProjects/steam_data_analysis/assets/steam.csv')
    print(f'Number of games in dataset: {len(data_set)}')

    data_set.head()

    data_set = data_set.assign(**{'overall_reviews': data_set.positive_ratings + data_set.negative_ratings})
    data_set = data_set.assign(**{'positive_rate': data_set.positive_ratings / data_set.overall_reviews})

    data_set = data_set.assign(**{'has_age_rating': data_set.required_age > 0})

    data_set = data_set.assign(**{'has_achievements': data_set.achievements > 0})

    data_set = data_set.assign(**{'free': data_set.price == 0})

    data_set['release_date'] = pd.to_datetime(data_set['release_date'])

    return data_set


def configure_rc_params():
    rcParams['figure.figsize'] = 8, 6
    rcParams['axes.titlesize'] = 18
    rcParams['axes.labelsize'] = 14
    rcParams['xtick.labelsize'] = 14
    rcParams['ytick.labelsize'] = 14
    rcParams['legend.fontsize'] = 11
    return rcParams
