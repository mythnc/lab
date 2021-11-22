class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            try:
                j = numbers.index(target - numbers[i], i+1)
            except ValueError:
                pass
            else:
                return [i + 1, j + 1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                return [i + 1, j + 1]
            elif sum_ < target:
                i += 1
            else:
                j -= 1
