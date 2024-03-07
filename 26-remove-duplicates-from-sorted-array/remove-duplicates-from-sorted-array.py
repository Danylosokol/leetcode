class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        for i in range(len(nums)):
            j = i
            while i < len(nums) - 1 and nums[i] == nums[i + 1] and j < len(nums):
                j += 1
                duplicate = nums.pop(i + 1)
                nums.append(duplicate)
            unique += 1
            if i < len(nums) - 1 and nums[i] >= nums[i + 1]:
                break
        return unique
            
        