class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = []

    def get(self, i: int) -> int:
        if i >= len(self.values):
            return -1
        return self.values[i]

    def set(self, i: int, n: int) -> None:
        if i >= len(self.values):
            return -1
        self.values[i] = n

    def pushback(self, n: int) -> None:
        if len(self.values) >= self.capacity:
            self.resize()
        self.values.append(n)

    def popback(self) -> int:
        if self.values:
            return self.values.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.values)
    
    def getCapacity(self) -> int:
        return self.capacity