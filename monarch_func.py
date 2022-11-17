import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# Receives a collated pandas dataframe created by the combine_logs function in collate_log.py
def ignore_outliers(df, field):
    # Calculating 1st and 3rd quartiles
    for x in [field]:
        q75, q25 = np.percentile(df.loc[:, x], [75, 25])
        intr_qr = q75 - q25

        max = q75 + (3 * intr_qr)
        min = q25 - (3 * intr_qr)

        df.loc[df[x] < min, x] = np.nan
        df.loc[df[x] > max, x] = np.nan

    return df


def remove_outliers(df, n_std):
    for col in df.columns:
        mean = df[col].mean()
        sd = df[col].std()
        df = df[(df[col] <= mean + (n_std * sd))]

    return df


def get_heatmap(df):
    ax = sns.heatmap(df.corr())
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    plt.tight_layout()
    plt.show()
    return
