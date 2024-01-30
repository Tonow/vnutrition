import numpy as np
import pandas as pd
from os import path
import streamlit as st

@st.cache_data
def get_df(type_case: str, file_path: tuple) -> pd.DataFrame:

    nutri_file = f"apport_{type_case}.csv"
    path_nutri_file = path.join(*file_path, nutri_file)
    df = pd.read_csv(path_nutri_file, header=[0, 1])

    df = df.reset_index()

    return df

@st.cache_data
def filter_multi_index_dataframe(df:pd.DataFrame, choice:str, column_name:str="Age") -> pd.DataFrame:
    # Apply the boolean condition to filter the DataFrame
    condition = df[column_name].iloc[:, 0] == choice
    filtered_df = df[condition]
    return filtered_df.set_index(column_name)


def get_needs_type(df: pd.DataFrame, need_code: str) -> pd.DataFrame:
    return df.xs(need_code, axis=1, level=1, drop_level=True)

def set_to_numeric(df: pd.DataFrame) -> pd.DataFrame:

    df = df.replace("ND", np.nan)

    for column in df.columns:
        if df[column].dtype == 'object':  # Check if the column is of object type
            df[column] = pd.to_numeric(df[column].str.replace(',', '.'))
    return df
