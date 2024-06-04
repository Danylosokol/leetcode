class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        currSubset = []
        self.helper(0, nums, currSubset, subsets)
        return subsets

    def helper(self, i, nums, currSubset, subsets):
        if i >= len(nums):
            subsets.append(currSubset.copy())
            return
        currSubset.append(nums[i])
        self.helper(i + 1, nums, currSubset, subsets)
        currSubset.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, currSubset, subsets)