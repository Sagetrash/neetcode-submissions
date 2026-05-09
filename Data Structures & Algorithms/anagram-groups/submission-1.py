class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            srtd = ''.join(sorted(i))
            if srtd not in dic:
                dic[srtd] = [i]
            else:
                dic[srtd].append(i)
        return list(dic.values())
