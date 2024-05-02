class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        L = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            while R - L + 1 - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
            result = max(result, R - L + 1)
        
        return result