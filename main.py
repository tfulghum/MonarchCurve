from collate_log import read_data, combine_folder, combine_logs, pd_to_excel
from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime

# by Tyler Fulghum, monarch curve testing section.
# Reads text file into pandas dataframe

def main():
    df = combine_logs("08_31_2022")
    strtime = df["Time [UTC]"]
    strtime = strtime.tolist()
    i = 0

    for x in strtime:
        strtime[i] = strtime[i].split(" ")
        strtime[i] = strtime[i][1]
        strtime[i] = strtime[i].replace(":", "")
        strtime[i] = int(strtime[i])
        i += 1

    x = df[" White_u"]
    print(x)
    print(type(x))

    pd_to_excel(df, "8_22")

    plt.title("Matplotlib demo")
    plt.xlabel("Time")
    plt.ylabel("White_u")
    plt.plot(strtime, x)
    plt.show()


if __name__ == "__main__":
    main()
