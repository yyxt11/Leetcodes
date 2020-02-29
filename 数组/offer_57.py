#设立左右指针, 逐步向中心递进的方式

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            return nums

        pl = 0
        pr = len(nums) - 1


        while(pl < pr):
            if nums[pl] + nums[pr] < target:
                pl += 1
            elif nums[pl] + nums[pr] > target:
                pr = pr -1 
            else:
                break

        return [nums[pl], nums[pr]]



