import sys
class Solution:
    #T(n) = O(n**2) and S(n) = O(N**2) -> avoiding stack space
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        #filling dp[][] from bottom right corner to the top
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                #check first and last char(same?)
                if s[i] ==  s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                #dividing into n-1 problem and returning the max
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]