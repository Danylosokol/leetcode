class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            num = i
            num_of_bits = 0

            while num:
                num = num & (num - 1)
                num_of_bits += 1

            result.append(num_of_bits)
        
        return result