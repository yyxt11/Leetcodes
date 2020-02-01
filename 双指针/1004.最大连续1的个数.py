#未完成
#silding windows,双指针


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        lp,rp = 0,0
        ans = 0
        i = 0
        while(rp <len(A)):
            i = i + 1
            #为1
            if A[rp]:
                rp += 1
            #为0
            else:
                if K == 0:
                    print(lp,rp,K,ans,i)
                    ans = max(ans,rp-lp)
                    while(A[lp]):
                        lp += 1
                    lp += 1
                    #print(lp,rp,K,ans)
                else:
                    print(lp,rp,K,ans,i)
                    K = K-1       
                    if K <= 0:
                        #比较大小
                        ans = max(ans,rp-lp)
                        #移动到最近的0,优化
                        while(A[lp]):
                            lp += 1
                    #进一位重置
                    lp += 1
                    K += 1
            # rp移动
            rp += 1

        return ans




            
