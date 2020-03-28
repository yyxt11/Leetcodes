#基本数学题
#寻找同样后缀的词,将其从words_set中删除
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        for word in words:
            for k in range(1,len(word)):           
                words_set.discard(word[k:])
                
        return sum(len(word)+1 for word in words_set)