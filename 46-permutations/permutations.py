class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(0, nums)

    def backtrack(self, i, nums):
        if i == len(nums):
            return [[]]
        
        result = []
        perms = self.backtrack(i + 1, nums)
        for p in perms:
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                result.append(pCopy)
        return result