from abc import ABC, abstractmethod

class Accumulator(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def accumulate(self, value):
        pass

    def __add__(self, other):
        return self.accumulate(other)

    def __sub__(self, other):
        return self.accumulate(-other)

class MyAccumulator(Accumulator):
    def __init__(self):
        self._sum = 0

    def accumulate(self, value):
      self._sum += value
      return self
    
    def add(self, x):
        self._sum += x
        return self
    
    def subtract(self, x):
        self._sum -= x
        return self
    
    def multiply(self, x):
        self._sum *= x
        return self
    
    def divide(self, x):
        self._sum /= x
        return self
    
    def clear(self):
        self._sum = 0
        return self
    
    def get_value(self):
        return self._sum

my_acc = MyAccumulator()
my_acc.add(5).add(10).add(15)
print(my_acc.get_value())  # Output: 30