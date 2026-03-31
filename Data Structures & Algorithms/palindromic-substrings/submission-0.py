class Solution:
    def countSubstrings(self, s: str) -> int:

        ans = set()        
        N = len(s)
        for idx in range(N):
            
            # even
            l, r = idx, idx + 1
            while l >= 0 and r < N and s[l] == s[r]:
                ans.add((l, r))
                l -= 1
                r += 1
            
            # odd
            l, r = idx, idx
            while l >= 0 and r < N and s[l] == s[r]:
                ans.add((l, r))
                l -= 1
                r += 1
        
        return len(ans)