#位运算标准体
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos,threes = 0,0,0

        for num in nums:
            #第一次出现为二进制位置1,第二第三次时候为1,通过ones 和 twos都置1标识为出现3次
            twos |= ones & num

            #第二次出现,某二进制置1, ones部分二进制位置0
            ones ^= num

            #第三次出现
            threes = ones & twos

            #将ones twos中出现了3次的二进制位清0
            ones &= ~threes
            twos &= ~threes

        return ones




        
