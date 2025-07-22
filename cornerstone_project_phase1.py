# Assistant
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
%matplotlib inline
import seaborn as sns
import os


def read_csv_file(filename):
    return pd.read_csv(filename)

def find_Null(df):
    if df.isnull().any().any():  # Fixed indentation here
        return df.isnull().sum()
    else:
        return 0  # This line had incorrect indentation

def find_Duplicates(df):
    # Same fix applied here
    if df.duplicated().any().any():
        return df.duplicated().sum()
    else:
        return 0

def fill_missing_mean(df):
    return df.fillna(df.mean(),inplace=True)

def  drop_duplicates(df):
    return df.drop_duplicates(inplace=True)

def main():
    df_crashes_fatalities_table = read_csv_file("/Users/srimahimavangala/Desktop/Education/AI/Project/Airplane_Crashes_and_Fatalities_Since_1908-2.csv")
    df_airline_traffic_passengers_table = read_csv_file("/Users/srimahimavangala/Desktop/Education/AI/Project/Air_Traffic_Passenger_Statistics.csv")
 if (find_Null(df_crashes_fatalities_table)>0):
     df_crashes_fatalities_with_mean = fill_missing_mean(df_crashes_fatalities_table)
 if (find_Null(df_airline_traffic_passengers_table)>0):
     df_airline_traffic_passengers_with_mean = fill_missing_mean(df_airline_traffic_passengers_table)
df_crashes_fatalities_with_mean.info()
df_airline_traffic_passengers_with_mean.info()
      

if __name__ == "__main__":
    main()
