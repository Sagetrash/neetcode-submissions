class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            for j in range(i+1,len(nums)):
                if val == nums[j]:
                    return [i,j]
            