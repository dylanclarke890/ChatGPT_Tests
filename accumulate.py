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

    def __str__(self):
        return str(self.value)
    
class MyAccumulator(Accumulator):
    def accumulate(self, value):
        self.value += value
        return self

a = MyAccumulator(0)
b = MyAccumulator(10)

# Chained method calls
a.accumulate(5).accumulate(3).accumulate(2)
b.accumulate(1).accumulate(2).accumulate(3)

print(a)  # Output: 10
print(b)  # Output: 16