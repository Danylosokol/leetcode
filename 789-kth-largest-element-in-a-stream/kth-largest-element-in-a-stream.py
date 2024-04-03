class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k

        for val in nums:
            self.add(val)

    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1:
            parent_i = i//2
            if self.heap[parent_i] > self.heap[i]:
                self.heap[parent_i], self.heap[i] = self.heap[i], self.heap[parent_i]
                i = parent_i
            else:
                break
        
        while len(self.heap) > self.k + 1:
            self.pop()
        
        return self.heap[1]
    
    def pop(self):
        res = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        i = 1
        while 2*i < len(self.heap):
            if 2*i + 1 < len(self.heap) and self.heap[2*i + 1] < self.heap[2*i] and self.heap[2*i + 1] < self.heap[i]:
                self.heap[2*i + 1], self.heap[i] = self.heap[i], self.heap[2*i + 1]
                i = 2*i + 1
            elif self.heap[2*i] < self.heap[i]:
                self.heap[2*i], self.heap[i] = self.heap[i], self.heap[2*i]
                i = 2*i
            else:
                break

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)