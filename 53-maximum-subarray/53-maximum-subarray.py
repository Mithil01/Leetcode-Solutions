class Solution:
    #T(n) = O(n) and S(n) = O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = nums[0]
        currsum = 0
        
        for num in nums:
            #if subarray sum until current element is -ve, ignore it and start with curr elem
            currsum = max(0,currsum)
            currsum += num
            maxsum = max(maxsum,currsum)
        
        return maxsum