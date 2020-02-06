#贪心算法优化


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        jumptable = [False for _ in range(len(nums))]
        jumptable[0] = True

        def canjump(v,jumptable):
            if any(jumptable[:v]):
                return True
            else:
                return False



        for i,v in enumerate(nums[::-1]):
            if i > 0:
                jumptable[i] = canjump(v,jumptable)


        return jumptable[-1]



        




            





            

