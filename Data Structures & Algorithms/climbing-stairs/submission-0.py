class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 0: return 1
        memo = [-1] * (n+1)
        memo[0] = 1
        memo[1] = 1
        def helper(k):
            if memo[k] != -1:
                return memo[k]
            memo[k] = helper(k-1) + helper(k-2)
            return memo[k]

        return helper(n)
