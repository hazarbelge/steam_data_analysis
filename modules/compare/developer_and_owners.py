import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd


def show_box_plot(data_set):
    developer_first_6 = pd.Series(data_set.developer.value_counts().sort_values(ascending=False).head(6))
    print("English" in developer_first_6.keys())

    data_set["developer_check"] = data_set['developer'].apply(
        lambda val: str(val) if str(val) in developer_first_6.keys() else "false")

    data_set = data_set[data_set.developer_check != "false"]
    sns.boxplot(
        x="developer",
        y="owners",
        data=data_set,
    )

    plt.title('Developer / Owners Box Plot')
    plt.xlabel('Developer')
    plt.ylabel('Owners')
    plt.show()
