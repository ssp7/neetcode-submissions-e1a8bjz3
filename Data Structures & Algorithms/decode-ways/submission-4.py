class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N == 0 or s[0] == '0': return 0
        if N == 1: return 1

        def canInclude(c1, c2):
            val = (int(c1) * 10) + int(c2)
            return 10 <= val <= 26 
        
        dp = [0] * N
        dp[0] = 1
        dp[1] = dp[0] if s[1] != '0' else 0
        if canInclude(s[0], s[1]):
            dp[1] += dp[0]
        idx = 2
        while idx < N:
            dp[idx] = dp[idx - 1] if s[idx] != '0' else 0
            if canInclude(s[idx - 1], s[idx]):
                dp[idx] += dp[idx - 2]
            idx += 1
        
        return dp[-1]