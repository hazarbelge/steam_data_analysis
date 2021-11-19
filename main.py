from modules.compare import positive_rate_and_price, released_date_and_price, overall_reviews_and_positive_rate, \
    achievements_and_owners
from modules.csv import init_csv
from modules.data_set.achievements import achievements
from modules.data_set.age_rating import age_rating
from modules.data_set.categories import categories
from modules.data_set.english_support import english_support
from modules.data_set.genres import genres
from modules.data_set.owners import owners
from modules.data_set.platforms import platforms
from modules.data_set.playtime import playtime
from modules.data_set.reviews import reviews
from modules.data_set.price import price
from modules.data_set.release_date import release_date


def initialize_analysis():
    ds = init_csv.initialize_data_set()
    init_csv.configure_rc_params()
    return ds


def achievements_analysis():
    achievements.show_pie_chart(data_set)
    achievements.show_hist_plot(data_set)


def age_rating_analysis():
    age_rating.show_pie_chart_has_age_rating(data_set)
    age_rating.show_pie_chart_with_age_rating(data_set)


def categories_analysis():
    categories.show_bar_plot(data_set)


def english_support_analysis():
    english_support.show_pie_chart(data_set)


def genres_analysis():
    genres.show_bar_plot(data_set)


def owners_analysis():
    owners.show_counter_plot(data_set)


def platforms_analysis():
    platforms.show_bar_plot(data_set)


def price_analysis():
    price.show_pie_chart(data_set)
    price.show_hist_plot(data_set)


def playtime_analysis():
    playtime.show_hist_plot(data_set)
    playtime.show_pie_chart(data_set)


def release_date_analysis():
    release_date.show_bar_plot(data_set)


def reviews_analysis():
    reviews.show_dist_plot(data_set)


def scatter_plots():
    achievements_and_owners.show_scatter_plot(data_set)
    overall_reviews_and_positive_rate.show_scatter_plot(data_set)
    positive_rate_and_price.show_scatter_plot(data_set)
    released_date_and_price.show_scatter_plot(data_set)


def run_analysis():
    #achievements_analysis()
    #age_rating_analysis()
    #categories_analysis()
    #english_support_analysis()
    #genres_analysis()
    #owners_analysis()
    #platforms_analysis()
    price_analysis()
    #playtime_analysis()
    #release_date_analysis()
    #reviews_analysis()
    #scatter_plots()


data_set = initialize_analysis()
run_analysis()

