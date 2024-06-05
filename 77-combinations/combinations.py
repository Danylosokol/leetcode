class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(1, [], result, n, k)
        return result
    
    def backtrack(self, i, combination, result, n, k):
        if len(combination) == k:
            result.append(combination.copy())
            return
        
        if i > n:
            return
        
        for j in range(i, n + 1):
            combination.append(j)
            self.backtrack(j + 1, combination, result, n, k)
            combination.pop()