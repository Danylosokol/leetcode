class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1

        prev_row = [0] * cols

        for r in range(rows - 2, -1, -1):
            curr_row = [0] * cols
            for c in range(cols - 2, -1, -1):
                if text1[r] == text2[c]:
                    curr_row[c] = 1 + prev_row[c + 1]
                else:
                    curr_row[c] = max(curr_row[c + 1], prev_row[c])
        
            prev_row = curr_row
        
        return prev_row[0]