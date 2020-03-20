#这个方法取巧了,这种取K个最大最小的,可以用堆排序去做


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 0:
            return arr
        arr.sort()

        return arr[:k]