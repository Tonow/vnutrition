import unittest
import pandas as pd

from tools.format_data import filter_dataframe_columns_with_stings


class TestFilterDataFrame(unittest.TestCase):
    def setUp(self):
        # Sample DataFrame for testing
        data = {
            "alim_ssgrp_nom_fr": [
                "Fruits",
                "Légumes et fruits",
                "Condiments",
                "Viandes",
                "Condiments et épices",
            ]
        }
        self.column_name = "alim_ssgrp_nom_fr"
        self.df = pd.DataFrame(data)

    def test_filter_single_string(self):
        filter_strings = ["légumes"]
        result = filter_dataframe_columns_with_stings(
            self.df, self.column_name, filter_strings
        )
        self.assertTrue(result.empty)

    def test_filter_multiple_strings(self):
        filter_strings = ["légumes", "condiment"]
        result = filter_dataframe_columns_with_stings(
            self.df, self.column_name, filter_strings
        )
        self.assertTrue(result.empty)

    def test_filter_total_single_string(self):
        filter_strings = ["Légumes et fruits"]
        result = filter_dataframe_columns_with_stings(
            self.df, self.column_name, filter_strings
        )
        expected = pd.DataFrame({"alim_ssgrp_nom_fr": ["Légumes et fruits"]})
        result.index = result.index.factorize()[0]
        pd.testing.assert_frame_equal(result, expected)

    def test_filter__total_multiple_strings(self):
        filter_strings = ["Légumes et fruits", "condiments"]
        result = filter_dataframe_columns_with_stings(
            self.df, self.column_name, filter_strings
        )
        expected = pd.DataFrame(
            {"alim_ssgrp_nom_fr": ["Légumes et fruits", "Condiments"]}
        )
        result.index = result.index.factorize()[0]
        pd.testing.assert_frame_equal(result, expected)

    def test_wrong_filter_strings(self):
        filter_strings = ["no present"]
        result = filter_dataframe_columns_with_stings(
            self.df, self.column_name, filter_strings
        )
        self.assertTrue(result.empty)

    def test_empty_filter_strings(self):
        filter_strings = []
        result = filter_dataframe_columns_with_stings(
            self.df, self.column_name, filter_strings
        )
        pd.testing.assert_frame_equal(result, self.df)
