class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(indx, subarray, curr_sum):
            if indx >= len(candidates) or curr_sum > target:
                return
            val = candidates[indx]
            subarray.append(val)
            curr_sum += val

            if curr_sum == target:
                result.append(subarray)
            
            backtracking(indx, subarray[:], curr_sum)
            backtracking(indx + 1, subarray[:-1], curr_sum - val)

        backtracking(0, [], 0)
        return result