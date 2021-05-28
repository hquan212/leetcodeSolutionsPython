#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = [] 
        self.helper(res, '', 0, 0, n)
        return res 

    
    def helper(self, list, string,open, close, n): 
        
        if len(string) == n*2: 
            list.append(string)
            return 
        
        if open < n: self.helper(list, string +'(', open+1, close, n)
        if close < open: self.helper(list, string +')', open, close+1, n)

# @lc code=end

