import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(data_set):
    data_set = data_set[data_set.achievements > 0]
    sns.scatterplot(
        x="achievements",
        y="owners",
        data=data_set,
    )

    plt.title('Achievements / Owners Scatter Plot')
    plt.xlabel('Achievements')
    plt.ylabel('Owners')
    plt.show()


def show_regression(data_set):
    data_set = data_set[data_set.achievements > 0]
    x_var = pd.DataFrame(data_set["achievements"])
    y_var = pd.DataFrame(data_set["owners"])

    model = linear_model.LinearRegression()
    model.fit(x_var, y_var)
    model.predict(x_var)

    sns.regplot(x=x_var, y=y_var, color="r")
    plt.title("Achievements / Owners Regression")
    plt.show()
