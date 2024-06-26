# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        result = n

        while l <= r:
            m = (l + r)//2

            if isBadVersion(m):
                result = m
                r = m - 1
            else:
                l = m + 1
        
        return result