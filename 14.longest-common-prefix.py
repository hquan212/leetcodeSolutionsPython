#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        shortestWord = min(strs, key=len)  # use the min function sorted by len
        for i, ch in enumerate(shortestWord):
            for other in strs:
                if other[i] != ch:
                    return shortestWord[:i]
        return shortestWord


# @lc code=end

