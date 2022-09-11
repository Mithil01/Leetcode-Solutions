class Solution:
    #T(n) = O(m*n) and S(n) = O(m*n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1:
            return 0 
        
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        
        #memoization
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = 1 
        
        for i in range(m):
            for j in range(n):
                    # Oth row and 0th col, only 1 path
                    if i == 0 or j == 0:
                        #check if there is obstacle(Yes -> make cell as 0)
                        if obstacleGrid[i][j] == 1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = 1
                    
                    #to handle : [[0,0],[1,1],[0,0] like scenarios]
                    if (i > 0 and dp[i-1][j] ==0) or (j > 0 and dp[i][j-1] == 0):
                            dp[i][j] = 0 
                            
                    # add paths of the previous cells(left and above one)        
                    if i>0 and j >0:
                        if obstacleGrid[i][j] == 1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
                    