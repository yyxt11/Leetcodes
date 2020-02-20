#一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
# 此方法对于和超过int长度的不大合适
#二分查找更好


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums) + 1
        totalshould = (n-1 + 0)* n/2
        totalreal = sum(nums)

        return int(totalshould -  totalreal)

        # def binaryfind(base,partsnums):
        #     if len(partsnums) == 0:
        #         return base+1

        #     middlenum = len(partsnums) / 2
        #     middleindex = math.flooerlen(partsnums) / 2

        #     if base + middlenum == partsnums[middleindex]:
        #         print('右边',base,middleindex,partsnums[middleindex+1:])
        #         r = binaryfind(base+middleindex,partsnums[middleindex+1:])
        #     else:
        #         print('左边',base,middleindex,partsnums[:middleindex])
        #         r = binaryfind(base,partsnums[:middleindex])
               

        #     return r

        # rr = binaryfind(0,nums)

        # return rr
