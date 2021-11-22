class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        # find non a
        ary = list(palindrome)
        for i in range(n//2):
            if palindrome[i] != 'a':
                ary[i] = 'a'
                return "".join(ary)

        # Change the last character to 'b'
        ary[n-1] = 'b'
        return "".join(ary)
