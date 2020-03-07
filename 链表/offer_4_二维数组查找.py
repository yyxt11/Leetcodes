#二维数组查找,可以用最大值,最小值比较消除整行或者整列

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        rowindex = len(matrix) - 1
        columindex = 0

        while(rowindex >= 0 and columindex < len(matrix[0])):
            if matrix[rowindex][columindex] > target:
                rowindex -= 1
            elif matrix[rowindex][columindex] < target:
                columindex += 1
            else:
                return True
                
        return False
