import pandas as pd


def filter_dataframe_columns_with_stings(
    df: pd.DataFrame, column_name: str, filter_strings: list
) -> pd.DataFrame:
    """In one columns filter dataframe on list of string

    Args:
        df (pd.DataFrame): Initial dataframe
        column_name (str): the columns to apply the filter.
        filter_strings (list): list of string for the filtering.

    Returns:
        pd.DataFrame: filtered dataframe
    """
    # Create a boolean mask for each string in the filter_strings list
    if filter_strings:
        # Create a boolean mask for each string in the filter_strings list
        pattern = "|".join([f"^{s}$" for s in filter_strings])
        mask = df[column_name].str.contains(pattern, case=False, regex=True, na=False)

        # Apply the mask to the DataFrame
        filtered_df = df[mask]
        return filtered_df
    else:
        return df
