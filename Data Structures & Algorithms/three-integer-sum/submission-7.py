class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(0,len(nums)-2):
            k = i+1
            j = len(nums)-1
            while(k<j):
                sum = nums[i]+nums[j]+nums[k]
                if sum == 0:
                    res.add((nums[i],nums[j],nums[k]))
                    j -= 1
                    k += 1
                else:
                    if sum <0:
                        k += 1
                    else:
                        j -= 1
        return list(res)
                