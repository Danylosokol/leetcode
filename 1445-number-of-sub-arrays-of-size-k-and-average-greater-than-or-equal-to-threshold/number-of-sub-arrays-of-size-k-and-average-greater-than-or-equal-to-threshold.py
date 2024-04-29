class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = 0
        result = 0
        L = 0

        for R in range(len(arr) + 1):
            if R - L + 1 > k:
                average = currSum / k
                if average >= threshold:
                    result += 1
                currSum -= arr[L]
                L += 1
            if R < len(arr):
                currSum += arr[R]
        return result