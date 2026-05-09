class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[]for _ in range(len(nums)+1)]
        fmap = {}
        res = []
        for i in nums:
            fmap[i] = fmap.get(i,0) + 1
        for i in fmap.items():
            freq[i[1]].append(i[0])
        
        for f in range(len(freq)-1,0,-1):
            for i in freq[f]:
                res.append(i)
                if len(res) == k:
                    return res