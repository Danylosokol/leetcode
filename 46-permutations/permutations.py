class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i == len(nums):
                return [[]]
            
            result = []
            perm = backtrack(i + 1)

            for p in perm:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    result.append(pCopy)

            return result
        
        return backtrack(0)
                    