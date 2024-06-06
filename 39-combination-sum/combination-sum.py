class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(i, currSum, combination):
            if currSum > target:
                return
            if currSum == target:
                result.append(combination.copy())
                return
            if i >= len(candidates):
                return
            combination.append(candidates[i])
            backtracking(i, currSum + candidates[i], combination)
            combination.pop()
            backtracking(i + 1, currSum, combination)
        
        backtracking(0, 0, [])
        return result