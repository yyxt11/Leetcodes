#因为是从左到右的三个部分,所以可以通过查找sum(A)/3 和sum(A)/3*2的点是否存在来判断
#同时需要满足题目的其他条件,比如 j > i 且部分点不能为空

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)

        if total % 3 != 0:
            return False
        else:
            itotal = sum(A)/3
            jtotal = sum(A)/3*2
            iindex,current = None,0
            for i,v in enumerate(A[:-1]):
                current += v
                if iindex is None:
                    if current == itotal:
                        iindex = i
                else:
                    if current == jtotal and i > iindex :
                        return True
            
            return False


        
