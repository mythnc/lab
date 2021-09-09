class Solution:
    def fib(self, n: int) -> int:
        table = {}
        table[0] = 0
        table[1] = 1
        for i in range(2, 31):
            table[i] = table[i-1] + table[i-2]
        return table[n]
