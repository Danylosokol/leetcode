class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L <= R:
            while L < R and not self.isAlphaNumeric(s[L]):
                L += 1
            while R > L and not self.isAlphaNumeric(s[R]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True
    
    def isAlphaNumeric(self, c):
        return(
            ord(c) >= ord('0') and ord(c) <= ord('9') or
            ord(c) >= ord('a') and ord(c) <= ord('z') or
            ord(c) >= ord('A') and ord(c) <= ord('Z')
        )