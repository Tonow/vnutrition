import streamlit as st
import pandas as pd


def show_columns_value(df: pd.DataFrame, show_columns: list):
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
                    st.metric(label=column_name, value=value, delta=None)
                except ValueError as ve:
                    st.error(f"Pour {column_name} : {ve}")
            else:
                st.error(f"Aucune Valeur pour {column_name}")
