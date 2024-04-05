class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prev_nums = set()

        for val in nums:
            if val not in prev_nums:
                prev_nums.add(val)
            else:
                return True
        
        return False