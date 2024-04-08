class MyHashSet:

    def __init__(self):
        self.set = [None, None]
        self.capacity = 2
        self.size = 0
        
    def hash(self, key):
        return key%self.capacity
    
    def rehash(self):
        self.capacity = 2*self.capacity
        oldSet = self.set[:]
        newSet = []
        for indx in range(self.capacity):
            newSet.append(None)
        self.set = newSet
        self.size = 0
        for val in oldSet:
            if val:
                self.add(val)

    def add(self, key: int) -> None:
        index = self.hash(key)
        while True:
            if self.set[index] == None:
                self.set[index] = key
                self.size += 1
                if self.size > self.capacity//2:
                    self.rehash()
                return
            elif self.set[index] == key:
                return

            index += 1
            index = index%self.capacity

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        index = self.hash(key)
        while True:
            if self.set[index] == key:
                self.set[index] = None
                self.size -= 1
                return
            index += 1
            index = index%self.capacity

    def contains(self, key: int) -> bool:
        initialIndex = self.hash(key)
        if self.set[initialIndex] == key:
                return True
        index = initialIndex + 1
        index = index%self.capacity
        while index != initialIndex:
            if self.set[index] == key:
                return True
            index += 1
            index = index%self.capacity
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)