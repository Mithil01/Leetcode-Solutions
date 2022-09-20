class Solution:
    #T(n) = O(n**2) and S(n) = O(n**2)
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[0]*n for _ in range(n)]
        max_len = 0
        result = " "
        
        #len=1 substring
        for i in range(n):
            dp[i][i] = 1
            max_len = 1
            result = s[i]
        
        #len=2 substring
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_len = 2
                result = s[i:i+2]
        
        #len = 3 to n substring
        for i in range(2,n):
            for j in range(i-1):
                #check first-last char match and in dp table check substr(from                       #second - secondlast char matches)
                if s[i] == s[j] and dp[j+1][i-1]:
                    dp[j][i] = 1
                    if max_len < i-j+1:
                        result = s[j:i+1]
                        max_len = i - j + 1
        return result
            