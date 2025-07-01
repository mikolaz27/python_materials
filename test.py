import unittest


class TestFrange(unittest.TestCase):

    def test_frange_single_param(self):
        # self.assertEqual(list(frange(5)) , [0, 1, 2, 3, 4])
        self.assertEqual(list(frange(5)), [0, 1, 2, 3, 4, 5])
    
    def test_frange_2_params(self):
        self.assertEqual(list(frange(2, 5)), [2, 3, 4])
        
    def test_frange_2_params_empty_result(self):
        self.assertEqual(list(frange(5, 2)), [])

    def test_frange_custom_step(self):
        self.assertEqual(list(frange(2, 10, 2)), [2, 4, 6, 8])

    def test_frange_reverse_order(self):
        self.assertEqual(list(frange(10, 2, -2)), [10, 8, 6, 4])

unittest.main(argv=[''], verbosity=2, exit=False)