import unittest

from decimal import Decimal


def frange(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    #     if step == 0:
    #         raise ValueError('0 cant be used as step')

    start = Decimal(str(start))
    stop = Decimal(str(stop))
    step = Decimal(str(step))
    result = start

    while (step > 0 and result < stop) or (step < 0 and result > stop):
        yield result
        result += step


class TestFrange(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_frange_single_param(self):
        # assert (list(frange(5)) == [0, 1, 2, 3, 4])
        self.assertEqual(list(frange(5)), [0, 1, 2, 3, 4, 5])

    def test_frange_2_params(self):
        self.assertEqual(list(frange(2, 5)), [0, 1, 2, 3, 4, 5])

    def test_frange_2_params_empty_result(self):
        self.assertEqual(list(frange(5, 2)), [])

    def test_frange_custom_step(self):
        self.assertEqual(list(frange(2, 10, 2)), [2, 4, 6, 8])

    def test_frange_reverse_order(self):
        self.assertEqual(list(frange(10, 2, -2)), [10, 8, 6, 4])


if __name__ == '__main__':
    unittest.main()
