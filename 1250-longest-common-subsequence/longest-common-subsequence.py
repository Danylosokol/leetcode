class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        prev_row = [0] * (cols + 1)

        for i in range(rows):
            cur_row = [0] * (cols + 1)
            for j in range(cols):
                if text1[i] == text2[j]:
                    cur_row[j + 1] = 1 + prev_row[j]
                else:
                    cur_row[j + 1] = max(cur_row[j], prev_row[j + 1])
            prev_row = cur_row

        return prev_row[cols]  
