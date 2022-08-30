from collate_log import read_data, combine_folder, combine_logs, pd_to_excel


# by Tyler Fulghum, monarch curve testing section.
# Reads text file into pandas dataframe

def main():
    df = combine_folder("7_28_1300_1500")
    df = combine_logs("7_28_1300_1500")
    print(df)
    #fname = "test1"
    #pd_to_excel(df, fname)


if __name__ == "__main__":
    main()
