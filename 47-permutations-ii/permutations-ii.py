class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.backtrack(0, nums)

    def backtrack(self, i, nums):
        if i == len(nums):
            return [[]]
        
        result = []
        # while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        #     i = i + 1
        perm = self.backtrack(i + 1, nums)

        for p in perm:
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                if pCopy not in result:
                    result.append(pCopy)
        
        return result