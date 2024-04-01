class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, subarray, sum):
            if sum == target:
                result.append(subarray[:])
                return

            if idx >= len(candidates) or sum > target:
                return

            subarray.append(candidates[idx])
            dfs(idx, subarray, sum + candidates[idx])
            subarray.pop()
            dfs(idx + 1, subarray, sum)
        
        dfs(0, [], 0)
        return result