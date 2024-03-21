class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity > 0:
            raise ValueError("Wrong capacity")
        self._capacity = capacity

