from stf_decomposition import stf_decomposition

import numpy as np
import unittest
import pandas as pd

DATA_SOURCE = "tests/data/data.txt"

class TestConstructor(unittest.TestCase):
    # stf_decomposition expects a data frame with an index
    # This will test if a correct error is thrown when a matrix is input instead of a data frame 
    def test_data_input(self):
        matrix = np.ones((10, 2))
        stf_decomposition(matrix, "blackman")
        