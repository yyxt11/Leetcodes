#因为是求和的结果,所以< 0 的可以跳过


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
       
        if len(nums) == 1:
            return nums[0]
        else:
            bigsum = nums[0]  
            currentsum = nums[0]  
            for i in nums[1:]:
                currentsum =  max(i , currentsum+ i)    
                
                bigsum = max(bigsum,currentsum)        

        return bigsum

