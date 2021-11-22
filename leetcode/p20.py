class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_symbols = ('(', '[', '{')
        right_symbols = (')', ']', '}')
        for c in s:
            if c in left_symbols:
                stack.append(c)
                continue

            try:
                if right_symbols.index(c) != left_symbols.index(stack.pop()):
                    return False
            except IndexError:
                return False


        # return len(stack) == 0
        if len(stack) > 0:
            return False
        
        return True

print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))
