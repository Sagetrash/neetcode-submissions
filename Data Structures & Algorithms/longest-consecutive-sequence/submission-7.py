class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        starts = []
        for i in hashset:
            if i-1 not in hashset:
                starts.append(i)
        lcs = []
        for strt in starts:
            s = [strt]
            while (s[-1]+1) in hashset:
                s.append(s[-1]+1)
            if len(lcs) <= len(s):
                lcs = s
        return len(lcs)



