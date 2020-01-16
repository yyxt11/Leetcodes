# 1. 回溯算法,递归穷举



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digdict = {
                   '2':['a','b','c'],
                   '3':['d','e','f'],
                   '4':['g','h','i'],
                   '5':['j','k','l'],
                   '6':['m','n','o'],
                   '7':['p','q','r','s'],
                   '8':['t','u','v'],
                   '9':['w','x','y','z']
                   }

        output = []
        def backrecall(currentstring,next_digitstr):
            if len(next_digitstr) == 0:
                return output.append(currentstring)
            else:
                for letter in digdict[next_digitstr[0]]:
                    backrecall(currentstring + letter,next_digitstr[1:])


        if len(digits) > 0:
            backrecall('',digits)

        return output