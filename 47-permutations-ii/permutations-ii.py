class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perms = []
        counts = {n: 0 for n in nums}
        for n in nums:
            counts[n] += 1
        
        def backtrack():
            if len(perms) == len(nums):
                result.append(perms[:])
            
            for n in counts:
                if counts[n] > 0:
                    perms.append(n)
                    counts[n] -= 1
                    backtrack()
                    perms.pop()
                    counts[n] += 1
            
        backtrack()
        return result