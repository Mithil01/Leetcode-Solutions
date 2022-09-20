class Solution:
    #T(n) = O(n**2), S(n) = O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [1]*n
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    #dp[j]+1 ensures we include current elem to already existing                         #subsequence while dp[i] ensures start the sequence from current
                    dp[i] = max(dp[j]+1,dp[i])
        
        #maximum of dp table will contain the maximum subsequence length
        return max(dp)