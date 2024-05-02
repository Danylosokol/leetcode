class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, 0
        s = list(s)
        for R in range(len(s)):
            if s[R].isalpha() or s[R].isdigit():
                s[L] = s[R].lower()
                L += 1
        s = s[:L]
        L, R = 0, len(s) - 1
        while L <= R:
            if s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1

        return True