import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums

        pivot = random.choice(nums)
        less_than, equal_to, more_than = [], [], []

        for val in nums:
            if val < pivot: less_than.append(val)
            elif val > pivot: more_than.append(val)
            else: equal_to.append(val)
            
        return self.sortArray(less_than) + equal_to + self.sortArray(more_than)