import unittest
from memory import Memory

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()
        self.mem.__init__()

    def test_memory_add(self):
        self.mem.memory_add(10)
        self.assertEqual(self.mem.memory_recall(), 10)

    def test_memory_clear(self):
        self.mem.memory_add(5)
        self.mem.memory_clear()
        self.assertEqual(self.mem.memory_recall(), 0)

    def test_memory_recall(self):
        self.mem.memory_add(7)
        self.assertEqual(self.mem.memory_recall(), 7)

if __name__ == '__main__':
    unittest.main()
