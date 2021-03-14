#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def checkTooLarge(self, x):
        # Check within 32 bit boundaries
        if -2**31 <= x <= (2**31-1):
            return False 
        return True

    def reverse(self, x: int) -> int:
        if x == 0 : return 0
        isNegative = [1,-1][x<0]  # Choose sign if x < 0
        res = isNegative * int(str(abs(x))[::-1])  # int casting auto removes leading 0s
        return 0 if self.checkTooLarge(res) else res
# @lc code=end

