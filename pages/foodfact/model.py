import pandas as pd
from config import (
    ALIM_SSGRP_CODE_TO_DROP,
    ALIM_GRP_CODE_TO_DROP,
    ALIM_SSSSGRP_CODE_TO_DROP,
    CIQUAL_FILE,
)

from dataclasses import dataclass


def get_df(filepath: str = CIQUAL_FILE) -> pd.DataFrame:
    df = pd.read_excel(filepath)
    return df


@dataclass
class FoodFact:
    """Class FoodFact."""

    df: pd.DataFrame
    alim_ssgrp_code_to_drop = ALIM_SSGRP_CODE_TO_DROP
    alim_grp_code_to_drop = ALIM_GRP_CODE_TO_DROP
    alim_ssssgrp_code_to_drop = ALIM_SSSSGRP_CODE_TO_DROP

    def filter_dataframe(self):
        # Use the isin method to drop rows
        self.df = self.df[~self.df["alim_grp_code"].isin(ALIM_GRP_CODE_TO_DROP)]
        self.df = self.df[~self.df["alim_ssgrp_code"].isin(ALIM_SSGRP_CODE_TO_DROP)]
        self.df = self.df[~self.df["alim_ssssgrp_code"].isin(ALIM_SSSSGRP_CODE_TO_DROP)]

    def transform_column_to_numeric(self):
        columns_to_transform = [col for col in self.df.columns if "/100 g)" in col]
        self.df[columns_to_transform] = self.df[columns_to_transform].apply(
            lambda x: pd.to_numeric(x.str.replace(",", "."), errors="coerce")
        )

    def get_float_string_columns(self):
        float_columns = self.df.select_dtypes(include="float64").columns
        str_columns = self.df.select_dtypes(include="object").columns
        return float_columns, str_columns
