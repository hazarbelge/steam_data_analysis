import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def show_counter_plot(data_set):
    mask_1 = data_set.owners.isin(
        [
            '0-20000',
        ]
    )
    data_set.loc[mask_1, 'owners'] = '0-20K'

    mask_2 = data_set.owners.isin(
        [
            '20000-50000',
            '50000-100000',
        ]
    )
    data_set.loc[mask_2, 'owners'] = '20K-100K'

    mask_3 = data_set.owners.isin(
        [
            '100000-200000',
        ]
    )
    data_set.loc[mask_3, 'owners'] = '100K-200K'

    mask_4 = data_set.owners.isin(
        [
            '200000-500000',
        ]
    )
    data_set.loc[mask_4, 'owners'] = '200K-500K'

    mask_5 = data_set.owners.isin(
        [
            '500000-1000000',
        ]
    )
    data_set.loc[mask_5, 'owners'] = '500K-1M'

    mask_6 = data_set.owners.isin(
        [
            '1000000-2000000',
        ]
    )
    data_set.loc[mask_6, 'owners'] = '1M-2M'

    mask_7 = data_set.owners.isin(
        [
            '2000000-5000000',
            '5000000-10000000',
            '10000000-20000000',
            '20000000-50000000',
            '50000000-100000000',
            '100000000-200000000',
        ]
    )
    data_set.loc[mask_7, 'owners'] = '2M+'

    sns.countplot(
        data=data_set,
        x='owners',
        order=data_set.owners.value_counts().index,
        color='gold',
    )

    plt.ylabel('Total Game Count')
    plt.xlabel('Owner Count')
    plt.title('Owner/Game Count')
    plt.show()

