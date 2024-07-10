class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lcs(s, s[::-1])
    
    def lcs(self, s1, s2):
        N, M = len(s1), len(s2)
        dp = [0] * (M + 1)

        for i in range(N):
            new_row = [0] * (M + 1)
            for j in range(M):
                if s1[i] == s2[j]:
                    new_row[j + 1] = 1 + dp[j]
                else:
                    new_row[j + 1] = max(new_row[j], dp[j + 1])
            dp = new_row
        
        return dp[M]