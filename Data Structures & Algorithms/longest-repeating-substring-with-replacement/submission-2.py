class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        map = defaultdict(int)
        left = 0
        ans = 0
        maxVal = 0

        for idx, char in enumerate(s):
            map[char] += 1
            maxVal = max(maxVal, map[char])

            while (idx - left - maxVal) > (k - 1):
                map[s[left]] -= 1
                left += 1
            ans = max(ans, idx - left + 1)

        return ans


'''

{ A: 1}

left = 0
idx = 0

A A B A B B A



'''