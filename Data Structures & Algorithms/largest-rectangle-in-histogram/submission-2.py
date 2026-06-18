class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        MaxArea = 0
        for i,h in enumerate(heights):
            startIn = i
            while stack and stack[-1][1]>h:
                curr = stack.pop()
                MaxArea = max(MaxArea,(curr[0]-i)*h)
                start = curr[0]
            stack.append((startIn,h))
        for i,h in stack:
            MaxArea = max(MaxArea,(len(heights)-i)*h)
        return MaxArea