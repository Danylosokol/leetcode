class Node:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class NumArray:

    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, L, R):
        if L == R:
            return Node(nums[L], L, R)
        root = Node(0, L, R)
        mid = (L + R) // 2
        root.left = self.build(nums, L, mid)
        root.right = self.build(nums, mid + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        self.root = self.update_helper(self.root, index, val)
    
    def update_helper(self, root, index, val):
        if root.L == root.R:
            root.sum = val
            return root
        mid = (root.L + root.R) // 2
        if index > mid:
            root.right = self.update_helper(root.right, index, val)
        else:
            root.left = self.update_helper(root.left, index, val)
        root.sum = root.right.sum + root.left.sum
        return root

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_helper(self.root, left, right)
    
    def sum_helper(self, root, left, right):
        if root.L == left and root.R == right:
            return root.sum
        mid = (root.L + root.R)//2
        if left > mid:
            return self.sum_helper(root.right, left, right)
        elif right <= mid:
            return self.sum_helper(root.left, left, right)
        else:
            return self.sum_helper(root.left, left, mid) + self.sum_helper(root.right, mid + 1, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)