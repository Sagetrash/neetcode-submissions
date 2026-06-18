class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        i = 0
        j = len(nums)-1
        k = (i+j)//2
        res = set()
        while i < j and k <= j and i <= k:
            print([i,k,j])
            sum = nums[i] + nums[k] + nums[j]
            print(sum)
            if sum == 0:
                print(i," ",k," ",j)
                res.add((nums[i],nums[k],nums[j]))
                k += 1
            elif sum > 0:
                j -= 1
                if k == j:
                    j = len(nums) - 1
                    k -= 1
            elif sum < 0:
                i += 1
                if k == i:
                    i = 0
                    k += 1
        return list(res)

            
