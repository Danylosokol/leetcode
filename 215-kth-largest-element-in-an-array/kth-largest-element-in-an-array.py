class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = self.mergeSort(nums, 0, len(nums) - 1)
        return sorted_nums[-k]

    def mergeSort(self, nums, s, e):
        if e - s + 1 <= 1:
            return nums
        
        m = (e + s)//2

        self.mergeSort(nums, s, m)
        self.mergeSort(nums, m + 1, e)

        return self.merge(nums, s, m, e)

    def merge(self, nums, s, m, e):
        left_part = nums[s:m+1]
        right_part = nums[m+1:e+1]

        l = 0
        r = 0
        k = s

        while l < len(left_part) and r < len(right_part):
            if left_part[l] <= right_part[r]:
                nums[k] = left_part[l]
                l += 1
            else:
                nums[k] = right_part[r]
                r += 1
            k += 1

        while l < len(left_part):
            nums[k] = left_part[l]
            k += 1
            l += 1
        while r < len(right_part):
            nums[k] = right_part[r]
            k += 1
            r += 1
        
        return nums

    