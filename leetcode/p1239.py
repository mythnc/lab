from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            letters = [0] * 26
            if not self.add_letters(letters, arr[i]):
                #print('failed in i')
                continue

            dp[i] = sum(letters)
            raw_letters = letters[:]
            for j in range(i+1, n):
                if not self.add_letters(letters, arr[j]):
                    #print('failed in j')
                    dp[i] = max(dp[i], sum(letters))
                    letters = raw_letters[:]
                    continue
            dp[i] = max(dp[i], sum(letters))

            #print(dp)
            #print(letters)

        return max(dp)

    def add_letters(self, letters, s):
        temp = [0] * 26
        for letter in s:
            index = ord(letter) - ord('a')
            if letters[index] > 0 or temp[index] > 0:
                return False
            temp[index] += 1

        for letter in s:
            letters[ord(letter) - ord('a')] += 1
        return True

print(Solution().maxLength(["un", "iq", "ue"])) #4
print(Solution().maxLength(["ab","ba","cd","dc","ef","fe","gh","hg","ij","ji","kl","lk","mn","nm","op","po"])) #16
print(Solution().maxLength(["yy","bkhwmpbiisbldzknpm"])) #0
print(Solution().maxLength(["a", "abc", "d", "de", "def"])) #6
