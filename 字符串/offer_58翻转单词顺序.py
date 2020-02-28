#easy

class Solution:
    def reverseWords(self, s: str) -> str:
        ssplit = s.split(' ')
        
        newssplit = []
        for ss in ssplit[::-1]:
            if len(ss)> 0:
                newssplit.append(ss)

        
        return ' '.join(newssplit)

