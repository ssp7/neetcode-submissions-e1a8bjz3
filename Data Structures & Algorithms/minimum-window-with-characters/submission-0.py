class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        left = 0
        tCount, sCount = Counter(t), defaultdict(int)
        window = [0, float("inf")]
        need = len(tCount)
        have = 0

        for idx, char in enumerate(s):
            sCount[char] += 1

            if sCount[char] == tCount[char]:
                have += 1
            
            while have == need:
                if (idx - left) < (window[1] - window[0]):
                    window = [left, idx]
                
                
                sCount[s[left]] -= 1
                if sCount[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1
        
        return "".join(s[window[0]: window[1] + 1]) if window[1] != float("inf") else ""