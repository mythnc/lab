class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left_bin = format(left, "031b")
        right_bin = format(right, "031b")

        i = 0
        while i < 31 and left_bin[i] == right_bin[i]:
                i += 1

        if i == 32:
            return left

        return int('0b' + left_bin[:i] + '0' * (31 - i), 2)



print(Solution().rangeBitwiseAnd(4, 7))
print(Solution().rangeBitwiseAnd(5, 7))
print(Solution().rangeBitwiseAnd(0, 0))
print(Solution().rangeBitwiseAnd(1, 2147483647))
print(Solution().rangeBitwiseAnd(6, 7))
