class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for idx in range(len(nums) - 1, -1, -1):
            val = nums[idx]
            options = [1]
            for jdx in range(idx + 1, len(nums)):
                if val < nums[jdx]:
                    options.append(dp[jdx] + 1)
            dp[idx] = max(options)
        return max(dp)