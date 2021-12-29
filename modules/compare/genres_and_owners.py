import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd


def show_box_plot(data_set):
    genres_first_10 = pd.Series(data_set.genres_first.value_counts().sort_values(ascending=False).head(10))
    print("English" in genres_first_10.keys())

    data_set["genres_check"] = data_set['genres_first'].apply(
        lambda val: str(val) if str(val) in genres_first_10.keys() else "false")

    data_set = data_set[data_set.genres_check != "false"]
    sns.boxplot(
        x="genres_first",
        y="owners",
        data=data_set,
    )

    plt.title('Genres / Owners Box Plot')
    plt.xlabel('Genres')
    plt.ylabel('Owners')
    plt.show()
