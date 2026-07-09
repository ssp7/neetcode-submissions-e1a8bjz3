class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in map:
                return [map[diff], idx]
            map[nums[idx]] = idx
        
        return [-1, -1]