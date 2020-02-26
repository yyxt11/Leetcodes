#扑克牌中的顺子题,easy模式

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        numcurrent = maums)

        anynum = nums.count(0)

        count  = 1
        while(count <= 4):
            numcurrent = numcurrent - 1
            if numcurrent not in nums:
                if anynum > 0:
                    anynum = anynum - 1
                    count += 1
                else:
                    return False
            else:
                count += 1

        return True
            

