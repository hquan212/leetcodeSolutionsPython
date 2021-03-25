#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    # Memoization solution similar to fibonacci.
    # can only take one or two steps at a time.
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n in self.memo: 
            return self.memo[n]
        elif n < 0: return 0
        elif n <= 1 : 
            return 1 
        else:
            val = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.memo[n] = val 
            return val 
# @lc code=end

