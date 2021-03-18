#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "" or s == " ": return 0 

        count = 0 
        for char in reversed(s):
            if char.isspace(): 
                if count: break 
            else: 
                count += 1 
        return count

# @lc code=end

