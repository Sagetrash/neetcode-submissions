class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = []
        s = []
        uni = set()
        nums.sort()
        for i in nums:
            if i in uni:
                continue
            uni.add(i)
            if s == []:
                s.append(i)
            elif s[-1] == i-1:
                s.append(i)
            else:
                s = [i]
            # print(s)
            if len(lcs) < len(s):
                lcs = s
        return len(lcs)