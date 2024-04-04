class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for val in nums:
            if val not in counts:
                counts[val] = 1
            else:
                return True
        
        return False