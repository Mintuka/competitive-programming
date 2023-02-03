class Solution(object):
    def numberToWords(self, num):
        
        map_digits = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
                     11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",
                     18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",
                     80:"Eighty",90:"Ninety",100:"Hundred",1000:"Thousand",1000000:"Million",1000000000:"Billion"}

        if num == 0:
            return 'Zero'

        result = []
        level,factor = 0,3
        curr_num = num//1000
        curr_mod = num%1000
        
        while curr_num or curr_mod:
            if curr_mod and level:
                result.append(map_digits[1000**level])
            div = curr_mod
            i = 0
            while i < factor:
                if (div == curr_mod) and (11 <= div % 100 <= 19):
                    result.append(map_digits[div%100])
                    div = div // 100
                    i += 2
                else:
                    div, mod = divmod(div, 10
                    if mod:
                        if not i:
                            result.append(map_digits[mod])
                        elif i == 1:
                            result.append(map_digits[mod*10])
                        elif i == 2:
                            result.append(map_digits[100])
                            result.append(map_digits[mod])
                    i += 1

            curr_num, curr_mod = divmod(curr_num, 1000)
            level += 1

        return " ".join(reversed(result))