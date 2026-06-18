class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key][timestamp] = value
    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.timemap[key].keys():
            return self.timemap[key][timestamp]
        else:
            try:
                return self.timemap[key][sorted(list(self.timemap[key].keys()))[-1]]
            except Exception as e:
                return None