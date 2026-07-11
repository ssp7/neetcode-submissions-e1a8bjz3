class Solution:
    def trap(self, height: List[int]) -> int:
        lMaxes = []
        lMax = 0
        for h in height:
            lMax = max(h, lMax)
            lMaxes.append(lMax)
        
        rMax = 0
        area = 0
        for idx in range(len(height) - 1, -1, -1):
            rMax = max(rMax, height[idx])
            h = min(lMaxes[idx], rMax)
            area += max(0, h - height[idx])
        
        return area



'''
0 2 2 3 3 3 3 3 3 3

0
0

0 2 2 3 3 3 3 3 3 3

0 2 0 3 1 0 1 3 2 1
'''