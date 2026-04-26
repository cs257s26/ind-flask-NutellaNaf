import unittest
import sys
import os
from ProductionCode.command_line import *

class TestData(unittest.TestCase):
    def test_load_valid_file(self):
        """Tests whether data from a valid CSV file is loaded successfully."""
        load_data()
        self.assertGreater(len(data), 0)

# Tests for Nafees' user story
    def test_non_numeric_data_column(self):
        """Tests whether a non-numerical data column is correctly rejected."""
        with self.assertRaises(ValueError, msg="Input a non-numerical column."):
            nafees_user_story("Model name")
    
    def test_numeric_data_column(self):
        """Tests whether a numerical data column correctly lists top 5 values of a column."""
        expected_list = [(2820.0, 4), (2160.0, 2), (1928.0, 6), (1709.0, 18), (1361.0, 5)]
        column = "training_hours"
        self.assertEqual(expected_list, nafees_user_story(column))

    def test_non_column(self):
        """Tests whether a column not in the dataset is correctly rejected."""
        with self.assertRaises(ValueError, msg="Input a valid column within the csv."):
            nafees_user_story("nafees")

# Tests for helper func
    def test_non_numeric_data_column_n(self):
        """Tests whether a non-numerical data column is correctly rejected."""
        with self.assertRaises(ValueError, msg="Input a non-numerical column."):
            top_n_column_values("Model name", 5)
    
    def test_numeric_data_column_n(self):
        """Tests whether a numerical data column correctly lists top 5 values of a column."""
        expected_list = [(2820.0, 4), (2160.0, 2), (1928.0, 6), (1709.0, 18), (1361.0, 5)]
        column = "training_hours"
        self.assertEqual(expected_list, top_n_column_values(column, 5))

    def test_non_column_n(self):
        """Tests whether a column not in the dataset is correctly rejected."""
        with self.assertRaises(ValueError, msg="Input a valid column within the csv."):
            top_n_column_values("nafees", 5)



if __name__ == '__main__':
    unittest.main()
