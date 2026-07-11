class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        prefix = 1

        for idx in range(len(nums)):
            ans[idx] = prefix * ans[idx]
            prefix *= nums[idx]
        
        prefix = 1

        for idx in range(len(nums) - 1, -1, -1):
            ans[idx] = prefix * ans[idx]
            prefix *= nums[idx]
        
        return ans