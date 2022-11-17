from collate_log import read_data, combine_folder, combine_logs, pd_to_excel
from monarch_func import ignore_outliers, get_heatmap, remove_outliers

from matplotlib import pyplot as plt
from scipy import stats
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import pydot
import pandas as pd
import numpy as np
import os

# by Tyler Fulghum, monarch curve testing section.
# Reads text file into pandas dataframe


def main():
    # Fetching data
    df = combine_logs("completedata")
    kdata = combine_logs("kacie")
    df = pd.concat([df, kdata])
    df = df.iloc[:, 1:-1]                           # Removing NaN row

    # Handling outliers
    get_heatmap(df)
    df1 = remove_outliers(df, 3)                    # df1 is data with rescaled outliers
    df1 = df1.drop(' PyroT_u [C]', axis=1)
    get_heatmap(df1)
    # Prepping Train / Test Split
    pyro = np.array(df1[' Pyro [uV]'])              # Data we want to match to
    feature_list = list(df1.columns)
    sensordata = df1.drop(' Pyro [uV]', axis=1)     # Dropping actual data
    sensordata = np.array(df1)                      # Convert to NP array
    train_features, test_features, train_labels, test_labels = train_test_split(sensordata, pyro, test_size=0.25, random_state=42)

    # Sklearn Random forest
    rf = RandomForestRegressor(n_estimators=1000, random_state=42)
    rf.fit(train_features, train_labels)
    predictions = rf.predict(test_features)

    # Calculate the absolute errors
    errors = abs(predictions - test_labels)
    print('Mean Absolute Error:', round(np.mean(errors), 2))

    # Calculate mean absolute percentage error (MAPE)
    mape = 100 * (errors / test_labels)
    # Calculate and display accuracy
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')

    # Tree printing
    # Limit depth of tree to 3 levels
    #rf_small = RandomForestRegressor(n_estimators=10, max_depth=3)
    #rf_small.fit(train_features, train_labels)
    # Extract the small tree
    #tree_small = rf_small.estimators_[5]
    # Save the tree as a png image
    #export_graphviz(tree_small, out_file='small_tree.dot', feature_names=feature_list, rounded=True, precision=1)
    #(graph,) = pydot.graph_from_dot_file('small_tree.dot')
    #graph.write_png('small_tree.png');


if __name__ == "__main__":
    main()
