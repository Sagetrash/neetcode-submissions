class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(0,len(nums)):
            y = target - nums[i]
            if y in hmap:
                return [hmap[y],i]
            else:
                hmap[nums[i]] = i

