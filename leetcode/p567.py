class Solution:
    # big O is s2_len
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False

        s1_freq = self.freq(s1)
        s2_freq = self.freq(s2[:s1_len])
        if s1_freq == s2_freq:
            return True
        for start in range(1, s2_len - s1_len + 1):
            end = start + s1_len
            # update s2_freq
            pre_letter_index = ord(s2[start-1]) - ord('a')
            new_letter_index = ord(s2[end-1]) - ord('a')
            s2_freq[pre_letter_index] -= 1
            s2_freq[new_letter_index] += 1
            if s1_freq == s2_freq:
                return True

        return False

    def freq(self, s):
        result = [0] * 26
        for letter in s:
            index = ord(letter) - ord('a')
            result[index] += 1
        return result

class SolutionSlow:
    # big O is s1_len * s2_len
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False

        s1_freq = self.freq(s1)
        for start in range(s2_len - s1_len + 1):
            end = start + s1_len
            s2_freq = self.freq(s2[start:end])
            if s1_freq == s2_freq:
                return True

        return False

    def freq(self, s):
        result = [0] * 26
        for letter in s:
            index = ord(letter) - ord('a')
            result[index] += 1
        return result
