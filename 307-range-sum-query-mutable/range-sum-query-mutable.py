class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    @staticmethod
    def define(nums, L, R):
        if L == R:  
            return SegmentTree(nums[L], L, R)
        root = SegmentTree(0, L, R)
        mid = (L + R)//2
        root.left = SegmentTree.define(nums, L, mid)
        root.right = SegmentTree.define(nums, mid + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return
        mid = (self.L + self.R) // 2
        if index <= mid:
            self.left.update(index, val)
        else:
            self.right.update(index, val)
        self.sum = self.left.sum + self.right.sum
    
    def range(self, left, right):
        if self.L == left and self.R == right:
            return self.sum
        mid = (self.L + self.R) // 2
        if left > mid:
            return self.right.range(left, right)
        elif right <= mid:
            return self.left.range(left, right)
        else:
            return self.left.range(left, mid) + self.right.range(mid + 1, right)


class NumArray:

    def __init__(self, nums: List[int]):
        self.segTree = SegmentTree.define(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.segTree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segTree.range(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)