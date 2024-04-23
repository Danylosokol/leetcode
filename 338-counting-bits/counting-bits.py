class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            curr_val = i
            num_of_bits = 0
            while curr_val:
                if curr_val & 1:
                    num_of_bits += 1
                curr_val = curr_val >> 1
            result.append(num_of_bits)
        
        return result