from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # store temperature and it's index
        stack = []
        result = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                top_index = stack[-1][1]
                result[top_index] = i - top_index
                stack.pop()
            stack.append((temperature, i))
        return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # store temperature's index
        stack = []
        result = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                top_index = stack.pop()
                result[top_index] = i - top_index
            stack.append(i)
        return result


print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
