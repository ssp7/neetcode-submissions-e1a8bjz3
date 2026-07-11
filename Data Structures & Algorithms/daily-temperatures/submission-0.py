class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stack = []

        for idx in range(len(temperatures)):
            temp = temperatures[idx]
            while stack and temperatures[stack[-1]] < temp:
                left = stack.pop()
                ans[left] = idx - left
            stack.append(idx)
        
        return ans


'''

[0, 0, 0, 0, 0, 0, 0]

[0]

[]

'''