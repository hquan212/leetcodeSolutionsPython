#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # create two pointers, one slow and one fast.
        # start i at 0 and j from 0 onward (faster pointer).
        # if nums[j] != val, copy it down to i and increase i
        # O(n) time, O(1) space

        # i = 0 
        # for j in range(len(nums)):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1 
        
        # return i

        # O(n) time, O(1) space V2 
        i = 0
        n = len(nums) 
        while i < n:
            if nums[i] == val: 
                nums[i] = nums[n-1]
                n -= 1
            else: i+=1
        return n


# @lc code=end

