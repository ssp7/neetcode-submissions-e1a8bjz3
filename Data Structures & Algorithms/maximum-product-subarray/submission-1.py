class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        g_max = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for num in nums[1:]:
            candidates = (num, curr_max * num, curr_min * num)
            curr_max, curr_min = max(candidates), min(candidates)
            g_max = max(g_max, curr_max)
        
        return g_max