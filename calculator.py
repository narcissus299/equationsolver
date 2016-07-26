class Calculator:

    def post(self,eq):
        heirarchy = ['-','+','*','/']
        post = ""
        stack = []
        for c in eq:
            if c.isdigit() or c=='.':
                post = post + c
            elif c == '(':
                stack.append(c)
                post = post+" "
            elif c == ')':
                p = stack.pop()
                while not p == '(':
                    post = post+" "+p
                    p = stack.pop()
            else:
                while  stack and heirarchy.index(c) < heirarchy.index(stack[-1]):
                    post = post+" "+stack.pop()
                stack.append(c)
                post = post + " "
        for item in stack[::-1]: post = post + " " + item
        return post.strip()

    def calc(self,eq):
        def add(y,x):
            return x+y
        def sub(y,x):
            return x-y
        def mul(y,x):
            return x*y
        def div(y,x):
            return x/y
        funcmap = {'+':add,'-':sub,'*':mul,'/':div}
        stack = []
        digit = ""
        for e in eq:
            if e == " " and digit:
                stack.append(float(digit.strip()))
                digit = ""
            elif e.isdigit() or e=='.':
                digit = digit+e
            elif not e==' ':
                operation = funcmap[e]
                result = operation(stack.pop(),stack.pop())
                stack.append(result)
        return stack.pop()

    def evaluate(self,eq):
        return self.calc(self.post(eq))