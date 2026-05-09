class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {} 
        for i,val in enumerate(nums):
            if val not in unique.keys():
                unique[val] = i
            else:
                return True
        return False