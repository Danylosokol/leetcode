class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, cur_amount):
            if cur_amount == amount:
                return 1
            
            if cur_amount > amount or i >= len(coins):
                return 0
            
            if (i, cur_amount) in dp:
                return dp[(i, cur_amount)]
            
            dp[(i, cur_amount)] = dfs(i, cur_amount + coins[i]) + dfs(i + 1, cur_amount)
            return dp[(i, cur_amount)]
        
        return dfs(0, 0)