import streamlit as st
import pandas as pd
from tools.format_data import filters_columns_with_near_string
from pages.foodfact.config import STRINGS_TO_DROP


def show_columns_foodfact_value(
    foodfact_df: pd.DataFrame, show_column: list, default_cols: list
):
    foodfact_df, columns = filters_columns_with_near_string(
        df=foodfact_df,
        search_strings_col=show_column,
        default_cols=default_cols,
        strings_to_drop=STRINGS_TO_DROP,
    )
    columns_choice = set(columns) - set(default_cols)
    foodfact_df_sorted = foodfact_df.sort_values(
        by=list - -(columns_choice), ascending=False
    )
    st.dataframe(foodfact_df_sorted[columns], hide_index=True)


def show_columns_value(
    df: pd.DataFrame, show_columns: list, default_cols: list, foodfact_df: pd.DataFrame
):
    """Show widget values for the columns list.

    Work only for columns with only one value.

    Args:
        df (pd.DataFrame): Dataframe with values to show.
        show_columns (list): List of columns to show.
    """
    if not df.empty:
        for column_name in show_columns:
            if df[column_name].any():
                try:
                    value = float(df[column_name])
                    st.subheader(column_name, divider="rainbow")
                    st.metric(label=column_name, value=value, delta=None)
                    show_columns_foodfact_value(
                        foodfact_df, show_column=column_name, default_cols=default_cols
                    )
                except ValueError as ve:
                    st.error(f"Pour {column_name} : {ve}")
            else:
                st.error(f"Aucune Valeur pour {column_name}")
