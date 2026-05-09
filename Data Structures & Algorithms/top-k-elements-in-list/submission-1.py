class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {}
        for i in nums:
            if i not in fmap:
                fmap[i] = 1
            else:
                fmap[i] += 1
        freq = [[]for i in range(len(nums)+1)]
        for n,f in fmap.items():
            freq[f].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res