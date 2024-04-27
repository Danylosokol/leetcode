class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_sub = 1
        curr_sub = 1

        is_last_more = False
        is_last_less = False
        last_val = arr[0]

        for num in arr[1:]:
            if not is_last_more and not is_last_less:
                if last_val > num:
                    is_last_more = True
                    is_last_less = False
                    curr_sub += 1
                elif last_val < num:
                    is_last_less = True
                    is_last_more = False
                    curr_sub += 1
                else:
                    curr_sub = 1
            elif is_last_more and last_val < num:
                is_last_less = True
                is_last_more = False
                curr_sub += 1
            elif is_last_less and last_val > num:
                is_last_more = True
                is_last_less = False
                curr_sub += 1
            else:
                is_last_more = last_val > num
                is_last_less = last_val < num
                if last_val != num:
                    curr_sub = 2
                else:
                    curr_sub = 1
            last_val = num
            max_sub = max(max_sub, curr_sub)

        return max_sub            
            
