class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                curr = stack.pop()
                res[curr[0]] = i-curr[0]
            stack.append((i,v))
        return res