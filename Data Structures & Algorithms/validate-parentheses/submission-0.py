class Solution:
    def isValid(self, s: str) -> bool:
        s = []
        for i in s:
            if ord(s[-1]) == ord(i)+1:
                s.pop()
            else:
                s.append()
        if len(s) ==0:
            return True
        else: 
            return False