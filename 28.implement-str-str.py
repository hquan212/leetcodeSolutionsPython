#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # take care of base case and
        # could add extra check if needle length is larger than haystack length
        # lets use a sliding window on string problem 
        if needle == "" : return 0 

        lenNeedle = len(needle)
        i = 0 
        while i + lenNeedle < len(haystack)+1:
            #slide through the haystack looking for first 
            # occurance of needle 
            if ( haystack[i:(i+lenNeedle)] == needle):
                return i
            else: 
                i +=1 
        return -1 


# @lc code=end

