import streamlit as st
import numpy as np
import pandas as pd
from os import path


def get_df(type_case):

    nutri_file = f"apport_{type_case}.csv"
    path_nutri_file = path.join("data","apport", nutri_file)
    df = pd.read_csv(path_nutri_file, header=[0, 1])

    df = df.reset_index()

    return df

def filter_multi_index_dataframe(df, choice, column_name="Age"):
    # Apply the boolean condition to filter the DataFrame
    condition = df[column_name].iloc[:, 0] == choice
    filtered_df = df[condition]
    return filtered_df.set_index(column_name)


def get_needs_type(df, need_code: str):
    return df.xs(need_code, axis=1, level=1, drop_level=True)

def set_to_numeric(df):

    df = df.replace("ND", np.nan)

    for column in df.columns:
        if df[column].dtype == 'object':  # Check if the column is of object type
            df[column] = pd.to_numeric(df[column].str.replace(',', '.'))
    return df
