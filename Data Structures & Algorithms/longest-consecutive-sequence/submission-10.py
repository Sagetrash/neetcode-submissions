class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        starts = []
        for i in hashset:
            if i-1 not in hashset:
                starts.append(i)
        lcs = 0
        for strt in starts:
            curr = strt
            s = 1
            while (curr+1) in hashset:
                s+=1
                curr+=1
            if lcs <= s:
                lcs = s
        return lcs



