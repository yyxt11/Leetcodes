# 1. 回溯算法,递归穷举
#只有在我们知道序列仍然保持有效时才添加 '(' or ')'，而不是每次添加。我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点
#当还有位置可以放的时候,先放置一个左括号. 如果右括号的数量不超过左括号,也可以放置一个右括号



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backward(S,left,right):
            if len(S) == 2*n:
                ans.append(S)
                return 
            if left < n:
                backward(S+'(',left+1,right)

            if right < left:
                backward(S+')',left,right+1)

        backward('',0,0)
        return ans

        