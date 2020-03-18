#基本数学题
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        xlinecover,ylinecover = True,True
        if rec1[2] >= rec2[2]:
            xbig,xsmall = rec1,rec2
        else: 
            xbig,xsmall = rec2,rec1

        if rec1[3] >= rec2[3]:
            ybig,ysmall = rec1,rec2 
        else: 
            ybig,ysmall = rec2,rec1
  
        if xbig[0] >= xsmall[2]:
            xlinecover = False
        if ybig[1] >= ysmall[3]:
            ylinecover = False

        return xlinecover & ylinecover