class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        curr = float("inf")
        for p in prices:
            if curr > p:
                curr = p
            else:
                ans = max(ans, p - curr)

        return ans