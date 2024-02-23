import pandas as pd
import numpy as np
import streamlit as st
from typing import Tuple


def filter_dataframe_columns_exact_stings(
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


def clean_string(original_string, strings_to_drop):
    for string_to_drop in strings_to_drop:
        original_string = original_string.replace(string_to_drop, " ")
    original_string = original_string.replace("\n", " ")
    return original_string


# Function to check if all words in any of the search strings are present in the column name
def check_all_words(column_name, search_strings, strings_to_drop):
    res = None
    search_strings = clean_string(search_strings.lower(), strings_to_drop)
    column_name_clean = clean_string(column_name.lower(), strings_to_drop)
    is_right_column = all(
        element in column_name_clean.split() for element in search_strings.split()
    )
    if is_right_column:
        return column_name
    return res


def filters_columns_with_near_string(
    df: pd.DataFrame,
    search_strings_col: str = None,
    default_cols: list = None,
    strings_to_drop: list = [],
) -> Tuple[pd.DataFrame, list]:
    """With the multiselect widget filter on dataframe the matching columns.

    Args:
        df (pd.DataFrame): Initial dataframe.
        default_cols (list, optional): Default columns for the widget. Defaults to None.

    Returns:
        Tuple[pd.DataFrame, list]: (Dataframe filtered with right columns,
            List of columns choose.
    """
    # Filter columns based on the condition
    filtered_columns = []
    for column in df.columns:
        column_checked = check_all_words(column, search_strings_col, strings_to_drop)
        if column_checked:
            filtered_columns.append(column_checked)
    if default_cols:
        filtered_columns += default_cols
        columns = list(set(filtered_columns))
    else:
        columns = filtered_columns

    return df[columns], columns


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
