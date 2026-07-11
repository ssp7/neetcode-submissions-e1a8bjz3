class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = ""

        for c in s:
            if c.isalnum():
                sanitized += c
        
        print(sanitized)
        
        l, r = 0, len(sanitized) - 1
        while l < r:
            if sanitized[l].lower() != sanitized[r].lower():
                return False
            l += 1
            r -= 1

        return True