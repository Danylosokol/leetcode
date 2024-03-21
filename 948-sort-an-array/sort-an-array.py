import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)
    
    def mergeSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
            
        m = (e + s)//2

        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m+1, e)

        return self.merge(arr, s, m, e)
    
    def merge(self, arr, s, m, e):
        left_part = arr[s:m+1]
        right_part = arr[m+1:e+1]

        l = 0
        r = 0
        i = s
        
        while l < len(left_part) and r < len(right_part):
            if left_part[l] <= right_part[r]:
                arr[i] = left_part[l]
                l += 1
            else: 
                arr[i] = right_part[r]
                r += 1
            i += 1

        while l < len(left_part):
            arr[i] = left_part[l]
            i += 1
            l += 1
        while r < len(right_part):
            arr[i] = right_part[r]
            i += 1
            r += 1

        return arr

            