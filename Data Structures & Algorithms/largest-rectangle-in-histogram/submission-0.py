class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for idx, h in enumerate(heights):
            idxToSet = idx
            while stack and stack[-1][1] > h:
                lastIdx, lastHeight = stack.pop()
                area = (idx - lastIdx) * lastHeight
                ans = max(ans, area)
                idxToSet = lastIdx
            stack.append([idxToSet, h])
            
        for idx, h in stack:
            area = (len(heights) - idx) * h
            ans = max(area, ans)
        
        return ans
        


'''
M.I.S

ans = 7

stack = [ [0, 7], ]

'''