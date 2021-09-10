class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = {
            0: 0,
            1: 0,
        }
        
        n = len(cost)
        for i in range(2, n+1):
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2])

        return min_cost[n]
