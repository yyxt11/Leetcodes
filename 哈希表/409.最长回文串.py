#因为是构建回文串，一对一对对称的，所以
#1.可以通过%2来计算到底有多少是遗留下来的独个的
#2.独个的可以最多再额外加上一个


class Solution:
    def longestPalindrome(self, s: str) -> int:

        minus_num = sum([s.count(ss)%2 for ss in set(s)]) - 1 

        return len(s) - max(0,minus_num)