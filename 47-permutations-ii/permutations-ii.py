class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        counts = {num:0 for num in nums}
        for num in nums:
            counts[num] += 1
        
        def backtrack():
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for num in counts:
                if counts[num] > 0:
                    perm.append(num)
                    counts[num] -= 1

                    backtrack()

                    perm.pop()
                    counts[num] += 1
        
        backtrack()
        return result