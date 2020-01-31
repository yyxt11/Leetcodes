#通过建立已走过的路径图ansmap来判断
#通过两个向量rdiction[0,1,0,-1 ] , cdirction[1,0,-1,0] 来控制正时针旋转的移动方向(i+1)% 4


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []

        R = len(matrix)
        C = len(matrix[0])
        ansmap = [[False]* C for _ in matrix]
        anslist =[]
        r,c,d = 0,0,0
        rd = [0,1,0,-1]
        cd = [1,0,-1,0]
        
        for i in range(R*C):
            anslist.append(matrix[r][c])
            ansmap[r][c] = True

            nextr,nextc = r+rd[d],c+cd[d]
  
            if 0 <= nextr < R and 0 <= nextc < C and not ansmap[nextr][nextc]:
                r,c = nextr,nextc   
            else:
                d = (d+1)%4
                r,c = r+rd[d],c+cd[d]
           

        return anslist



            

