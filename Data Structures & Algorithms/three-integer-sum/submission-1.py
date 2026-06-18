class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        i = 0
        j = len(nums)-1
        k = (i+j)//2
        res = set()
        while i < k < j:
            sum= nums[i] + nums[j] + nums[k]
            if sum == 0:
                res.add((nums[i],nums[j],nums[k]))
                k+=1
            if sum > 0:
                j-=1
            if sum < 0:
                i += 1
        return list(res)

            
