import pandas as pd
from os import path
import streamlit as st


@st.cache_data
def get_df(type_case: str, file_path: tuple) -> pd.DataFrame:
    """Retrieve the intake dataframe from csv file.

    Args:
        type_case (str): type of person.
        file_path (tuple): path of csv file.

    Returns:
        pd.DataFrame: the dataframe index reset.
    """
    nutri_file = f"apport_{type_case}.csv"
    path_nutri_file = path.join(*file_path, nutri_file)
    df = pd.read_csv(path_nutri_file, header=[0, 1])

    df = df.reset_index()

    return df
