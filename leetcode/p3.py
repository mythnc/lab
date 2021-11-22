class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        start = 0
        end = 1
        max_ = 1
        set_ = {s[start]}
        while start < end < n:
            if s[end] not in set_:
                set_.add(s[end])
                end += 1
                max_ = max(max_, len(set_))
                continue

            while s[start] != s[end]:
                set_.remove(s[start])
                start += 1
            start += 1
            end += 1

        return max_

print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring(""))
