#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # THERE ARE SECRETS TO THIS LOOK BELOW! XOR them before 
        x, y = int(a, 2), int(b, 2) # Convert from string to bin.
        while y: 
            answer = x^y # this is the sum without carry 
            carry = (x&y) << 1 # carry is just and left shifted
            x,y = answer, carry
        return bin(x)[2:]

# @lc code=end

