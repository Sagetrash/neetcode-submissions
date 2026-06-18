class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = set()
        r = len(nums)-1
        for l in range(0,len(nums)-2):
            m = l+1
            while(m<r):
                sm = nums[l] + nums[m] + nums[r]
                if sm == 0:
                    out.add((nums[l],nums[m],nums[r]))
                if sm < 0:
                    m += 1
                else:
                    r -= 1
            l += 1
            r = len(nums)-1
        return list(out)