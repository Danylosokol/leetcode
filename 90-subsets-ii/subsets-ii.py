class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        currSubset = []

        self.backtrack(0, nums, subsets, currSubset)
        return subsets
    
    def backtrack(self, i, nums, subsets, currSubset):
        if i >= len(nums):
            subsets.append(currSubset.copy())
            return
        currSubset.append(nums[i])
        self.backtrack(i + 1, nums, subsets, currSubset)
        currSubset.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.backtrack(i + 1, nums, subsets, currSubset)