class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        maxLength = 1
        charsMet = set()
        charsMet.add(s[0])
        L = 0

        for R in range(1, len(s)):
            while s[R] in charsMet and R > L:
                charsMet.remove(s[L])
                L += 1
            charsMet.add(s[R])
            maxLength = max(maxLength, R - L + 1)
        
        return maxLength
