#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # take care of base case and O((N-L)L) time, O(1) space
        # N is len haystack, L is len needle
        # could add extra check if needle length is larger than haystack length
        # lets use a sliding window on string problem 
        # if needle == "" : return 0 

        # lenNeedle = len(needle)
        # i = 0 
        # while i + lenNeedle < len(haystack)+1:
        #     #slide through the haystack looking for first 
        #     # occurance of needle 
        #     if ( haystack[i:(i+lenNeedle)] == needle):
        #         return i
        #     else: 
        #         i +=1 
        # return -1 


        #===================
        def kmp(str_):
            b, prefix = 0, [0]
            for i in range(1, len(str_)):
                while b > 0 and str_[i] != str_[b]:
                    b = prefix[b - 1]
                if str_[b] == str_[i]:
                    b += 1
                else:
                    b = 0
                prefix.append(b)
            return prefix

        str_ = kmp(needle + '#' + haystack)
        n = len(needle)
        if n == 0:
            return n
        for i in range(n + 1, len(str_)):
            if str_[i] == n:
                return i - 2 * n
        return -1


# @lc code=end

