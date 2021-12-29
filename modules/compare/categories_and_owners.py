import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd


def show_box_plot(data_set):
    categories_first_6 = pd.Series(data_set.categories_first.value_counts().sort_values(ascending=False).head(6))
    print("English" in categories_first_6.keys())

    data_set["categories_check"] = data_set['categories_first'].apply(
        lambda val: str(val) if str(val) in categories_first_6.keys() else "false")

    data_set = data_set[data_set.categories_check != "false"]
    sns.boxplot(
        x="categories_first",
        y="owners",
        data=data_set,
    )

    plt.title('Categories / Owners Box Plot')
    plt.xlabel('Categories')
    plt.ylabel('Owners')
    plt.show()
