import streamlit as st
import pandas as pd
from pages.foodfact.model import FoodFact, get_df
from pages.foodfact.config import NAME, FER_CLN, ALIM_SSGRP_NOM_FR
from tools.view import (
    filters_rows_on_columns_multiselect,
    sort_one_column,
    filters_columns_multiselect,
    search_str,
)


def foodfact_get_data() -> pd.DataFrame:
    """Retrieve the dataframe pre_formatted

    Returns:
        pd.DataFrame: Dataframe for this model.
    """
    foodfact_instance = FoodFact(df=get_df())
    foodfact_instance.filter_dataframe()
    foodfact_instance.transform_column_to_numeric()
    df = foodfact_instance.df
    return df


def show_main_content():
    """Show all widget for the main content."""
    df = foodfact_get_data()
    df, columns = filters_columns_multiselect(
        df=df, default_cols=[FER_CLN], hide_default_cols=[NAME, ALIM_SSGRP_NOM_FR]
    )
    df = filters_rows_on_columns_multiselect(df, ALIM_SSGRP_NOM_FR, "Groupe d'aliment")
    df = sort_one_column(df=df)
    df = search_str(df=df, column_to_search=NAME, label="Chercher un nom:")

    st.dataframe(df, hide_index=True)


# to_include = "a inclure"
# # Add a boolean column with all values set to False
# df[to_include] = False

# weight = "poids en g"
# # Add an integer column with all values set to 0
# df["poids en g"] = 0


# option_and_editable = columns + [to_include, weight]
# edited_df = st.data_editor(df[option_and_editable])
# for col in float_options:
#     edited_df[col] = edited_df.apply(
#         lambda row: foodfact_instance.calculate_with_weight(row, col, weight), axis=1
#     )

# # Filter rows where 'to_include' is True
# edited_filtered_df = edited_df[edited_df[to_include]]
# st.dataframe(edited_filtered_df)
