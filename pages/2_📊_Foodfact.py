import streamlit as st
from pages.foodfact.model import FoodFact, get_df


foodfact_instance = FoodFact(df=get_df())
foodfact_instance.filter_dataframe()
foodfact_instance.transform_column_to_numeric()
df = foodfact_instance.df
float_columns, str_columns = foodfact_instance.get_float_string_columns()

fer_cln = "Fer (mg/100 g)"
name = "alim_nom_fr"

options = st.multiselect(
    "What are your favorite column", df.columns.values.tolist(), [name, fer_cln]
)

# Select columns with dtype float

column_to_search = st.selectbox(
    "column to search", list(set(str_columns).intersection(options))
)

# Columns to transform

float_options = list(set(float_columns).intersection(options))
column_to_sort = st.selectbox("column to sort", float_options)

if st.checkbox("sort from a value"):
    df = df.sort_values(by=column_to_sort, ascending=False)


search_str = st.text_input(f"Search in column {column_to_search}")
df = df[df[column_to_search].str.contains(search_str, case=False, na=False)]
st.dataframe(df[options])

to_include = "a inclure"
# Add a boolean column with all values set to False
df[to_include] = False

weight = "poids en g"
# Add an integer column with all values set to 0
df["poids en g"] = 0


def calculate_with_weight(row, col, weight):
    if row[weight] >= 0:
        return row[col] * row[weight]
    else:
        return 0


option_and_editable = options + [to_include, weight]
edited_df = st.data_editor(df[option_and_editable])
for col in float_options:
    edited_df[col] = edited_df.apply(
        lambda row: calculate_with_weight(row, col, weight), axis=1
    )

# Filter rows where 'to_include' is True
edited_filtered_df = edited_df[edited_df[to_include]]
st.dataframe(edited_filtered_df)
