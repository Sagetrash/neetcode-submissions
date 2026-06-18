class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        res = [0]*len(temperatures)
        for i,v in enumerate(temperatures):
            print(days)
            print(res)
            if not days:
                days.append((i,v))
                continue
            if v <= days[-1][1]:
                days.append((i,v))
            else:
                curr = days.pop()
                res[curr[0]] = i - curr[0]
                days.append((i,v))
        print(days)
        print(res)
        last = days.pop()
        while days:
            curr = days.pop()
            if last[1] > curr[1]:
                res[curr[0]] = last[0] - curr[0]
            else:
                last = curr
        return res