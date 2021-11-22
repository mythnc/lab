from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ary = list(s)
        result = self.backtrack(ary)
        return ["".join(i) for i in result]

    def backtrack(self, ary):
        #print(ary)
        n = len(ary)
        result = []
        has_alpha = False
        for i in range(n):
            if ary[i].isalpha():
                has_alpha = True
                back_s = [[]]
                if i != n-1:
                    # find next
                    back_s = self.backtrack(ary[i+1:])

                #print(back_s)
                for s in back_s:
                    #print(s)
                    result.append(ary[:i] + [ary[i].lower()] + s)
                    result.append(ary[:i] + [ary[i].upper()] + s)
                break

        if not has_alpha:
            return [["".join(ary)]]

        #print("result", result)
        return result


print(Solution().letterCasePermutation("0"))
print(Solution().letterCasePermutation("0a"))
print(Solution().letterCasePermutation("0a123"))
print(Solution().letterCasePermutation("0a1b"))
print(Solution().letterCasePermutation("a1b2"))
print(Solution().letterCasePermutation("abc"))
print(Solution().letterCasePermutation("3z4"))
print(Solution().letterCasePermutation("12345"))
