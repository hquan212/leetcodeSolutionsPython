#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## two pointer method, have a slow pointer that will change the array in place as we move the j pointer
        # forward. 
        if not nums: return 0 

        i = 0 
        for j in range(len(nums)):
            if nums[i] == nums[j] : j +=1 
            else:
                nums[i+1] = nums[j]
                i +=1 
        return i+1
# @lc code=end

