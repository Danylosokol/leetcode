class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []

        def dfs(idx, subset):
            if idx >= len(nums):
                result.append(subset[:])
                return
            
            subset.append(nums[idx])
            dfs(idx+1, subset)
            subset.pop()
            dfs(idx+1, subset)
        
        dfs(0, subset)
        return result