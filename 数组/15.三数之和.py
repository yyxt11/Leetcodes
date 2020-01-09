#难重点在于去重
# 1. 数组排序
# 2. 遍历确定基准数, 基准数首先去重(是否和之前的数字相同)
# 3. 双指针双向遍历, 三数之和为0则保留, 双向遍历中需要去重(是否和之前的数字相同), 相同则跳过

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        #sort
        sortednums = sorted(nums)
        result = []

        # #del inde list
        # delindexlist = 

        for i,v in enumerate(sortednums):
            if v > 0:
                break
            if i > 0 and v == sortednums[i-1]:
                continue

            leftindex = i+1
            rightindex = len(nums) - 1
            
            while(leftindex < rightindex):
                if  v + sortednums[leftindex] + sortednums[rightindex] < 0:
                    leftindex += 1
                elif  v + sortednums[leftindex] + sortednums[rightindex] > 0:
                    rightindex = rightindex - 1
                else:
            
                    result.append([v, sortednums[leftindex] ,sortednums[rightindex]])
                    leftindex += 1
                    rightindex = rightindex - 1

                    #update index.prevent
                    while(leftindex < rightindex and sortednums[leftindex] == sortednums[leftindex -1]):
                        leftindex += 1
                    
                    while(leftindex < rightindex and sortednums[rightindex] == sortednums[rightindex+1]):
                        rightindex = rightindex - 1


        return result