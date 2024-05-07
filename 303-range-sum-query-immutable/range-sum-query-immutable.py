class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pref = []
        total = 0
        for num in self.nums:
            total += num
            self.pref.append(total)

    def sumRange(self, left: int, right: int) -> int:
        prefRight = self.pref[right]
        prefLeft = self.pref[left - 1] if left > 0 else 0
        return prefRight - prefLeft 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)