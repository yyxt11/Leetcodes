#求余数,不能使用乘除和mod
#这边就是回归数学本质

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0

        sign = (dividend > 0) ^ (divisor>0)

        divid = abs(dividend)
        divis = abs(divisor)


        divisornum = divis
        count = 1
        while(divid>=divis):
            #print(res,divid,divisornum,divis)
            if divid >= divisornum:
                #指数次divisor倍数,加快减少速度
                divid = divid - divisornum
                res += count
                divisornum += divisornum
                count += count
            else:
                #重置倍数
                divisornum = divis
                count = 1

        if sign:
            res = 0 - res

        return min(max(-2**31, res), 2**31-1)

            




        
