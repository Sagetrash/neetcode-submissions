class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        out = []
        while(l<=r):
            if(abs(nums[l])>abs(nums[r])):
                out.append(nums[l]**2)
                l += 1
            else:
                out.append(nums[r]**2)
                r -= 1
        print(out)
        return out[::-1]