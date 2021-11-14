from modules.csv import init_csv
from modules.data_set.achievements import achievements
from modules.data_set.age_rating import age_rating
from modules.data_set.english_support import english_support


def initialize_analysis():
    ds = init_csv.initialize_data_set()
    init_csv.configure_rc_params()
    return ds


def achievements_analysis():
    achievements.show_pie_chart(data_set)


def age_rating_analysis():
    age_rating.show_pie_chart_has_age_rating(data_set)
    age_rating.show_pie_chart_with_age_rating(data_set)


def english_support_analysis():
    english_support.show_pie_chart(data_set)


data_set = initialize_analysis()

achievements_analysis()
age_rating_analysis()
english_support_analysis()
