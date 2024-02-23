import pandas as pd
import streamlit as st
from typing import Tuple
from config import TYPE_CASE, APPORT_QTY
from pages.intake.model import get_df
from tools.format_data import (
    filter_multi_index_dataframe,
    get_needs_type,
    set_object_to_numeric,
)


def show_sidebar() -> Tuple[pd.DataFrame, list]:
    """Show all widget for side bar.

    Returns:
        Tuple[pd.DataFrame, list]: Dataframe filtered and the columns to use.
    """
    with st.sidebar:
        type_case = st.selectbox("Cas", TYPE_CASE)
        df = get_df(type_case, ("data", "apport"))
        age_choice = st.selectbox("Age", df["Age"])
        filtered_rows = filter_multi_index_dataframe(
            df, choice=age_choice, column_name="Age"
        )

        need_code_key = st.selectbox("Besoin", APPORT_QTY.keys())

        try:
            filtered_df = get_needs_type(filtered_rows, APPORT_QTY[need_code_key])
            filtered_df = set_object_to_numeric(filtered_df)
        except KeyError:
            st.error(f"Aucune clé {need_code_key}")
            filtered_df = pd.DataFrame()
        show_columns = st.multiselect("Apport", filtered_df.columns)
        return filtered_df, show_columns
