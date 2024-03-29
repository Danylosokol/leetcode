class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]

        num = nums[0]

        subsets_without_num = self.subsets(nums[1:])
        subsets_with_num = [[num] + subset for subset in subsets_without_num]
        
        return subsets_with_num + subsets_without_num
        