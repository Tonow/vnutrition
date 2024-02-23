import pandas as pd
from config import INTAKE_README_PATH
from tools.view import get_readme, filters_rows_on_columns_multiselect
from pages.intake.view import show_columns_value
from pages.foodfact.main_content import foodfact_get_data
from pages.foodfact.config import NAME, ALIM_SSGRP_NOM_FR


def show_main_content(df: pd.DataFrame, show_columns: list):
    """Show all widget for the main content."""
    default_cols = [NAME, ALIM_SSGRP_NOM_FR]
    get_readme(INTAKE_README_PATH)
    foodfact_df = foodfact_get_data()
    foodfact_df = filters_rows_on_columns_multiselect(
        foodfact_df, ALIM_SSGRP_NOM_FR, "Groupe d'aliment"
    )
    show_columns_value(df, show_columns, default_cols, foodfact_df)
    # foodfact_df, columns = filters_columns_with_near_string(
    #     df=foodfact_df,
    #     search_strings_cols=show_columns,
    #     default_cols=default_cols,
    #     strings_to_drop=STRINGS_TO_DROP
    # )
    # columns_choice = set(columns) - set(default_cols)
    # for column in columns_choice:
    #     foodfact_df_sorted = foodfact_df.sort_values(by=column, ascending=False)
    #     st.subheader(column, divider='rainbow')
    #     st.dataframe(foodfact_df_sorted, hide_index=True)
