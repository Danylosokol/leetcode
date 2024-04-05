class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainers = {}

        for i in range(len(nums)):
            if nums[i] not in remainers:
                remainers[target - nums[i]] = i
            else:
                return[remainers[nums[i]], i]
        
        return [0, 0]