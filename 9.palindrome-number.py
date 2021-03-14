#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert to string solution: O(n) space, O(n) time
        # if x == "": return True
        # if x < 0: return False

        # charX = str(x)
        # l, r = 0, len(charX)-1
        # while l <= r:
        #     if charX[l] != charX[r]:
        #         return False
        #     l += 1
        #     r -= 1 
        # return True


        # ============================= 
        # Non solution O(1) space, O(n) time
        if x < 0:
            return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10  # This one command reverses a positive integer!
            p //= 10 # Must do an integer division to avoid inf loop of floats
        return res == x

# @lc code=end

