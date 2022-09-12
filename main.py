from collate_log import read_data, combine_folder, combine_logs, pd_to_excel
from monarch_func import ignore_outliers
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime


# by Tyler Fulghum, monarch curve testing section.
# Reads text file into pandas dataframe

def main():
    df = combine_logs("08_31_2022")
    df = ignore_outliers(df," UVB_u")
    print(df)
    df.boxplot(" UVB_u")
    plt.show()

if __name__ == "__main__":
    main()
