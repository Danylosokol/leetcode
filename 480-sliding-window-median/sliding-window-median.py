from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lst = SortedList()
        result = []
        for i in range(len(nums)):
            lst.add(nums[i])
            if len(lst) > k:
                lst.remove(nums[i - k])
            if len(lst) == k:
                median = lst[k//2] if k % 2 == 1 else (lst[k // 2] + lst[k//2 -1])/2
                result.append(median)
        return result