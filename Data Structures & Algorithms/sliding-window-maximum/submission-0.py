class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        left = right = 0
        dq = collections.deque()
        while right < len(nums):
            
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            dq.append(right)

            if left > dq[0]:
                dq.popleft()

            if (right - left) >= k - 1:
                ans.append(nums[dq[0]])
                left += 1

            right += 1


        return ans





'''

ans = []

dq = [1]

l = 0
r = 0





'''