class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}

        for i in range(len(nums)):
            if nums[i] not in remainder:
                remainder[target - nums[i]] = i
            else:
                return [remainder[nums[i]], i]
        
        return [0, 0]