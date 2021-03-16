#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Did not get this no time, use Greedy approach 
        # n = len(nums)
        # curr_sum = max_sum = nums[0]
        # for i in range(1, n):
        #     curr_sum = max(curr_sum + nums[i], nums[i])
        #     max_sum = max(max_sum, curr_sum)

        # return max_sum

        # =================== Divide and Conquer 
        def divideAndConquer(nums, i, j):
            if i == j-1:
                return nums[i],nums[i],nums[i],nums[i]
            
            i_mid = i + (j-i) // 2 
            a1, m1, b1, s1 = divideAndConquer(nums, i, i_mid)
            a2, m2, b2, s2 = divideAndConquer(nums, i_mid, j)

            a = max(a1, s1+a1)
            b = max(b2, s2+b1)
            m = max(m1,m2,b1+a2)
            s = s1+s2 
            return a,m,b,s 
        
        _, m ,_,_ = divideAndConquer(nums,0, len(nums))
        return m
# @lc code=end

