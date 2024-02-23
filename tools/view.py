from os import path
import streamlit as st
import pandas as pd
from typing import Tuple

from tools.format_data import filter_dataframe_columns_with_stings
from tools.data_infos import get_float_string_columns


@st.cache_data
def get_readme(readme_path: list):
    """From a path read README.md file and use st.markdown.

    Args:
        path (list): Path of the readme file.
    """
    with open(
        path.join(*readme_path, "README.md"), "r", encoding="utf-8"
    ) as readme_file:
        readme_content = readme_file.read()

    st.markdown(readme_content)


def filters_rows_on_columns_multiselect(
    df: pd.DataFrame, column_name: str, label: str
) -> pd.DataFrame:
    """With the multiselect widget filter on dataframe the matching rows.

    Args:
        df (pd.DataFrame): Initial dataframe.
        column_name (str): Column to apply the filter.
        label (str): Label of the widget.

    Returns:
        pd.DataFrame: Dataframe filtered with right rows.
    """
    column_items_to_filter = st.multiselect(label, set(df[column_name].values.tolist()))
    if column_items_to_filter:
        df = filter_dataframe_columns_with_stings(
            df, column_name, column_items_to_filter
        )
    return df


def filters_columns_multiselect(
    df: pd.DataFrame,
    label: str = "Columns to keep",
    default_cols: list = None,
    hide_default_cols: list = None,
) -> Tuple[pd.DataFrame, list]:
    """With the multiselect widget filter on dataframe the matching columns.

    Args:
        df (pd.DataFrame): Initial dataframe.
        label (str): Label of the widget. Defaults to ""Columns to keep".
        default_cols (list, optional): Default columns for the widget. Defaults to None.
        hide_default_cols (list, optional): Columns show in dataframe but not on widget. Defaults to None.

    Returns:
        Tuple[pd.DataFrame, list]: (Dataframe filtered with right columns,
            List of columns choose.
    """
    columns_choice = set(df.columns.values.tolist()) - set(hide_default_cols)
    columns = st.multiselect(label, columns_choice, default_cols)
    if hide_default_cols:
        hide_default_cols += columns
        columns = list(set(hide_default_cols))
    return df[columns], columns


def search_str(
    df: pd.DataFrame,
    column_to_search: str = None,
    label: str = None,
    case: bool = False,
) -> pd.DataFrame:
    """Search string in one columns and return matching rows.

    Args:
        df (pd.DataFrame): Initial dataframe.
        column_to_search (str, optional): Columns to do the filter. Defaults to None.
        label (str, optional): Label of the widget. Defaults to None.
        case (bool, optional): If True, case sensitive. Defaults to False.

    Returns:
        pd.DataFrame: Dataframe filtered with right rows.
    """
    _, str_columns = get_float_string_columns(df)

    if not column_to_search:
        column_to_search = st.selectbox("Column to search", list(set(str_columns)))
    if not label:
        label = f"Search in column {column_to_search}"
    search_str = st.text_input(label)
    df = df[df[column_to_search].str.contains(search_str, case=case, na=False)]
    return df


def sort_one_column(
    df: pd.DataFrame,
    label_checkbox: str = "Sort from a value",
    label_selectbox: str = "Column to sort",
    ascending: bool = False,
) -> pd.DataFrame:
    """To sort the dataframe on one columns

    Args:
        df (pd.DataFrame): Initial dataframe.
        label_checkbox (str, optional): Checkbox widget label. Defaults to "Sort from a value".
        label_selectbox (str, optional): Selectbox widget label. Defaults to "Column to sort".
        ascending (bool, optional): Sort ascending vs. descending.
          Specify list for multiple sort orders.
          If this is a list of bools, must match the length of the by.
          Defaults to False.

    Returns:
        pd.DataFrame: Dataframe sorted.
    """
    float_columns, _ = get_float_string_columns(df)
    float_options = list(set(float_columns))

    if st.checkbox(label_checkbox):
        column_to_sort = st.selectbox(label_selectbox, float_options)
        df = df.sort_values(by=column_to_sort, ascending=ascending)
    return df
