class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # booyer moore voting algorithm
        cand = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == cand:
                count += 1
            else:
                count -= 1
        
        if count > 0:
            return cand
        else:
            for i in set(nums):
                if i != cand:
                    return i