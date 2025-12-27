import unittest
from basic_ops import add, subtract, multiply, divide, mod


class TestBasicOps(unittest.TestCase):

    # add
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_signs(self):
        self.assertEqual(add(-5, 7), 2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(-3, 0), -3)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.1), 5.6, places=6)

    # subtract
    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-2, -3), 1)  # -2 - (-3) = 1

    def test_subtract_mixed(self):
        self.assertEqual(subtract(3, -2), 5)
        self.assertEqual(subtract(-3, 2), -5)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3, places=6)

    # multiply
    def test_multiply_positive(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-4, 3), -12)
        self.assertEqual(multiply(-4, -3), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(-7, 0), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply(7, 1), 7)
        self.assertEqual(multiply(-3, 1), -3)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4), 10.0, places=6)
        self.assertAlmostEqual(multiply(-1.5, 2), -3.0, places=6)

    # divide
    def test_divide_positive(self):
        self.assertEqual(divide(6, 2), 3.0)

    def test_divide_negative(self):
        self.assertEqual(divide(-6, 2), -3.0)
        self.assertEqual(divide(6, -2), -3.0)
        self.assertEqual(divide(-6, -2), 3.0)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(5, 2), 2.5, places=6)
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=6)

    def test_divide_by_one(self):
        self.assertEqual(divide(7, 1), 7.0)

    def test_divide_by_negative_one(self):
        self.assertEqual(divide(8, -1), -8.0)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0.0)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError, msg="Деление на ноль!"):
            divide(5, 0)
        with self.assertRaises(ValueError):
            divide(0, 0)

    # mod
    def test_mod_positive(self):
        self.assertEqual(mod(10, 3), 1)

    def test_mod_negative_dividend(self):
        # Python: результат mod имеет знак ДЕЛИТЕЛЯ
        self.assertEqual(mod(-10, 3), 2)    # потому что -10 = (-4)*3 + 2
        self.assertEqual(mod(10, -3), -2)   # 10 = (-4)*(-3) + (-2)
        self.assertEqual(mod(-10, -3), -1)  # -10 = (3)*(-3) + (-1)

    def test_mod_zero_dividend(self):
        self.assertEqual(mod(0, 5), 0)

    def test_mod_by_one(self):
        self.assertEqual(mod(7, 1), 0)

    def test_mod_by_negative_one(self):
        self.assertEqual(mod(7, -1), 0)
        self.assertEqual(mod(-7, -1), 0)

    def test_mod_floats(self):
        self.assertAlmostEqual(mod(7.5, 2), 1.5, places=6)
        self.assertAlmostEqual(mod(-7.5, 2), 0.5, places=6)

    def test_mod_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            mod(10, 0)


if __name__ == '__main__':
    unittest.main()
