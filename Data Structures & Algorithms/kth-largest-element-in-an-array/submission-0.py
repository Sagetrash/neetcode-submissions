import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in nums:
            hq.heappush(pq,-i)
        for i in range(k-1):
            hq.heappop(pq)
        return -(hq.heappop(pq))