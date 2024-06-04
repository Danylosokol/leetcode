class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currSubset = []
        self.helper(0, nums, subsets, currSubset)
        return subsets
    
    def helper(self, i, nums, subsets, currSubset):
        if i >= len(nums):
            subsets.append(currSubset.copy())
            return
        currSubset.append(nums[i])
        self.helper(i+1, nums, subsets, currSubset)
        currSubset.pop()
        self.helper(i+1, nums, subsets, currSubset)