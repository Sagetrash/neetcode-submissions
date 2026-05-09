class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starts = set()

        for i in nums:
            if i-1 not in nums:
                starts.add(i)
        
        print(nums)
        print(starts)
        
        lcs = 0
        s = 1
        for i in starts:
            j = i
            s = 1
            while True:
                if j+1 in nums:
                    s+=1
                    j+=1
                else:
                    if lcs < s:
                        lcs = s
                    break
        return lcs