from modules.csv import init_csv
from modules.data_set.achievements import achievements
from modules.data_set.age_rating import age_rating
from modules.data_set.english_support import english_support
from modules.data_set.owners import owners
from modules.data_set.release_date import release_date


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


def owners_analysis():
    owners.show_counter_plot(data_set)


def release_date_analysis():
    release_date.show_bar_plot(data_set)


def run_analysis():
    achievements_analysis()
    age_rating_analysis()
    english_support_analysis()
    owners_analysis()
    release_date_analysis()


data_set = initialize_analysis()
run_analysis()

