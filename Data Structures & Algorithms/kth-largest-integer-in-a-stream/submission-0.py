import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = nums
        hq.heapify(self.pq)
        while len(self.pq) > k:
            hq.heappop(self.pq)

    def add(self, val: int) -> int:
        hq.heappush(self.pq,val)
        while len(self.pq) > self.k:
            hq.heappop(self.pq)
        return self.pq[0]