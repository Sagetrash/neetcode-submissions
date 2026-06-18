class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicc = {}
        for i,n in enumerate(nums):
            dicc[n] = i
        print(dicc)
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dicc:
                return [i,dicc[comp]]