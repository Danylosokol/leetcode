class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(nums: List[int], s: int, e: int) -> List[int]:
            # print("s:")
            # print(s)
            # print("e:")
            # print(e)
            if e - s <= 0:
                # print("base case...")
                return nums
            
            m = (s + e)//2
            # print("nums before recursion:")
            # print(nums)
            mergeSort(nums, s, m)
            mergeSort(nums, m + 1, e)
            # print("nums after recursion:")
            # print(nums)
            # print("s and m and e")
            # print(s, m, e)
            left_part = nums[s:m + 1]
            # print("left_part:")
            # print(left_part)
            right_part = nums[m+1:e+1]
            # print("right_part:")
            # print(right_part)
            left_pointer = 0
            right_pointer = 0
            main_pointer = s
            while left_pointer < len(left_part) and right_pointer < len(right_part):
                if left_part[left_pointer] <= right_part[right_pointer]:
                    nums[main_pointer] = left_part[left_pointer]
                    main_pointer += 1
                    left_pointer += 1
                else:
                    nums[main_pointer] = right_part[right_pointer]
                    main_pointer += 1
                    right_pointer += 1
            if left_pointer >= len(left_part):
                while right_pointer < len(right_part):
                    nums[main_pointer] = right_part[right_pointer]
                    main_pointer += 1
                    right_pointer += 1
            else:
                while left_pointer < len(left_part):
                    nums[main_pointer] = left_part[left_pointer]
                    main_pointer += 1
                    left_pointer += 1
        
        # print("calling merge sort...")
        mergeSort(nums, 0, len(nums) - 1)
        return nums

    def insertionSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
        return nums