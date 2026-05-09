class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            srt = ''.join(sorted(i))
            if srt in dic:
                dic[srt].append(i)
            else:
                dic[srt] = [i]
        return list(dic.values())