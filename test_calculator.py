import unittest
import math
from basic_ops import add, subtract, multiply, divide, mod
from advanced_math import sin_func, cos_func, power, sqrt_func, floor_func, ceil_func
from memory import Memory


class TestBasicOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(-5, 4),-1)
        self.assertEqual(add(4.5,9),13.5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 7), -7)
        self.assertEqual(subtract(7, 0), 7)
        self.assertEqual(subtract(0, 0), 0)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2, places=6)
        self.assertEqual(subtract(500000, 1000000), -500000)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(-2.5, 2), -5.0)
        self.assertEqual(multiply(-1000, 1000), -1000000)
        self.assertEqual(multiply(-5, -1), 5)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(-10, -2), 5)
        self.assertEqual(divide(5, -1), -5)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_mod(self):
        self.assertEqual(mod(10, 3), 1)
        self.assertEqual(mod(7, 3), 1)
        self.assertEqual(mod(10, -3), -2)
        self.assertEqual(mod(1000000, 999), 1000000 % 999)
        self.assertEqual(mod(5, 10), 5)


class TestAdvancedMath(unittest.TestCase):
    def test_sin_func(self):
        self.assertAlmostEqual(sin_func(0), 0.0, places=6)
        self.assertAlmostEqual(sin_func(30), 0.5, places=6)
        self.assertAlmostEqual(sin_func(90), 1.0, places=6)
        self.assertAlmostEqual(sin_func(180), 0.0, places=6)
        self.assertAlmostEqual(sin_func(270), -1.0, places=6)

    def test_cos_func(self):
        self.assertAlmostEqual(cos_func(0), 1.0, places=6)
        self.assertAlmostEqual(cos_func(60), 0.5, places=6)
        self.assertAlmostEqual(cos_func(90), 0.0, places=6)
        self.assertAlmostEqual(cos_func(180), -1.0, places=6)
        self.assertAlmostEqual(cos_func(270), 0.0, places=6)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(-2, 3), -8)
        self.assertAlmostEqual(power(4, 0.5), 2.0, places=6)

    def test_sqrt_func(self):
        self.assertEqual(sqrt_func(9), 3)
        self.assertAlmostEqual(sqrt_func(2), math.sqrt(2), places=6)
        with self.assertRaises(ValueError):
            sqrt_func(-4)

    def test_floor_func(self):
        self.assertEqual(floor_func(3.7), 3)
        self.assertEqual(floor_func(-1.2), -2)
        self.assertEqual(floor_func(0.0), 0)

    def test_ceil_func(self):
        self.assertEqual(ceil_func(3.1), 4)
        self.assertEqual(ceil_func(-1.8), -1)
        self.assertEqual(ceil_func(0.0), 0)


class TestMemory(unittest.TestCase):
    def test_memory_add_and_recall(self):
        mem = Memory()
        mem.memory_add(5)
        mem.memory_add(2.5)
        self.assertAlmostEqual(mem.memory_recall(), 7.5, places=6)

    def test_memory_clear(self):
        mem = Memory()
        mem.memory_add(10)
        mem.memory_clear()
        self.assertEqual(mem.memory_recall(), 0)

    def test_memory_negative_values(self):
        mem = Memory()
        mem.memory_add(-5)
        mem.memory_add(2)
        self.assertEqual(mem.memory_recall(), -3)

    def test_memory_sequence(self):
        mem = Memory()
        mem.memory_add(3)
        mem.memory_add(7)
        self.assertEqual(mem.memory_recall(), 10)
        mem.memory_clear()
        mem.memory_add(1.1)
        mem.memory_add(2.2)
        self.assertAlmostEqual(mem.memory_recall(), 3.3, places=6)


if __name__ == '__main__':
    unittest.main()
