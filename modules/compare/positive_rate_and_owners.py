import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(data_set):
    sns.scatterplot(
        x="positive_rate",
        y="owners",
        data=data_set,
    )

    plt.title('Positive Rate / Owners Scatter Plot')
    plt.xlabel('Positive Rate')
    plt.ylabel('Owners')
    plt.show()


def show_regression(data_set):
    x_var = pd.DataFrame(data_set["positive_rate"])
    y_var = pd.DataFrame(data_set["owners"])

    model = linear_model.LinearRegression()
    model.fit(x_var, y_var)
    model.predict(x_var)

    sns.regplot(x=x_var, y=y_var, color="r")
    plt.title("Positive Rate / Owners Regression")
    plt.xlabel('Positive Rate')
    plt.ylabel('Owners')
    plt.show()
