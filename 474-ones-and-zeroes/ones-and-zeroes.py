class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(index, m, n):
            if index >= len(strs):
                return 0
            
            if (index, m, n) in dp:
                return dp[(index, m, n)]
            
            dp[(index, m, n)] = dfs(index + 1, m, n)

            mCount, nCount = strs[index].count("0"), strs[index].count("1")

            if (m >= mCount) and (n >= nCount):
                dp[(index, m, n)] = max(dp[(index, m, n)], 1 + dfs(index + 1, m - mCount, n - nCount))
            
            return dp[(index, m, n)]
        
        return dfs(0, m, n)