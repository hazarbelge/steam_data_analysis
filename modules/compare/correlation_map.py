import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def show_correlation_map(data_set):
    f, ax = plt.subplots()
    hm = sb.heatmap(data_set.corr(), annot=True, linewidths=.5, fmt=".2f", ax=ax, cmap="Wistia_r")
    hm.set_yticklabels(labels=data_set.corr().columns.values, va="top", rotation=22)
    hm.set_xticklabels(labels=data_set.corr().columns.values, ha="right", rotation=22)
    plt.title("Correlation Map")
    plt.show()


def show_correlation_matrix(data_set):
    f, ax = plt.subplots()
    hm = sb.heatmap(data_set.corr(), vmax=.8, square=True)
    hm.set_yticklabels(labels=data_set.corr().columns.values, va="top", rotation=22)
    hm.set_xticklabels(labels=data_set.corr().columns.values, ha="right", rotation=22)
    plt.title("Correlation Matrix")
    plt.show()