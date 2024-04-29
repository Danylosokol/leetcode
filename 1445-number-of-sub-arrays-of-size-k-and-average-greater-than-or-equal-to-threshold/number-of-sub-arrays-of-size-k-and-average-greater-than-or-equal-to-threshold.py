class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = 0
        result = 0
        L = 0

        for R in range(len(arr)):
            if R - L + 1 > k:
                currSum -= arr[L]
                L += 1
            currSum += arr[R]
            if (R - L + 1 == k) and ((currSum / k) >= threshold):
                result += 1
        return result