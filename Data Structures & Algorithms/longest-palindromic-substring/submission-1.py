class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_even = len(s) % 2 == 0
        ans = 0
        start = 0
        for idx, char in enumerate(s):
            l, r = idx, idx + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > ans:
                    ans = r - l + 1
                    start = l
                l -= 1
                r += 1

            l, r = idx, idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > ans:
                    ans = r - l + 1
                    start = l
                l -= 1
                r += 1

        return s[start: start + ans]