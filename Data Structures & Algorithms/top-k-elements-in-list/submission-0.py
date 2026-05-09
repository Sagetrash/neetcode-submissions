class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {}
        for i in nums:
            if i not in fmap:
                fmap[i] = 1
            else:
                fmap[i] += 1
        srtd_map = dict(sorted(fmap.items(), key = lambda item: item[1],reverse = True))
        return list(srtd_map.keys())[:k]