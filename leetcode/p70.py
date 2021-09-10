class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {
            1: 1,
            2: 2,
        }
        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]
        
        return steps[n]
