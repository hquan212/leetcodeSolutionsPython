#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # we could use binary search, if found return index, if not, find index 
        # get l and r, calculdate middle (r- l) // 2 
        # compare target with nums[middle] 
        # while l <= r
        # if  target is larger, l = middle re do bnsear 
        # if target is smaller, r = middle re do bnsear 
        # if target == nums[middle] return middle 
        # not found 
        # if target > nums: middle return middle + 1 else middle 
        # O(log(N)) time complexity

        # l, r  = 0, len(nums) -1 
        # while l <= r:
        #     middle = (r + l) // 2 
        #     if target == nums[middle]:
        #         return middle
        #     elif target > nums[middle]: 
        #         l = middle + 1
        #     else: 
        #         r = middle -1
        # return l

        # allow duplicates in array:
        l, r = 0, len(nums) -1 
        while l<= r:
            m = (l+r) // 2 
            if nums[m] < target:
                l = m + 1 
            else: 
                if nums[m] == target and nums[m-1] < target:
                    return m 
                else: 
                    r = m -1 
        return l


# @lc code=end

