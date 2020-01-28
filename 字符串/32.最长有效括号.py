#这种需要对称求解的题目都可以用栈解决，DP算法也可以


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #栈记录,-1 为0前面一位，类似指针加个前置的空指针
        leftstack = [-1]
        longestsub = 0
        for i,v in enumerate(s):
            #压入左括号
            if v == '(':
                leftstack.append(i)
            else:
                leftstack.pop()
                
                if len(leftstack) == 0:
                    leftstack.append(i)
                else:
                    validlen =  i - leftstack[-1] 
                    #print(validlen,i)
                    
                    longestsub = max(longestsub,validlen)
        
        return longestsub
