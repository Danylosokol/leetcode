class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_sub = 1
        curr_sub = 1

        is_last_more = False
        is_last_less = False
        last_val = arr[0]

        for num in arr[1:]:
            print("curr number:")
            print(num)
            if not is_last_more and not is_last_less:
                print("initial setting:")
                if last_val > num:
                    is_last_more = True
                    is_last_less = False
                    curr_sub += 1
                    print("last_num is bigger")
                elif last_val < num:
                    is_last_less = True
                    is_last_more = False
                    print("last_num is smalles")
                    curr_sub += 1
                else:
                    print("last num is the same")
                    curr_sub = 1
            elif is_last_more and last_val < num:
                print("continue array, last_num is smalles")
                is_last_less = True
                is_last_more = False
                curr_sub += 1
            elif is_last_less and last_val > num:
                print("continue array, last_num is bigger")
                is_last_more = True
                is_last_less = False
                curr_sub += 1
            else:
                print("ressetting array")
                is_last_more = last_val > num
                is_last_less = last_val < num
                if last_val != num:
                    curr_sub = 2
                else:
                    curr_sub = 1
            last_val = num
            max_sub = max(max_sub, curr_sub)

        return max_sub            
            
