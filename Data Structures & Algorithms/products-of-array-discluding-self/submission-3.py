class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        postfix = [0 for _ in range(n)]
        prefix[0] = postfix[-1] = 1
        for i in range(1,n):
            postfix[n-i-1] = postfix[n-i] * nums[n-i]
            prefix[i] = prefix[i-1] * nums[i-1]
        
        res = []
        for i in range(n):
            res.append(prefix[i]*postfix[i])
        return res