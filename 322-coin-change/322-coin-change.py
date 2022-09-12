import sys

class Solution:
    #T(n) = O(amount*len(coins)) #S(n) = O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize for num in range(amount+1)]
        dp[0] = 0
        
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if coins[j] <= amount:
                    dp[i] = min(dp[i],dp[i-coins[j]] + 1)
                    
        if dp[amount] != sys.maxsize:
            return dp[amount]
        else :
            return -1