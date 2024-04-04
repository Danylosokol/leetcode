class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for val in nums:
            if val not in hashset:
                hashset.add(val)
            else:
                return True
        
        return False