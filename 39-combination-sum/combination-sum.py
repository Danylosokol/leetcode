class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(indx, subarray):
            if indx >= len(candidates) or sum(subarray) > target:
                return
            val = candidates[indx]
            subarray.append(val)

            if sum(subarray) == target:
                result.append(subarray)
            
            backtracking(indx, subarray[:])
            backtracking(indx + 1, subarray[:-1])

        backtracking(0, [])
        return result