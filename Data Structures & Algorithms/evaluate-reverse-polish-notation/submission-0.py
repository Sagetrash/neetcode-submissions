class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oprs = {'+':self.add,'-':self.sub,'*':self.mul,'/':self.div}
        for i in tokens:
            if i not in oprs:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(oprs[i](a,b))
        return stack[-1]
    def div(self,a,b) -> int:
        return int(a/b)
    def mul(self,a,b) -> int:
        return a*b
    def sub(self,a,b) -> int:
        return a-b
    def add(self,a,b) -> int:
        return a+b