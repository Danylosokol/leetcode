class Solution:
    def countSubstrings(self, s: str) -> int:
        # strings = set()
        counter = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # strings.add(s[l:r + 1])
                counter += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # strings.add(s[l:r + 1])
                counter += 1
                l -= 1
                r += 1
        
        return counter