import pandas as pd
import numpy as np
import streamlit as st


def filter_dataframe_columns_with_stings(
    df: pd.DataFrame, column_name: str, filter_strings: list
) -> pd.DataFrame:
    """In one columns filter dataframe on list of string

    Args:
        df (pd.DataFrame): Initial dataframe
        column_name (str): the columns to apply the filter.
        filter_strings (list): list of string for the filtering.

    Returns:
        pd.DataFrame: filtered dataframe
    """
    # Create a boolean mask for each string in the filter_strings list
    if filter_strings:
        # Create a boolean mask for each string in the filter_strings list
        pattern = "|".join([f"^{s}$" for s in filter_strings])
        mask = df[column_name].str.contains(pattern, case=False, regex=True, na=False)

        # Apply the mask to the DataFrame
        filtered_df = df[mask]
        return filtered_df
    else:
        return df


@st.cache_data
def filter_multi_index_dataframe(
    df: pd.DataFrame, choice: str, column_name: str = "Age"
) -> pd.DataFrame:
    """In dataframe with the choice on a column get only row from this choice.

    Args:
        df (pd.DataFrame): the dataframe
        choice (str): the item value choose on the column
        column_name (str, optional): the column for the filter. Defaults to "Age".

    Returns:
        pd.DataFrame: one filtered dataframe with one row.
    """
    # Apply the boolean condition to filter the DataFrame
    condition = df[column_name].iloc[:, 0] == choice
    filtered_df = df[condition]
    return filtered_df.set_index(column_name)


def get_needs_type(df: pd.DataFrame, need_code: str) -> pd.DataFrame:
    """Filter the dataframe only on the second level of multi-index.

    Args:
        df (pd.DataFrame): The dataframe to filter.
        need_code (str): The code of the second index.

    Returns:
        pd.DataFrame: New dataframe only with the second level index.
    """
    return df.xs(need_code, axis=1, level=1, drop_level=True)


def set_object_to_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """Change all object columns to numeric.

    Args:
        df (pd.DataFrame): The dataframe to change.

    Returns:
        pd.DataFrame: New dataframe without object columns but numeric.S
    """
    df = df.replace("ND", np.nan)

    for column in df.columns:
        if df[column].dtype == "object":  # Check if the column is of object type
            df[column] = pd.to_numeric(df[column].str.replace(",", "."))
    return df
