from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shift = lambda c, x: chr((ord(c) - ord('a') + x) % 26 + ord('a'))
        
        for i in range(len(shifts)-1, 0, -1):
            shifts[i-1] += shifts[i]

        return "".join([shift(c, x) for c, x, in zip(s, shifts)])


print(Solution().shiftingLetters("abc", [3,5,9]))
print(Solution().shiftingLetters("aaa", [1,2,3]))
print(Solution().shiftingLetters("ruu", [26,9,17]))
