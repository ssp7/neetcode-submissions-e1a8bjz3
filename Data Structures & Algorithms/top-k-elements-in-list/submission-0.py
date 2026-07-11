class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        keys = list(count.keys())

        keys.sort(reverse = True, key = count.get)

        return keys[:k]