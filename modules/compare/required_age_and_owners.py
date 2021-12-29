import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(data_set):
    sns.scatterplot(
        x="required_age",
        y="owners",
        data=data_set,
    )

    plt.title('Required Age / Owners Scatter Plot')
    plt.xlabel('Required Age')
    plt.ylabel('Owners')
    plt.show()


def show_regression(data_set):
    x_var = pd.DataFrame(data_set["required_age"])
    y_var = pd.DataFrame(data_set["owners"])

    model = linear_model.LinearRegression()
    model.fit(x_var, y_var)
    model.predict(x_var)

    sns.regplot(x=x_var, y=y_var, color="r")
    plt.title('Required Age / Owners Regression')
    plt.xlabel('Required Age')
    plt.ylabel('Owners')
    plt.show()

