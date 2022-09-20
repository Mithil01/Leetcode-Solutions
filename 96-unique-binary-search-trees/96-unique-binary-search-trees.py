class Solution:
    #T(n) = O(n**2) ,O(n)
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(1,i+1):
                #using recursive formulation Summation((i-1)*(n-i)) for i ranging 
                #from i to n 
                dp[i] += dp[j-1]*dp[i-j]
        
        return dp[n]