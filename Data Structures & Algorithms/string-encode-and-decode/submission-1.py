class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for s in strs:
            code = f'{code}{len(s)}#{s}'
        # print(code)
        return code
    def decode(self, s: str) -> List[str]:
        res = []
        count = ''
        i = 0
        while i < len(s):
            print(count)
            if s[i] == '#':
                i += 1
                count = int(count)
                res.append(s[i:i+count])
                i += count
                count = ''
                continue            
            count = count+s[i]
            i += 1
        return res

