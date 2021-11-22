class Solution:
    def reverseWords_built_in(self, s: str) -> str:
        return " ".join(s.split()[::-1])

    def reverseWords_slow(self, s: str) -> str:
        # from index n-1 to 0
        start = len(s) - 1
        result = []
        while start >= 0:
            # find first non-space character
            while start >= 0 and s[start] == ' ':
                start -= 1

            if start < 0:
                break

            # find first space character
            end = start - 1
            while end >= 0 and s[end] != ' ':
                end -= 1

            result.append(s[end+1:start+1])
            #print(f"end {end} start {start}")
            if end < 0:
                break

            if s[end] == ' ':
                start = end - 1
                continue

        return " ".join(result)

    def reverseWords_no_space(self, s: str) -> str:
        # from index n-1 to 0
        start = len(s) - 1
        output = ""
        while start >= 0:
            # find first non-space character
            while start >= 0 and s[start] == ' ':
                start -= 1

            if start < 0:
                break

            # find first space character
            end = start - 1
            while end >= 0 and s[end] != ' ':
                end -= 1

            output = f"{output} {s[end+1:start+1]}"
            if end < 0:
                break

            if s[end] == ' ':
                start = end - 1
                continue

        return output[1:]

print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("   hello world "))
print(Solution().reverseWords("a good   example"))
print(Solution().reverseWords("   Bob    Loves   Alice    "))
print(Solution().reverseWords("Alice does not even like bob"))
