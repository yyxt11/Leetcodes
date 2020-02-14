#难度:简单


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer_str = [0 for i in range(max(len(a),len(b))+1) ]

        al,bl = list(a)[::-1],list(b)[::-1]

        dist  = abs(len(al) - len(bl))
       # print(al,bl,answer_str)
        if len(al) > len(bl):
            bl = bl + [0 for i in range(dist)] 
        elif len(al) < len(bl):
            al = al + [0 for i in range(dist)] 
            
        for i,v in enumerate(al):
            #print(answer_str)
            if al[i] == '1' and bl[i] == '1':
                
                answer_str[i+1] = 1
            elif al[i] == '1' or bl[i] == '1':
                if answer_str[i]:
                    answer_str[i] = 0
                    answer_str[i+1] = 1
                else:
                    answer_str[i] = 1

        answer_str = answer_str[::-1]

       # print(answer_str)
        if answer_str[0] == 0:
            answer_str = answer_str[1:]


        return ''.join([str(a) for a in answer_str])



            



