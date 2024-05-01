class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        result = 0
        L = 0

        for R in range(len(s)):
            counts[s[R]] = 1 + counts.get(s[R], 0)
            while R - L + 1 - max(counts.values()) > k:
                counts[s[L]] -= 1
                L += 1
            result = max(result, R - L + 1)

        return result