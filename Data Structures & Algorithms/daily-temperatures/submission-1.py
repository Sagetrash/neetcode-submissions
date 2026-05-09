class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        res = [0]*len(temperatures)
        for i,v in enumerate(temperatures):
            while days and v > days[-1][1]:
                curr = days.pop()
                res[curr[0]] = i - curr[0]
            days.append((i,v))
        return res