import streamlit as st
import pandas as pd
from tools.format_data import filters_columns_with_near_string
from pages.foodfact.config import STRINGS_TO_DROP, NEEDS_COL, PART_SIZE
import plotly.graph_objects as go


def show_edited_df(foodfact_df_sorted, foodfact_df_show_column, columns, needs_value):
    edited_df = st.data_editor(
        foodfact_df_sorted[columns],
        disabled=(list(set(foodfact_df_sorted.columns.to_list()) - set(PART_SIZE))[0]),
        hide_index=True,
        column_config={
            foodfact_df_show_column: st.column_config.ProgressColumn(
                foodfact_df_show_column,
                format="%.2f/100g",
                min_value=0,
                max_value=100,
            ),
        },
    )
    edited_df = edited_df[edited_df[PART_SIZE] > 0]
    edited_df["Apport %"] = 100 * (edited_df[PART_SIZE] / edited_df[NEEDS_COL])
    st.dataframe(edited_df, hide_index=True)
    fig = go.Figure(
        data=[
            go.Bar(name=NEEDS_COL, x=[NEEDS_COL, "Apport %"], y=[needs_value, 0]),
        ]
    )
    for _, row in edited_df.iterrows():
        fig.add_trace(
            go.Bar(
                name=row["alim_nom_fr"],
                x=[NEEDS_COL, "Apport %"],
                y=[0, (row["Apport %"] / 100) * needs_value],
            )
        )
    # Change the bar mode
    fig.update_layout(barmode="stack")
    st.plotly_chart(fig, use_container_width=True)


def show_columns_foodfact_value(
    foodfact_df: pd.DataFrame, show_column: str, default_cols: list, needs_value: float
):
    foodfact_df, columns = filters_columns_with_near_string(
        df=foodfact_df,
        search_strings_col=show_column,
        default_cols=default_cols,
        strings_to_drop=STRINGS_TO_DROP,
    )
    columns_choice = set(columns) - set(default_cols)
    foodfact_df_sorted = foodfact_df.sort_values(
        by=list(columns_choice), ascending=False
    )
    foodfact_df_show_column = list(
        set(foodfact_df_sorted.columns.to_list()) - set(default_cols)
    )[0]
    quantity_to_intake = 100 * (
        needs_value / foodfact_df_sorted[foodfact_df_show_column]
    )
    foodfact_df_sorted[NEEDS_COL] = quantity_to_intake
    foodfact_df_sorted[PART_SIZE] = 0
    columns.insert(0, NEEDS_COL)
    columns.insert(0, PART_SIZE)
    show_edited_df(foodfact_df_sorted, foodfact_df_show_column, columns, needs_value)


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
                    needs_value = float(df[column_name])
                    st.subheader(column_name, divider="rainbow")
                    st.metric(label=column_name, value=needs_value, delta=None)
                    show_columns_foodfact_value(
                        foodfact_df,
                        show_column=column_name,
                        default_cols=default_cols,
                        needs_value=needs_value,
                    )
                except ValueError as ve:
                    st.error(f"Pour {column_name} : {ve}")
            else:
                st.error(f"Aucune Valeur pour {column_name}")
