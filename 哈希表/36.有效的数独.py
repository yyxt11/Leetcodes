#需要判断列,行,3x3是否有重复的0~9的数字,所以找个比较好的hashkey就可以


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhashtable = []
        columshashtable = []
        threeboardtable = []

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    rowhashkey = str(r) + num
                    if rowhashkey not in rowhashtable:
                        rowhashtable.append(rowhashkey)
                    else:
                        # print('r',rowhashtable)
                        return False

                    columshashkey = str(c) + num
                    if columshashkey not in columshashtable:
                        columshashtable.append(columshashkey)
                    else:
                        # print('c',columshashkey)
                        return False

                    threeboardtablekey = str(r // 3) + str(c // 3) + num
                    if threeboardtablekey not in threeboardtable:
                        threeboardtable.append(threeboardtablekey)
                    else:
                        # print('3X3',threeboardtablekey,r,c,threeboardtable)
                        return False

        return True