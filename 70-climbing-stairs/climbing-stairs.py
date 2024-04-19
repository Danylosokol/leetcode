class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        firstStair = 1
        secondStair = 2
        n -= 2
        while n > 0:
            temp = firstStair
            firstStair = secondStair
            secondStair = temp + firstStair
            n -= 1
        return secondStair