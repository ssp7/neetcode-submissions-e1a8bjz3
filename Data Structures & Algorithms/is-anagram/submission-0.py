class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)

        
        return Counter(s) == Counter(t)