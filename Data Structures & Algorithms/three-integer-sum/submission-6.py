class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(0,len(nums)-1):
            k = i+1
            j = len(nums)-1
            while k < j:
                print(i,k,j)
                sum = nums[i]+nums[j]+nums[k]
                print(sum)
                if sum == 0:
                    res.add((nums[i],nums[k],nums[j]))
                    k += 1
                    continue
                if sum < 0:
                    k += 1
                    continue
                if sum > 0:
                    j -= 1
                    continue
        return list(res)
