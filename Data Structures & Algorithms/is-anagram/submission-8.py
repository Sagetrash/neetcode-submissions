class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = set(s)
        b = set(t)
        return a==b and len(s) == len(t)