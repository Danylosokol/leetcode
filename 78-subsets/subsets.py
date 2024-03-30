class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(indx):
            if indx >= len(nums):
                return result.append(subset[:])
            
            subset.append(nums[indx])
            dfs(indx + 1)

            subset.pop()
            dfs(indx + 1)

        dfs(0)
        return result