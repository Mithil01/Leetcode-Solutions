class Solution:
    #T(n) = O(nlogn) and S(n) = O(1)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        arrowsCnt = 1 #min 1 arrow needed since input constrains pt >= 1
        points.sort()  #To ease overlap finding 
        currRightEnd = points[0][1]
        
        for pt in points[1:]:
            if pt[0] <= currRightEnd :
                #Since we want to maximize bursting baloons w/ min arrows
                currRightEnd  = min(currRightEnd , pt[1])
            else:
                #Use new arrow
                arrowsCnt += 1
                currRightEnd  = pt[1]
                
        return arrowsCnt
        