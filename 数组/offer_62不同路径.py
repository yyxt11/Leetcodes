#机器人巡径题,medium


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        waysstate = [[0]*m for i in range(0,n)]
   
        for i in range(0,m):
            for j in range(0,n): 
                if i == 0 or j == 0:
                    waysstate[j][i] = 1
                else:
                    waysstate[j][i] = waysstate[j][i-1] + waysstate[j-1][i]


        return waysstate[n-1][m-1]
