class Solution:
    def reverseWords(self, s: str) -> str:
        words = (word for word in s.split())
        reverse_words = (w[::-1] for w in words)
        return " ".join(reverse_words)



print(Solution().reverseWords("Let's take LeetCode contest"))
