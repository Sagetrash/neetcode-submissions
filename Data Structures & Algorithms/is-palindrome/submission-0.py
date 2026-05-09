class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = ''
        for i in s:
            if i.isalnum():
                snew = snew + i
        snew = snew.lower()
        print(snew)
        if snew == snew[::-1]:
            return True
        return False