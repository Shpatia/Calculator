class Memory:
    def init(self):
        self.value = 0

    def memory_add(self, num):
        self.value += num

    def memory_clear(self):
        self.value = 0

    def memory_recall(self):
        return self.value