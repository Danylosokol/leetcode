class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]

        for i in nums:
            counts[i] += 1
        
        idx = 0
        for i in range(len(counts)):
            for _ in range(counts[i]):
                nums[idx] = i
                idx += 1
        

        