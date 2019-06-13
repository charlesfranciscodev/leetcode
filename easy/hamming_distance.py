class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        x_xor_y = x ^ y
        while x_xor_y > 0:
            distance += x_xor_y & 1
            x_xor_y >>= 1
        return distance
