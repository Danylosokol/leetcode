class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reminders = {}

        for i, val in enumerate(nums):
            if val not in reminders:
                reminders[target - val] = i
            else:
                return [reminders[val], i]