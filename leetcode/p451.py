from collections import Counter


class Solution:
    # 54 ms
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        return "".join(char * times for char, times in count.most_common())

    # 65 ms
    def frequencySort_s(self, s: str) -> str:
        count = Counter(s)
        result = ""
        for char, times in count.most_common():
            result += char * times
        return result

    # 73 ms
    def frequencySort_s(self, s: str) -> str:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        return "".join(char * times for char, times in sorted(d.items(), key=lambda x: x[1], reverse=True))

        

print(Solution().frequencySort("tree"))
print(Solution().frequencySort("Aabb"))
