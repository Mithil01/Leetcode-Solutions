class Solution:
    #T(n) = O(n) and S(n) = O(n)
    def partitionLabels(self, s: str) -> List[int]:
        #To keep track of when to end the sub-partition
        lastOccurence = {c : i for i,c in enumerate(s)}
        
        end = start = 0
        result = list()
        
        for i,c in enumerate(s):
            #Ensures char belongs to one subpartition only.
            end = max(end, lastOccurence[c])
            
            if i == end:
                #subpartition is found, append its length to a list
                result.append(end -  start + 1)
                #start finding new sub-partition
                start = i + 1
        
        return result