class Solution:
    def calculate(self, s: str) -> int:
        #remove white spaces
        s = "".join(s.split())
        infix = deque()
        i = 0
        while i < len(s):
            if s[i] in "+-*/": infix.append(s[i])
            nums = deque()
            while i < len(s) and s[i] not in "+-*/":
                nums.append(s[i])
                i += 1
            if nums:
                infix.append("".join(nums))
                i -= 1

            i += 1
        #convert into postfix expression
        s = infix.copy()
        opr = deque()
        opd = deque()
        for x in s:
            if x not in "*-/+":
                opd.append(x)
            else:
                while opr and opr[-1] in "*/" and x in "-+":
                        opd.append(opr.pop())
                while opr and opr[-1] in "-+" and x in "-+":
                        opd.append(opr.pop())
                while opr and opr[-1] in "*/" and x in "*/":
                        opd.append(opr.pop())
                opr.append(x)
                    
        while opr:
            opd.append(opr.pop())
            
        #calculate the postfix expression
        calc = deque()
        while opd:
            val = opd.popleft()
            if val in "+-*/":
                x1 = int(calc.pop())
                x2 = int(calc.pop())
                if val == "+":
                    calc.append(x2 + x1)
                elif val == "-":
                    calc.append(x2 - x1)
                elif val == "*":
                    calc.append(x2 * x1)
                elif val == "/":
                    calc.append(int(x2 / x1))
            else:
                calc.append(val)
        print(calc[0])
        return calc[0]