class Solution:
    def sortColors(self, nums: List[int]) -> None:
        pivot_l = 0
        pivot_r = 2

        l = 0
        r = len(nums) - 1
        idx = 0

        while idx <= r:
            if nums[idx] == pivot_l:
                nums[idx], nums[l] = nums[l], nums[idx]
                l += 1
            elif nums[idx] == pivot_r:
                nums[idx], nums[r] = nums[r], nums[idx] 
                r -= 1
                continue   
            idx += 1
            
            
    
        