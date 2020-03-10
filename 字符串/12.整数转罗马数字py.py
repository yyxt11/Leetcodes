#主要是注意5和10除余数的时候可以统一处理


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        Mnum = num//1000
        r = num - 1000*Mnum
        Cnum = r // 100
        r = r - 100*Cnum
        Xnum = r // 10
        r = r - 10*Xnum
        Inum = r
        
        romalist = ['M','C','X','I']
        romalist5 = ['D','L','V',]


        for i,V in enumerate([Mnum,Cnum,Xnum,Inum]):
            if i == 0:
                ans += romalist[i]*V
            else:
                if V == 4:
                    ans = ans + romalist[i] + romalist5[i-1] 
                elif V >= 5 and V < 9:
                    ans = ans  + romalist5[i-1] + romalist[i]*(V-5)
                elif V == 9:
                    ans = ans + romalist[i] + romalist[i-1]
                else:
                    ans += romalist[i]*V
        
        return ans

