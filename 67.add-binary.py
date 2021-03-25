#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bina, binb = int(a,2), int(b,2) 
        while (binb): 
            xord = bina^binb 
            carry = (bina&binb) << 1 
            bina, binb = xord, carry 
        return bin(bina)[2:]

# @lc code=end

