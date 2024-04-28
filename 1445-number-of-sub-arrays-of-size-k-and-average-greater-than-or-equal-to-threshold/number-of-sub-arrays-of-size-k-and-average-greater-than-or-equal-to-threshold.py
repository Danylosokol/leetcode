class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        curr_sum = 0
        result = 0

        for R in range(len(arr) + 1):
            if R - L + 1 > k:
                average = curr_sum / k
                if average >= threshold:
                    result += 1
                curr_sum -= arr[L]
                L += 1
            if R < len(arr):
                curr_sum += arr[R]
        
        return result