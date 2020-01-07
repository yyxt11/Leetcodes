class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows <= 1:
            return s

        rowindex = 0
        down = False
        charmap = [[]for i in range(numRows)]
        
        for i,v in enumerate(s):
            
            charmap[rowindex].append(v)
            if rowindex == 0 or rowindex == numRows - 1:
                down = False if down else True

            if down:
                rowindex += 1
            else:
                rowindex = rowindex - 1

        vv  = ''

        for v in charmap:
            vv  = vv + ''.join(v)

        return vv