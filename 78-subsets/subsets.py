class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        curr = []

        def dfs(idx, curr):
            if idx >= len(nums):
                result.append(curr[:])
                return
            
            curr.append(nums[idx])
            idx += 1
            dfs(idx, curr)
            curr.pop()
            dfs(idx, curr)
        
        dfs(0, curr)
        return result