class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, s, e):
            if e - s + 1 <= 1:
                return arr
            
            m = (s + e)//2

            mergeSort(arr, s, m)
            mergeSort(arr, m + 1, e)

            return merge(arr, s, m, e)
        
        def merge(arr, s, m, e):
            left = arr[s:m+1]
            right = arr[m+1:e+1]
            l = 0
            r = 0
            i = s

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    arr[i] = left[l]
                    l += 1
                else:
                    arr[i] = right[r]
                    r += 1
                i += 1
            
            while l < len(left):
                arr[i] = left[l]
                i += 1
                l += 1
            
            while r < len(right):
                arr[i] = right[r]
                i += 1
                r += 1
            
            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)