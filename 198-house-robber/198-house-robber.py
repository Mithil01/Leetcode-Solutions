class Solution:
    #T(n) = O(n), S(n) = 0(n)
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        
        if n == 1:
            return nums[0]
        
        else:
            dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        
            for i in range(2,n):
                dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        
        return dp[n-1]
        