#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        linked = {} #this dict saves the differences between the target and the actual values with index.
        for i in range(len(nums)):
            if nums[i] in linked:
                return [linked[nums[i]], i]
            else:
                linked[target - nums[i]] = i
        
# @lc code=end

