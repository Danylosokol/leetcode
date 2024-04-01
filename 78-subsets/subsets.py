class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        def dfs(idx, curr):
            if idx >= len(nums):
                result.append(curr[:])
                return
            
            curr.append(nums[idx])
            dfs(idx + 1, curr)
            curr.pop()
            dfs(idx + 1, curr)
        
        dfs(0, [])
        return result