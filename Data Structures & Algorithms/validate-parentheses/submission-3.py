class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in brackets:
                if brackets[i] != stack[-1]:
                    return False
                else:
                    if stack:
                        stack.pop()
            else:
                stack.append(i)
        return True