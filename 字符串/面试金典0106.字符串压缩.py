#easy

class Solution:
    def compressString(self, S: str) -> str:
        
        if len(S)<=1:
            return S

        Slist = list(S)
        Sresult = ''
        count = 1
        for i,v in enumerate(Slist):
            if i == 0:
                Sresult += v
            else:
                if v == Slist[i-1]:
                    count += 1
                else:
                    Sresult = Sresult + str(count) + v
                    count = 1
        
        Sresult += str(count)

        return Sresult if len(Sresult) < len(S) else S
        



            
           

