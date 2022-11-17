import numpy as np
import pandas as pd
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


def get_joint_plot(df):
    sns.set_theme(style="whitegrid")

    # Show the joint distribution using kernel density estimation
    g = sns.jointplot(
        data=df,
        x=" Temp RTC [C]", y=" White_u", hue="Month",
        kind="kde")
    plt.tight_layout()
    plt.show()
    return

def parse_dateTime(df):
    # Changing Date to a more readable format

    df["Year"] = 0
    df["Month"] = 0
    df["Day"] = 0

    df['Year'] = df['Time [UTC]'].apply(lambda x: x[0:4])
    df['Year'] = pd.to_numeric(df['Year'])
    df['Day'] = df['Time [UTC]'].apply(lambda x: x[8:10])
    df['Day'] = pd.to_numeric(df['Day'])

    df.loc[df['Time [UTC]'].str.contains('/07/'), 'Month'] = 7
    df.loc[df['Time [UTC]'].str.contains('/08/'), 'Month'] = 8
    df.loc[df['Time [UTC]'].str.contains('/09/'), 'Month'] = 9
    df.loc[df['Time [UTC]'].str.contains('/10/'), 'Month'] = 10
    df.loc[df['Time [UTC]'].str.contains('/11/'), 'Month'] = 11
    df.loc[df['Time [UTC]'].str.contains('/12/'), 'Month'] = 12

    return df
