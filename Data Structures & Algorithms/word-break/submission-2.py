class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        words = set(wordDict)

        for idx in range(1, N + 1):
            for jdx in range(idx):
                if dp[jdx] and s[jdx: idx] in words:
                    dp[idx] = True

        return dp[N]