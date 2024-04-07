class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reminders = {}

        for indx, val in enumerate(nums):
            if val not in reminders:
                reminders[target - val] = indx
            else:
                return [reminders[val], indx]