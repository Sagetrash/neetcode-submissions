class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res = res + f"{len(i)}#" + i
        return res

    def decode(self, s: str) -> List[str]:
        count = 0
        res = []
        i = 0
        strr = ''
        while i < len(s):
            if s[i] == '#':
                count = int(strr)
                res.append(s[i+1:i+count+1])
                i = i + count + 1
                strr = ''
                continue
            strr = strr + s[i]
            i = i+1
        return(res)

            
             
            
                

