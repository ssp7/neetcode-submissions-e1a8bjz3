class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)

        def canEat(k):
            idx = 0
            time = 0
            while idx < len(piles):
                time += (piles[idx] // k)
                if piles[idx] % k:
                    time += + 1
                idx += 1
            
            return time <= h
        
        while left <= right:
            mid = (left + right) // 2
            if canEat(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
