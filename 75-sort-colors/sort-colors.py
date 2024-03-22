class Solution:
    def sortColors(self, nums: List[int]) -> None:
        pivot_r = 2
        pivot_l = 0

        l = 0
        r = len(nums) - 1
        i = 0

        while i < len(nums) and i <= r:
            if nums[i] == pivot_l:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == pivot_r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
            
            
    
        