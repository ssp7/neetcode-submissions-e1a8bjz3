class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue

            l, r = idx + 1, len(nums) - 1
            while l < r:
                total = nums[idx] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ans.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
        
        return ans




'''
-1 0 0 1


'''