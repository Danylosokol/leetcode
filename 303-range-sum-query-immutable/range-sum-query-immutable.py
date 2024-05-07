class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pref = []
        total = 0
        for num in self.nums:
            total += num
            self.pref.append(total)
        print(self.pref)

    def sumRange(self, left: int, right: int) -> int:
        print("initial left and right:")
        print(left)
        print(right)
        prefRight = self.pref[right]
        prefLeft = self.pref[left - 1] if left > 0 else 0
        print("pref left and right:")
        print(prefLeft)
        print(prefRight)
        return prefRight - prefLeft 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)