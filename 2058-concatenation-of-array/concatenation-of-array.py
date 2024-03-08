class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * 2 * len(nums)
        print(ans)
        for i in range(2):
            print(i)
            print(nums)
            for j in range(len(nums)):
                print(j)
                print(i*len(nums) + j)
                print("-------")
                ans[i*len(nums) + j] = nums[j]
        print(ans)
        return ans