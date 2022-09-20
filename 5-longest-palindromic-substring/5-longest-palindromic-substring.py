class Solution:
    #T(n) = O(n**2) and S(n) = O(1)
    def checkaroundi(self,left,right,s,n,palinstr,max_len):
        
        while left >= 0 and right < n and s[left] == s[right]:
            if max_len < right - left + 1:
                max_len = right - left + 1
                palinstr = s[left: left + (right - left + 1)]
            
            left -= 1
            right += 1
            
        return max_len,palinstr
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n == 1:
            return s
        
        max_len = 1
        #string len is 1 
        palinstr = s[0] 
        
        #maintain two pointers, left and right towards either ends of i
        for i in range(1,n):
            #if substring is even len
            max_len,palinstr = self.checkaroundi(i-1,i,s,n,palinstr,max_len)
            #if substring is odd len
            max_len,palinstr = self.checkaroundi(i-1,i+1,s,n,palinstr,max_len)
        
        return palinstr