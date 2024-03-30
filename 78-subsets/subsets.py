class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(indx, subset):
            if indx >= len(nums):
                return result.append(subset)

            dfs(indx + 1, subset)
            dfs(indx + 1, subset + [nums[indx]])

        dfs(0, [])
        return result