import os
import pandas as pd
import openpyxl


# Returns a dataframe of the target file

def read_data(log_name, log_date):
    pa = os.path.dirname(os.path.abspath(__file__))
    print(pa)
    pa = os.path.join(pa, "mdata", log_date, "Logs", log_name)
    df = pd.read_csv(pa, sep=",")

    return df


# Takes in folder that you want to apply the function to. Will have multiple headers, meant to give an overview.

def combine_folder(folder_name):
    # Blank dictionary
    df_inlog = []
    # OS.scan to go through looking for each log file
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "mdata", folder_name, "Logs")

    # Files must contain "Log" in name
    with os.scandir(path) as logs:
        for entry in logs:
            if entry.name.startswith('Log') and entry.is_file():
                df_inlog.append((pd.read_csv(os.path.join(path, entry.name))))

    return df_inlog


# Function combines the data, removing all the headers. Only use if it is all the same type of data

def combine_logs(folder_name):
    # Blank dictionary
    li = []
    # OS.scan to go through looking for each log file
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "mdata", folder_name, "Logs")

    # Files must contain "Log" in name
    with os.scandir(path) as logs:
        for entry in logs:
            if entry.name.startswith('Log') and entry.is_file():
                df = pd.read_csv((os.path.join(path, entry.name)), header=1)
                li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)
    return frame


# Prints to excel in the output folder. df is the dataframe,  fname is the file name you'd like

def pd_to_excel(df, fname):
    fname = fname + ".xlsx"
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "mdata", "output", fname)
    df.to_excel(path, index=False, header=True)
    return
