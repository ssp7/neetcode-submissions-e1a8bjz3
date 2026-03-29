class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        idx = len(cost) - 1
        while idx >= 0:
            first = 0 if idx + 1 >= len(cost) else cost[idx + 1] 
            second = 0 if idx + 2 >= len(cost) else cost[idx + 2]

            cost[idx] = cost[idx] + min(first, second)
            idx -= 1
        return min(cost[0], cost[1])