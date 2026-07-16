class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        ans = 0
        left = 0

        for idx, char in enumerate(s):
            while char in characters:
                characters.remove(s[left])
                left += 1
            ans = max(ans, idx - left + 1)
            characters.add(char)
        
        return ans
            
