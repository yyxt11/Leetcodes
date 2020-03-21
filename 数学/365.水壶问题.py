#方法一.DFS暴力搜索法,这个有些案例会超时
#遍历所有的操作,同时为了记录,用self.state记录当前状态
#1.X满上
#2.Y满上
#3.X倒入Y中,直到Y满或者倒空
#4.Y倒入X中,直到X满或者倒空
#5.X倒空
#6.Y倒空


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0,0)]
        self.state = set()


        while(stack):
            remainX,remainY = stack.pop()

            if remainX == z or remainY == z or remainY+remainX == z:
                return True

            if (remainX,remainY) in self.state:
                continue

            self.state.add((remainX,remainY))
                
            stack.append((x,remainY))
            stack.append((remainX,y))
            stack.append((x-min(remainX,y-remainY),remainY + min(remainX,y-remainY)))
            stack.append((remainX + min(remainY,x-remainX),y-min(remainY,x-remainX)))
            stack.append((0,remainY))
            stack.append((remainX,0))

        return False



#方法2,贝祖定律
#求一对整数,使得ax+by = z,也就是最大公约数
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0 :
            return z==0 or x+y == z

        return z % math.gcd(x,y) == 0
