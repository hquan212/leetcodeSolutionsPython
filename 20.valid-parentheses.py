#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        valids = { ')' : '(',  ']' : '[' , '}': '{'}
        stack = []
        for ch in s:
            if ch in valids.values():
                stack.append(ch) # opening chars 
            elif ch in valids.keys():
                if stack == [] or valids[ch] != stack.pop():
                    return False
            else:
                return False 
        return stack == []


        
# @lc code=end

