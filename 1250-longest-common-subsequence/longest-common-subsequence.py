class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        prev_row = [0] * (cols + 1)

        for r in range(rows):
            cur_row = [0] * (cols + 1)
            for c in range(cols):
                if text1[r] == text2[c]:
                    cur_row[c + 1] = 1 + prev_row[c]
                else:
                    cur_row[c + 1] = max(cur_row[c], prev_row[c + 1])
            prev_row = cur_row
        
        return cur_row[cols]