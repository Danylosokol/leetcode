class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        options = []

        for i in digits:
            option = []
            for j in range(3):
                if int(i) > 7:
                    option.append(chr(97 + ((int(i) - 2) * 3) + j + 1))
                else:
                    option.append(chr(97 + ((int(i) - 2) * 3) + j))
            if int(i) == 7:
                option.append(chr(97 + ((int(i) - 2) * 3) + 3))
            elif int(i) == 9:
                option.append(chr(97 + ((int(i) - 2) * 3) + 3 + 1))
            options.append(option)
        print(options)
        def backtrack(i, max, combination):
            if i == max:
                if not len(combination):
                    return
                result.append("".join(combination.copy()))
                return
            
            for j in range(len(options[i])):
                combination.append(options[i][j])
                backtrack(i + 1, max, combination)
                combination.pop()
        
        backtrack(0, len(options), [])
        return result