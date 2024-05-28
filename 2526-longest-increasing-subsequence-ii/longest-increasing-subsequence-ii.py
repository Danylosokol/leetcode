class Node:
    def __init__(self, val, L, R):
        self.val = val
        self.left = None
        self.right = None
        self.L = L
        self.R = R
    
class SegmentTree:
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, L, R):
        if L == R:
            return Node(0, L, R)
        root = Node(0, L, R)
        M = (L + R) // 2
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        return root
    
    def update(self, index, val):
        self.update_helper(self.root, index, val)
    
    def update_helper(self, root, index, val):
        if root.L == root.R:
            root.val = val
            return
        M = (root.L + root.R) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.val = max(root.left.val, root.right.val)
    
    def query(self, L, R):
        return self.query_helper(self.root, L, R)
    
    def query_helper(self, root, L, R):
        if root.L >= L and root.R <= R:
            return root.val
        M = (root.L + root.R) // 2
        max_value = 0
        if L <= M:
            max_value = self.query_helper(root.left, L, R)
        if R > M:
            max_value = max(max_value, self.query_helper(root.right, L, R))
        return max_value

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        tree = SegmentTree([i for i in range(max(nums) + 1)])
        max_length = 1
        for value in nums:
            length = tree.query(value - k, value - 1) + 1
            print(length)
            max_length = max(max_length, length)
            tree.update(value, length)
        return max_length