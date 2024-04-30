class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        maxLength = 1
        charsMet = set()
        charsMet.add(s[0])
        L = 0

        for R in range(1, len(s)):
            print("s[R]:")
            print(s[R])
            while s[R] in charsMet and R > L:
                print("in while:")
                print(charsMet)
                charsMet.remove(s[L])
                L += 1
                print("L now:")
                print(s[L])
            charsMet.add(s[R])
            maxLength = max(maxLength, R - L + 1)
        
        return maxLength
