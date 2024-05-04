class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        for R in range(1, len(nums)):
            if nums[L] != nums[R]:
                L += 1
                nums[L] = nums[R]
            elif (L == 0 or nums[L] != nums[L - 1]) and L < R:
                L += 1
                nums[L] = nums[R]
        return L + 1