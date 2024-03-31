class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(indx, subarray):
            if indx >= len(candidates) or sum(subarray) > target:
                return
            print("--------")
            print(subarray)
            val = candidates[indx]
            subarray.append(val)

            if sum(subarray) == target:
                print("adding to result:")
                print(subarray)
                result.append(subarray)
            print(subarray)
            print("going to recursion")
            
            backtracking(indx, subarray[:])
            backtracking(indx + 1, subarray[:-1])

        backtracking(0, [])
        return result