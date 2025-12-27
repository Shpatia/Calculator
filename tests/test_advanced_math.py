import unittest
import math
from advanced_math import sin_func, cos_func, power, sqrt_func, floor_func, ceil_func


class TestAdvancedMath(unittest.TestCase):

    # sin tests
    def test_sin_func_0(self):
        self.assertAlmostEqual(sin_func(0), 0.0, places=6)

    def test_sin_func_30(self):
        self.assertAlmostEqual(sin_func(30), 0.5, places=6)

    def test_sin_func_45(self):
        self.assertAlmostEqual(sin_func(45), round(math.sqrt(2)/2, 6), places=6)

    def test_sin_func_60(self):
        self.assertAlmostEqual(sin_func(60), round(math.sqrt(3)/2, 6), places=6)

    def test_sin_func_90(self):
        self.assertAlmostEqual(sin_func(90), 1.0, places=6)

    def test_sin_func_180(self):
        self.assertAlmostEqual(sin_func(180), 0.0, places=6)

    def test_sin_func_270(self):
        self.assertAlmostEqual(sin_func(270), -1.0, places=6)

    def test_sin_func_360(self):
        self.assertAlmostEqual(sin_func(360), 0.0, places=6)

    def test_sin_func_negative(self):
        self.assertAlmostEqual(sin_func(-90), -1.0, places=6)

    def test_sin_func_large_angle(self):
        # sin is periodic with 360°
        self.assertAlmostEqual(sin_func(450), sin_func(90), places=6)  # 450 % 360 = 90

    # cos tests
    def test_cos_func_0(self):
        self.assertAlmostEqual(cos_func(0), 1.0, places=6)

    def test_cos_func_60(self):
        self.assertAlmostEqual(cos_func(60), 0.5, places=6)

    def test_cos_func_90(self):
        self.assertAlmostEqual(cos_func(90), 0.0, places=6)

    def test_cos_func_180(self):
        self.assertAlmostEqual(cos_func(180), -1.0, places=6)

    def test_cos_func_270(self):
        self.assertAlmostEqual(cos_func(270), 0.0, places=6)

    def test_cos_func_360(self):
        self.assertAlmostEqual(cos_func(360), 1.0, places=6)

    def test_cos_func_negative(self):
        self.assertAlmostEqual(cos_func(-60), 0.5, places=6)

    def test_cos_func_large_angle(self):
        self.assertAlmostEqual(cos_func(720), cos_func(0), places=6)

    # power tests
    def test_power_positive_int(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exp(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_one_exp(self):
        self.assertEqual(power(7, 1), 7)

    def test_power_zero_base(self):
        self.assertEqual(power(0, 5), 0)

    def test_power_negative_exp_int(self):
        self.assertAlmostEqual(power(2, -2), 0.25, places=6)

    def test_power_negative_base_odd_exp(self):
        self.assertEqual(power(-2, 3), -8)

    def test_power_negative_base_even_exp(self):
        self.assertEqual(power(-2, 2), 4)

    def test_power_fractional_exp(self):
        # Note: your current `power(a, b)` uses `a ** b`, which supports floats
        self.assertAlmostEqual(power(4, 0.5), 2.0, places=6)
        self.assertAlmostEqual(power(8, 1/3), 2.0, places=6)

    def test_power_zero_zero(self):
        # Python defines 0**0 == 1
        self.assertEqual(power(0, 0), 1)

    # sqrt tests
    def test_sqrt_func_perfect_square(self):
        self.assertEqual(sqrt_func(9), 3.0)

    def test_sqrt_func_zero(self):
        self.assertEqual(sqrt_func(0), 0.0)

    def test_sqrt_func_one(self):
        self.assertEqual(sqrt_func(1), 1.0)

    def test_sqrt_func_non_perfect_square(self):
        self.assertAlmostEqual(sqrt_func(2), math.sqrt(2), places=6)

    def test_sqrt_func_large_number(self):
        self.assertAlmostEqual(sqrt_func(10000), 100.0, places=6)

    def test_sqrt_func_negative_raises(self):
        with self.assertRaises(ValueError):
            sqrt_func(-1)

    # floor tests
    def test_floor_func_positive(self):
        self.assertEqual(floor_func(3.7), 3)

    def test_floor_func_negative(self):
        self.assertEqual(floor_func(-3.2), -4)  # floor goes *down*

    def test_floor_func_integer(self):
        self.assertEqual(floor_func(5.0), 5)

    def test_floor_func_zero(self):
        self.assertEqual(floor_func(0.9), 0)

    def test_floor_func_negative_integer(self):
        self.assertEqual(floor_func(-5.0), -5)

    # ceil tests
    def test_ceil_func_positive(self):
        self.assertEqual(ceil_func(3.2), 4)

    def test_ceil_func_negative(self):
        self.assertEqual(ceil_func(-3.7), -3)  # ceil goes *up*

    def test_ceil_func_integer(self):
        self.assertEqual(ceil_func(7.0), 7)

    def test_ceil_func_zero(self):
        self.assertEqual(ceil_func(0.1), 1)

    def test_ceil_func_negative_integer(self):
        self.assertEqual(ceil_func(-4.0), -4)


if __name__ == '__main__':
    unittest.main()
