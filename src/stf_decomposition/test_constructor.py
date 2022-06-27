from stf_decomposition import stf_decomposition

import numpy as np
import unittest

DATA_SOURCE = "tests/data/data.txt"

class TestConstructor(unittest.TestCase):
    # stf_decomposition expects 
    def test_data_input(self):
        