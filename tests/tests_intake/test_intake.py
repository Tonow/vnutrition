import unittest

from pages.intake.model import get_df


class TestGetDF(unittest.TestCase):
    def setUp(self):
        self.type_case = "test"
        self.file_path = ("tests", "data", "apport")

    def test_get_df(self):
        # Test the function with a specific type_case
        result = get_df(self.type_case, self.file_path)

        # Assert that the result is a DataFrame with the expected structure
        expected_columns = [
            ("index", ""),
            ("Age", "Unnamed: 0_level_1"),
            ("Fer\nmg/jour", "BME"),
            ("Fer\nmg/jour", "ANR/AS"),
            ("Fer\nmg/jour", "AMT"),
            ("Magnésium\nmg/jour", "BME"),
            ("Magnésium\nmg/jour", "ANR/AS"),
            ("Magnésium\nmg/jour", "AMT"),
        ]
        self.assertEqual(result.columns.tolist(), expected_columns)
        self.assertEqual(result.shape, (4, 8))

    def test_get_df_file_not_found(self):
        # Test the function with a type_case that does not have a corresponding file
        type_case = "nonexistent"
        with self.assertRaises(FileNotFoundError):
            get_df(type_case, self.file_path)
