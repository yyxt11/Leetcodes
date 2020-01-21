#最长回文串基础题
#通过遍历 + 向两边同时衍生找相同字符的方法


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        maxlen = 0
        start,end = 0,0
        
        def getPalindromelen(s,l,r):
            while(l>=0 and r< len(s)):
                if s[l] == s[r]:
                    l = l -1
                    r = r + 1
                else:
                    break
                    
            return l,r



        for i,v in enumerate(s):
            l1,r1 = getPalindromelen(s,i,i)
            l2,r2 = getPalindromelen(s,i,i+1)

            comlen = 0
            
            if r2 - l2 >= r1 - l1:
                if r2 - l2 > maxlen:
                    maxlen = r2 - l2
                    start = l2+1
                    end = r2
            else:
                if r1 -l1 > maxlen:
                    maxlen = r1 - l1
                    start = l1+1
                    end = r1
                    

        return s[start:end]
