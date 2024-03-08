class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left_pointer = 0
        for right_pointer in range(len(nums)):
            if nums[right_pointer] != val:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
        return left_pointer
        