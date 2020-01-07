class Solution:
    def myAtoi(self, str: str) -> int:
        return max(min(2**31-1,int(*re.findall('^[\+\-]?\d+', str.lstrip()))),-2**31)