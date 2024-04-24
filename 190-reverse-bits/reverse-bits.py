class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            # get the current last bit (ones bit) in our number
            bit = (n >> i) & 1
            # place the bit to the beginning of the result
            # OR will reutrn one only when bit is one
            result = result | (bit << (31 - i))
        return result