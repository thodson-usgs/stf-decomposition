from ast import parse
import numpy as np
import unittest
import pandas as pd
import sys

sys.path.append('src')

from stf_decomposition import STF

class TestConstructor(unittest.TestCase):
    # STF expects a data frame with an index
    # This will test if a correct error is thrown when a matrix is input instead of a data frame 
    def test_incorrect_data_input(self):
        matrix = np.ones((10, 2))
        with self.assertRaises(ValueError):
            STF(matrix, "blackman")
    # This will test if no error is thrown when data with a period is input to STF() without a formal period argument 
    def test_inferring_period_input(self):
        data = pd.read_csv("tests/data/co2.csv", index_col='date', parse_dates=True)
        try:
            STF(data, "blackman")
        except ValueError:
            self.fail("STF() did not correctly infer period from data")
    # This will test if an error is thrown when data with no period is input to STF() without a formal period arumnet 
    def test_no_period_input(self):
        data = pd.read_csv("tests/data/co2.csv", index_col = 'date')
        with self.assertRaises(ValueError):
            STF(data, "blackman")
    # This will test that an error is thrown if an invalid window is input
    def test_invalid_window(self):
        data = pd.read_csv("tests/data/co2.csv", index_col = 'date', parse_dates=True)
        with self.assertRaises(ValueError):
            STF(data, "normal", seasonal = 13)
    # This will test that all compatible windows with scipy.signal.get_window work as expected
    def test_valid_windows(self):
        data = pd.read_csv("tests/data/co2.csv", index_col = 'date', parse_dates=True)
        windows = ['boxcar', 'triang', 'blackman', 'hamming', 'hann', 'bartlett', 
        'flattop', 'parzen', 'bohman', 'blackmanharris', 'nuttall', 'barthann', 
        'cosine', 'exponential', 'tukey', 'taylor']
        for window in windows:
            try:
                STF(data, window, seasonal = 13)
            except(ValueError):
                self.fail(f"Window {window} did not work as expected")


        
