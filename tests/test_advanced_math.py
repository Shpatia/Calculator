import unittest
from advanced_math import sin_func, cos_func, power, sqrt_func, floor_func, ceil_func

class TestAdvancedMath(unittest.TestCase):
    def test_sin_func(self):
        self.assertAlmostEqual(sin_func(90), 1.0, places=6)

    def test_cos_func(self):
        self.assertAlmostEqual(cos_func(0), 1.0, places=6)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_sqrt_func(self):
        self.assertEqual(sqrt_func(9), 3)

    def test_floor_func(self):
        self.assertEqual(floor_func(3.7), 3)

    def test_ceil_func(self):
        self.assertEqual(ceil_func(3.2), 4)

if __name__ == '__main__':
    unittest.main()
