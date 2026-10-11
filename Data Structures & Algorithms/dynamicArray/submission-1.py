class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.filled = 0
        self.list = [None] * capacity

    def get(self, i: int) -> int:
        return self.list[i]

    def set(self, i: int, n: int) -> None:
        self.list[i] = n

    def pushback(self, n: int) -> None:
        for element in range(len(self.list)):
            if self.list[element] is None:
                self.list[element] = n
                self.filled += 1
                return  
        if self.filled == self.capacity:
            self.resize()
        self.list[self.filled] = n
        self.filled += 1

    def popback(self) -> int:
        for element in range(len(self.list)):
            if self.list[element] is None:
                popped = self.list[element - 1]
                self.list[element - 1] = None
                self.filled -= 1 
                return popped
        popped = self.list[-1]
        self.list[-1] = None
        self.filled -= 1
        return popped
 
    def resize(self) -> None:
        new_list = [None] * (self.capacity * 2)
        for i in range(len(self.list)):
            new_list[i] = self.list[i]
        self.list = new_list
        self.capacity = len(new_list)

    def getSize(self) -> int:
        return self.filled 
        
    def getCapacity(self) -> int:
        return self.capacity
