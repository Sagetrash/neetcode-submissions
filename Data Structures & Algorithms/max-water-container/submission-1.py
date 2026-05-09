class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxi = 0
        while i < j:
            vol = (j-i) * min(heights[i],heights[j])
            if vol > maxi:
                maxi=vol
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return maxi