import pandas as pd
from config import INTAKE_README_PATH
from tools.view import get_readme
from pages.intake.view import show_columns_value


def show_main_content(df: pd.DataFrame, show_columns: list):
    """Show all widget for the main content."""
    get_readme(INTAKE_README_PATH)
    show_columns_value(df, show_columns)
    # st.dataframe(filtered_df)
