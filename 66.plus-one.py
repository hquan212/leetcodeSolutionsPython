#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # the worst golphing lol
        # return [int(x) for x in str(int("".join(map(str,digits))) + 1)]

        # Ones compliment and reversed 
        for i in range(len(digits)):
            # if the ones complement digit is lower than 9, 
            # just add one and return
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            # else set this to zero and continue one more time in for loop 
            # until we get to a non 9 case .
            digits[~i] = 0 

        # BRILLIANT, if all are 9, 
        # create a new 0s len of digits plus leading one. 
        return [1] + [0] * len(digits)

# @lc code=end

