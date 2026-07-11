class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            if not (num - 1) in s:
                curr = 1
                while num + 1 in s:
                    num += 1
                    curr += 1

                ans = max(curr, ans)
        
        return ans