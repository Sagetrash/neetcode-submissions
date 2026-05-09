class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        res = ''
        store = self.timemap.get(key,[])
        l = 0
        r = len(store)-1
        while l <= r:
            mid = (l+r)//2
            if store[mid][0] <= timestamp:
                res = store[mid][1]
                l = mid + 1
            else:
                r = mid -1
        return res

