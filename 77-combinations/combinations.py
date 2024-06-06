class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(1, n, result, k, [])
        return result

    def backtrack(self, i, n, result, k, combination):
        if len(combination) == k:
            result.append(combination.copy())
            return 

        if i > n:
            return
        
        for j in range(i, n + 1):
            combination.append(j)
            self.backtrack(j + 1, n, result, k, combination)
            combination.pop()