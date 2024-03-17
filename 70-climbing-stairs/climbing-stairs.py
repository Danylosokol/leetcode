class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1
        for _ in range(n - 1):
            temp = n1
            n1 = n2 + n1
            n2 = temp
        return n1
        