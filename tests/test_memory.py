import unittest
from memory import Memory


class TestMemory(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()

    def test_initial_value_is_zero(self):
        self.assertEqual(self.mem.memory_recall(), 0)

    def test_add_updates_value_correctly(self):
        self.mem.memory_add(15)
        self.assertEqual(self.mem.memory_recall(), 15)

    def test_multiple_additions_accumulate(self):
        self.mem.memory_add(3)
        self.mem.memory_add(7)
        self.mem.memory_add(-2)
        self.assertEqual(self.mem.memory_recall(), 8)

    def test_clear_resets_to_zero_after_additions(self):
        self.mem.memory_add(20)
        self.mem.memory_clear()
        self.assertEqual(self.mem.memory_recall(), 0)

    def test_clear_has_no_effect_when_already_zero(self):
        self.mem.memory_clear()
        self.assertEqual(self.mem.memory_recall(), 0)

    def test_recall_returns_current_value_without_modifying_it(self):
        self.mem.memory_add(12)
        first_recall = self.mem.memory_recall()
        second_recall = self.mem.memory_recall()
        self.assertEqual(first_recall, 12)
        self.assertEqual(second_recall, 12)

    def test_add_with_zero_leaves_value_unchanged(self):
        self.mem.memory_add(5)
        self.mem.memory_add(0)
        self.assertEqual(self.mem.memory_recall(), 5)

    def test_negative_addition_works_as_expected(self):
        self.mem.memory_add(10)
        self.mem.memory_add(-4)
        self.assertEqual(self.mem.memory_recall(), 6)

if __name__ == '__main__':
    unittest.main()
