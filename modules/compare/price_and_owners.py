import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(data_set):
    sns.scatterplot(
        x="price",
        y="owners",
        data=data_set,
    )

    plt.title('Price / Owners Scatter Plot')
    plt.xlabel('Price')
    plt.ylabel('Owners')
    plt.show()


def show_regression(data_set):
    x_var = pd.DataFrame(data_set["price"])
    y_var = pd.DataFrame(data_set["owners"])

    model = linear_model.LinearRegression()
    model.fit(x_var, y_var)
    model.predict(x_var)

    sns.regplot(x=x_var, y=y_var, color="r")
    plt.title('Price / Owners Regression')
    plt.xlabel('Price')
    plt.ylabel('Owners')
    plt.show()

