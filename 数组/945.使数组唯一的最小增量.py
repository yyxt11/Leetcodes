#通过遍历扫描range len(A),此处因为考虑数组大小为40000,所以上限应该记为80000
#1.如果有重复的数组,放入一个重复数组中
#2.如果有未出现的数字,增将重复数组中的某个数字加到这个未出现的数字


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = [0] * 80000
        for x in A:
            count[x] += 1
        
        ans = taken = 0
        for x in range(80000):
            if count[x] >= 2:
                taken += count[x] - 1
                ans -= x * (count[x] - 1)
            elif taken > 0 and count[x] == 0:
                taken -= 1
                ans += x
        
        return ans





        




            





            

