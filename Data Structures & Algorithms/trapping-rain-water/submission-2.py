class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0,len(height)-1
        res = 0
        leftmax,rightmax = height[i],height[j]
        while i < j:
            if height[i] < height[j]:
                i += 1
                leftmax = max(leftmax,height[i])
                res += leftmax - height[i]
            else:
                j -= 1
                rightmax = max(leftmax,height[j])
                res += rightmax-height[j]
        return res