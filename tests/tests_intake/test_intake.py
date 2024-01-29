import unittest
import pandas as pd
import numpy as np

from intake.intake import set_to_numeric

class TestSetToNumeric(unittest.TestCase):

    def setUp(self):
        # Set up some sample data for testing
        data = {
            'Column1': ['10', '20', 'ND'],
            'Column2': ['30', '40', '50.5'],
            'Column3': [1, 2, 3]
        }
        self.df = pd.DataFrame(data)

    def test_set_to_numeric(self):
        # Test the function with a DataFrame containing numeric and non-numeric values
        result = set_to_numeric(self.df)

        # Assert that the 'Column1' and 'Column2' are now numeric, and 'Column3' remains unchanged
        expected_result = pd.DataFrame({
            'Column1': [10.0, 20.0, np.nan],
            'Column2': [30.0, 40.0, 50.5],
            'Column3': [1, 2, 3]
        })
        pd.testing.assert_frame_equal(result, expected_result)

    def test_set_to_numeric_with_commas(self):
        # Test the function with a DataFrame containing commas as decimal separators
        data = {
            'Column1': ['10000,0', '20000,0', '30000,5'],
            'Column2': ['40000.75', '50000.0', 'ND'],
            'Column3': [1, 2, 3]
        }
        df_with_commas = pd.DataFrame(data)
        result = set_to_numeric(df_with_commas)

        # Assert that the 'Column1' and 'Column2' are now numeric, and 'Column3' remains unchanged
        expected_result = pd.DataFrame({
            'Column1': [10000.0, 20000.0, 30000.5],
            'Column2': [40000.75, 50000.0, np.nan],
            'Column3': [1, 2, 3]
        })
        pd.testing.assert_frame_equal(result, expected_result)

    def test_set_to_numeric_no_changes(self):
        # Test the function with a DataFrame already containing only numeric values
        data = {
            'Column1': [10, 20, 30],
            'Column2': [40.5, 50.75, 60.0],
            'Column3': [1, 2, 3]
        }
        df_numeric_only = pd.DataFrame(data)
        result = set_to_numeric(df_numeric_only)

        # Assert that the DataFrame remains unchanged
        pd.testing.assert_frame_equal(result, df_numeric_only)
