from _heapq import heappush
import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for i in stones:
            hq.heappush(pq,-i)
        while(len(pq)!=1):
            st1 = -(hq.heappop(pq))
            st2 = -(hq.heappop(pq))
            st1 = st1-st2
            hq.heappush(pq,-st1)
        return -hq.heappop(pq)
