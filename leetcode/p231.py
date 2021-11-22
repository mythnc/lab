class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b = bin(n)

        if b[2] != '1':
            return False

        for bit in b[3:]:
            if bit != '0':
                return False
        return True


print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(3))
print(Solution().isPowerOfTwo(4))
print(Solution().isPowerOfTwo(5))
print(Solution().isPowerOfTwo(-5))
print(Solution().isPowerOfTwo(0))
