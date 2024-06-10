class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        def backtrack():
            if len(perm) == len(nums):
                res.append(perm[:])
            
            for num in counts:
                if counts[num] > 0:
                    perm.append(num)
                    counts[num] -= 1

                    backtrack()

                    perm.pop()
                    counts[num] += 1
            
        backtrack()
        return res
