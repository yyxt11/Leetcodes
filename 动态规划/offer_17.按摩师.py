 
 #第i个位置是否接受预约,accept为接受,reject为不接受
 #动态规划,递归公司 dp[i] = max(dp[i-1],dp[i-2] + nums[i])

class Solution:
    def massage(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0


        reserve_accept,reserve_reject = nums[0],0

        for i in range(1,len(nums)):
            next_reserve_reject = max(reserve_reject,reserve_accept)

            next_reserve_accept = reserve_reject + nums[i]

            reserve_reject,reserve_accept = next_reserve_reject,next_reserve_accept


        return max(reserve_accept,reserve_reject)


            
