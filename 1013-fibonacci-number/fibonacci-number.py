class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n <= 0:
            return 0
        result = self.fib(n - 1) + self.fib(n - 2)
        return result
        