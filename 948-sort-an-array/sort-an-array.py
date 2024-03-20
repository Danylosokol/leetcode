class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSortHelper(nums):
            if len(nums) <= 1: return nums

            pivot = random.choice(nums)
            less_than, equal_to, greater_than = [], [], []

            for val in nums:
                if val < pivot: less_than.append(val)
                elif val > pivot: greater_than.append(val)
                else: equal_to.append(val)
            
            return quickSortHelper(less_than) + equal_to + quickSortHelper(greater_than)
        
        return quickSortHelper(nums)

        # def quickSortHelper(arr, s, e):
        #     if e - s + 1 <= 1:
        #         return arr
            
        #     # place a mid element to the end of array to use it as a pivot
        #     m = (s + e)//2
        #     arr[m], arr[e] = arr[e], arr[m]

        #     pivot = arr[e]
        #     j = s #slow pointer

        #     for i in range(s, e):
        #         if arr[i] < pivot:
        #             arr[j], arr[i] = arr[i], arr[j]
        #             j += 1

        #     arr[j], arr[e] = pivot, arr[j]

        #     quickSortHelper(arr, s, j-1)
        #     quickSortHelper(arr, j+1, e)

        #     return arr
        
        # return quickSortHelper(nums, 0, len(nums) - 1)

    # Merge sort O(nlogn)
    def mergeSort(self, nums: List[int]) -> List[int]:

        def merge(nums, s, m, e):
            left_part = nums[s:m + 1]
            right_part = nums[m+1:e+1]

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

            while right_pointer < len(right_part):
                nums[main_pointer] = right_part[right_pointer]
                main_pointer += 1
                right_pointer += 1
            while left_pointer < len(left_part):
                nums[main_pointer] = left_part[left_pointer]
                main_pointer += 1
                left_pointer += 1

        def mergeSortHelper(nums: List[int], s: int, e: int) -> List[int]:
            if e - s <= 0:
                return nums
            
            m = (s + e)//2

            mergeSortHelper(nums, s, m)
            mergeSortHelper(nums, m + 1, e)

            merge(nums, s, m, e)

            return nums
        
        return mergeSortHelper(nums, 0, len(nums) - 1)

    # Insertion sort O(n^2)
    def insertionSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
        return nums