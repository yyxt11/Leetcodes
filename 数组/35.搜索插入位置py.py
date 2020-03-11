#二分查找查找插入位置


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        def binarysearch(nums,target,index):
    
            if len(nums) == 1:
                if nums[0] == target:
                    return index
                elif nums[0] < target:
                    return index + 1
                else:
                    return max(index - 1,0)
            else:
                middleindex = len(nums)//2

                if nums[middleindex] > target:
                    return binarysearch(nums[:middleindex],target,index)
                elif nums[middleindex] < target:
                    return binarysearch(nums[middleindex:],target,index+middleindex)
                else:
                    return index+middleindex

        ans = binarysearch(nums,target,0)

        return ans


        
