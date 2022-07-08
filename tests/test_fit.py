from ast import parse
from unicodedata import decomposition
import numpy as np
import unittest
import pandas as pd
import sys
from pandas import testing as tm

sys.path.append('src')

from stf_decomposition.stf_decomposition import stf_decomposition

class TestFit(unittest.TestCase):
    # This will test if an array of constant values are input as the signal data that the trend decomposition will have a slope of zero 
    def test_simple_input(self):
        data = pd.Series(np.repeat(1, 100))
        stf = stf_decomposition(data, "blackman", period = 7, seasonal = 3)
        res = stf.fit()
        trend_slope = np.polyfit(res.trend.index, res.trend, 1)[0]
        self.assertAlmostEqual(trend_slope, 0)
    # This will test if two independent runs of the same argument inputs will yield equal results
    def test_multiple_calls(self):
        data = pd.read_csv("tests/data/co2.csv", index_col='date', parse_dates=True)
        stf_1 = stf_decomposition(data, "blackman", seasonal = 13)
        res_1 = stf_1.fit()
        stf_2 = stf_decomposition(data, "blackman", seasonal = 13)
        res_2 = stf_2.fit()
        tm.assert_series_equal(res_1.trend, res_2.trend) and tm.assert_series_equal(res_1.seasonal, res_2.seasonal) and tm.assert_series_equal(res_1.resid, res_2.resid)
    # This will test if the sum of the decomposed components is equal to the observed data
    def test_decompositions_equal_observed(self):
        data = pd.read_csv("tests/data/co2.csv", index_col = 'date', parse_dates=True)
        stf = stf_decomposition(data, "blackman", seasonal = 13)
        res = stf.fit()
        decompositions_sum = res.trend + res.seasonal + res.resid
        tm.assert_series_equal(decompositions_sum, stf.observed, check_names = False)



