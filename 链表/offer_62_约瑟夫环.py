#约瑟夫环问题,可以用递归方法解决
#f(i) = (f(i-1) + m)%i

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        left = 0
        for i in range(2,n+1):
            left = (left + m) % i

        return left 
