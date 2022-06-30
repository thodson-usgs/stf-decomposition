from ast import parse
import numpy as np
import unittest
import pandas as pd
import sys

sys.path.append('src')

from stf_decomposition.stf_decomposition import stf_decomposition

class TestFit(unittest.TestCase):
    # This will test if an array of constant values are input as the signal data that the trend decomposition will have a slope of zero 
    def test_simple_input(self):
        data = pd.Series(np.repeat(1, 100))
        stf = stf_decomposition(data, "blackman", period = 7, seasonal = 3)
        res = stf.fit()
        trend_slope = np.polyfit(res.trend.index, res.trend, 1)[0]
        self.assertEqual(trend_slope, 0)



