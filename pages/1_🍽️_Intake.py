import streamlit as st
from config import TYPE_CASE, APPORT_QTY, INTAKE_README_PATH
from pages.intake.model import (
    get_df,
    filter_multi_index_dataframe,
    get_needs_type,
    set_object_to_numeric,
)
from pages.intake.view import show_columns_value
from tools.view import get_readme

get_readme(INTAKE_README_PATH)
type_case = st.selectbox("cas", TYPE_CASE)
df = get_df(type_case, ("data", "apport"))
age_choice = st.selectbox("age", df["Age"])
filtered_rows = filter_multi_index_dataframe(df, choice=age_choice, column_name="Age")

need_code_key = st.selectbox("besoin", APPORT_QTY.keys())

try:
    filtered_df = get_needs_type(filtered_rows, APPORT_QTY[need_code_key])
    filtered_df = set_object_to_numeric(filtered_df)
    show_columns_value(filtered_df)
    st.dataframe(filtered_df)
except KeyError:
    st.error(f"Aucune clé {need_code_key}")
