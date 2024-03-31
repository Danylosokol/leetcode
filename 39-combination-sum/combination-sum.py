class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            
            if idx >= len(candidates) or total > target:
                return
            
            curr.append(candidates[idx])
            dfs(idx, curr, total + candidates[idx])
            curr.pop()
            dfs(idx+1, curr, total)
        
        dfs(0, [], 0)
        return result