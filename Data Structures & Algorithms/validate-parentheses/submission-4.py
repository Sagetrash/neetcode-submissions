class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(',']':'[','}':'{'}
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i in brackets:
                if brackets[i] != stack[-1]:
                    return False
                elif brackets[i] == stack[-1]:
                    stack.pop()
            else:
                stack.append(i)
        return True