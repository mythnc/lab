from typing import List


# slow
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        # make hash
        values = []
        times = []
        for n in nums:
            if n in values:
                times[values.index(n)] += 1
            else:
                values.append(n)
                times.append(1)
        # dp
        dp = [0] * len(values)
        for index, value in enumerate(values):
            dp[index] = value * times[index]
            if index > 0 and value-1 == values[index-1]:
                previous_max_index = index-1
            else:
                previous_max_index = index
            dp[index] += self.get_max(dp, previous_max_index)
        return max(dp)

    def get_max(self, dp, index):
        try:
            return max(dp[:index])
        except ValueError:
            return 0

class Solution2:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        # make hash
        num_times = {}
        for n in nums:
            try:
                num_times[n] += 1
            except KeyError:
                num_times[n] = 1
        # dp
        previous_max = 0
        current_max = 0
        for key in num_times:
            if key-1 in num_times:
                temp = num_times[key] * key + previous_max
            else:
                temp = num_times[key] * key + current_max
            previous_max = current_max
            current_max = max(temp, current_max)
        return current_max


print(Solution().deleteAndEarn([3,4,2])) #6
print(Solution().deleteAndEarn([2,2,3,3,3,4])) #9
print(Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6])) #18

print(Solution2().deleteAndEarn([3,4,2])) #6
print(Solution2().deleteAndEarn([2,2,3,3,3,4])) #9
print(Solution2().deleteAndEarn([1,1,1,2,4,5,5,5,6])) #18
