class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
        ']' : '[',
        ')' : '(',
        '}':'{'
        }
        stack = ["$"]
        for i in s:
            if brackets.get(i,0) == stack[-1]:  
                stack.pop()
            else:
                stack.append(i)
            print(stack)
        if stack[-1] == "$":
            return True
        else:
            return False