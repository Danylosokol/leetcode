class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitToChars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(i, combination):
            if len(combination) == len(digits):
                result.append(combination)
                return
            
            for char in digitToChars[digits[i]]:
                backtrack(i + 1, combination + char)
        
        if len(digits):
            backtrack(0, "")
        
        return result