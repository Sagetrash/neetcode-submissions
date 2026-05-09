class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        j = len(nums)-1
        for i in range(len(nums)-2):
            k = i+1
            j = len(nums)-1
            while k<j:
                sum = nums[i] + nums[k]+nums[j]
                if sum == 0:
                    res.add((nums[i],nums[k],nums[j]))
                    k += 1
                if sum < 0:
                    k+=1
                    continue
                if sum > 0:
                    j -= 1
                    continue
        return list(res)
