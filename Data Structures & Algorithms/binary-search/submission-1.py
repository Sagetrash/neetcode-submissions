class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        res = -1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                res = mid
                break
            if nums[mid] > target:
                j = mid -1
            else:
                i = mid + 1
        return res