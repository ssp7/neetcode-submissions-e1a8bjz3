class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dist = [[p, s] for p, s in zip(position, speed)]
        dist.sort(key= lambda dist: dist[0])
        stack = []
        for p, s in reversed(dist):
            t = (target - p) / s
            timeToSet = t
            if stack and stack[-1] >= t:
                timeToSet = stack.pop()
            stack.append(timeToSet)
    
        return len(stack)


'''

[0, 10] [1, 7] [2, 2] [3, 6] [4, 6] [5, 9]
s = []





'''