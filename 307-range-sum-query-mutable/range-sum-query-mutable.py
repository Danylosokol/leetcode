class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    @staticmethod
    def build(nums, L, R):
        if L == R:
                return SegmentTree(nums[L], L, R)
            
        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return 
        
        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.sum = self.left.sum + self.right.sum

    def sumRange(self, left, right):
        if self.L == left and self.R == right:
            return self.sum
        
        M = (self.L + self.R) // 2
        if left > M:
            return self.right.sumRange(left, right)
        elif right <= M:
            return self.left.sumRange(left, right)
        else:
            return self.left.sumRange(left, M) + self.right.sumRange(M + 1, right)

class NumArray:

    def __init__(self, nums: List[int]):
        self.segmentTree = SegmentTree.build(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.segmentTree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segmentTree.sumRange(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)