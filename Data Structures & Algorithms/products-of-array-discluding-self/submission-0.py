class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            prod = 1
            for j in nums:
                if i == j:
                    continue
                prod = prod*j
            res.append(prod)
        return res