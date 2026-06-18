class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key][timestamp] = value
    def get(self, key: str, timestamp: int) -> str:
        while timestamp not in self.timemap[key].keys():
            timestamp += -1
        return self.timemap[key][timestamp]