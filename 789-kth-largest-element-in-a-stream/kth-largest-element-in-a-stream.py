class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k
        for val in nums:
            self.add(val)
        print("finish adding")


    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1:
            parent_idx = i // 2
            if self.heap[parent_idx] > self.heap[i]:
                self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
                i = parent_idx
            else:
                break
        while len(self.heap) > self.k + 1:
            self.pop(self.heap)
        # print("heap after adding:")
        # print(val)
        # print(self.heap)
        return self.heap[1]
    
    def pop(self, heap):
        if len(heap) <= 1:
            return None
        
        if len(heap) == 2:
            return heap.pop()
        
        res = heap[1]
        heap[1] = heap[-1]
        heap.pop()
        idx = 1
        while 2*idx < len(heap):
            if 2*idx < len(heap) - 1 and heap[2*idx + 1] < heap[2*idx] and heap[2*idx + 1] <  heap[idx]:
                heap[idx], heap[2*idx + 1] = heap[2*idx + 1], heap[idx]
                idx = 2*idx + 1
            elif heap[2*idx] < heap[idx]:
                heap[idx], heap[2*idx] = heap[2*idx], heap[idx]
                idx = 2*idx
            else:
                break
        
        return res

            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)