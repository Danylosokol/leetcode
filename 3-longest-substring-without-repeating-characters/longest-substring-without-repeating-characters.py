class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedChars = set()
        result = 0
        L = 0

        for R in range(len(s)):
            while s[R] in visitedChars:
                visitedChars.remove(s[L])
                L += 1
            visitedChars.add(s[R])
            result = max(result, R - L + 1)
        
        return result