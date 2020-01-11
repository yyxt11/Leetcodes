# 1. 遍历确定基准数,
# 2. 双指针双向遍历, 短边一侧向内靠拢，计算靠拢后的值并与之前的比较，保留较大者

class Solution:
    def maxArea(self, height: List[int]) -> int:
  
        if len(height) == 2:
            return height[1] if height[0] > height[1] else height[0]

        largestpool = 0
        lpoint = 0
        rpoint = len(height) - 1
        while(lpoint !=rpoint):
            #caculate
            if height[rpoint] >= height[lpoint]:
                currentpool = height[lpoint]*abs(lpoint-rpoint)
                lpoint = lpoint + 1
            else:
                currentpool = height[rpoint]*abs(lpoint-rpoint)
                rpoint = rpoint - 1

            #update pool
            if currentpool > largestpool:
                largestpool = currentpool
      

           
        return largestpool
