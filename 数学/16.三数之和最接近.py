#超时,待解决

class Solution:
    def threeSumClosest(self, nums, target):

        if len(nums) <= 3:
            result = 0

            for n in nums:
                result += n

            return result

        else:
            sortednums = sorted(nums)
            result = None
            for i, s in enumerate(sortednums):


                if i > 0 and s == sortednums[i - 1]:
                    continue

                ileft = i + 1
                iright = i + 2

                compareresult = None
                closestset = None
                preminus = None
                bound = len(nums) - 1

                while (iright <= bound):
                    nextminus = s + sortednums[ileft] + sortednums[iright] - target

                # perfect
                    if nextminus == 0:
                        compareresult = target
                        break

                    if closestset is None:
                        closestset = nextminus
                        compareresult = nextminus + target

                    else:

                        if abs(nextminus) < abs(closestset):
                            compareresult = nextminus + target
                            closestset = nextminus
                        else:
                            if preminus >0 and abs(nextminus) > abs(preminus):
                                ileft += 1
                                iright = ileft + 1
                                preminus = nextminus
                                continue



                    preminus = nextminus
                    iright = iright + 1
                    if iright > bound:
                        ileft += 1
                        iright = ileft + 1



                if result is None:

                    result = compareresult
                elif compareresult is not None:
                    if abs(result - target) > abs(compareresult - target):

                        result = compareresult

            return result


if __name__ == '__main__':
    l = [1,6,9,14,16,70]
    n = 81

    A = Solution()
    B = A.threeSumClosest(l,n)
    print(B)
