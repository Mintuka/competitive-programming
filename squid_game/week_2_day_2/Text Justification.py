class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justify = []
        count = 0
        container = []
        
        for word in words:
            if count+len(word) > maxWidth:
                justify.append(container)
                count = 0
                container = []
            container.append(word)
            count += len(word)+1
        justify.append(container)
        
        for idx,lineWords in enumerate(justify):
            chars = 0
            for word in lineWords:
                chars += len(word)
            space = maxWidth - chars
            gaps = len(lineWords)-1
            evens = last = 0
            if gaps:
                evens = space//gaps
                last = space%gaps
            else:
                #if one word in lineWords
                last = space
            
            sp = ' '*evens
            sentence = []
            sentence.append(lineWords[0])
            if last:
                if gaps == 0:
                    sentence.append(sp+' '*last)
                else:
                    sentence.append(sp+' ')
                last -= 1
            else:
                sentence.append(sp)
            for i in range(1,len(lineWords)):
                sentence.append(lineWords[i])
                if last:
                    sentence.append(sp+' ')
                    last -= 1
                else:
                    sentence.append(sp)

            if len(sentence) > 2:
                sentence.pop()
            if idx < len(justify)-1:
                justify[idx] = ''.join(sentence)
            
        final = ' '.join(justify[-1])
        final += ' '*(maxWidth - len(final))
        justify[-1] = final
        
        return justify