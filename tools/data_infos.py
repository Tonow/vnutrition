import pandas as pd
from typing import Tuple


def get_float_string_columns(df: pd.DataFrame) -> Tuple[list, list]:
    """Get lists of columns type.

    Args:
        df (pd.DataFrame): dataframe to check.

    Returns:
        Tuple[list, list]: list of different type.
    """
    float_columns = []
    float_columns.extend(df.select_dtypes(include="float64").columns)
    float_columns.extend(df.select_dtypes(include="float32").columns)
    str_columns = df.select_dtypes(include="object").columns
    return float_columns, str_columns
