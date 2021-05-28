#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# backtracking recursino problem 

# create helper function 
# send in output array, 
# for loop through each value and create a tree of other values 

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 
        self.backtracking(res, [], nums )
        return res
    
    def backtracking(self, res, tempList, nums):
        if len(tempList) == len(nums):
            return res.append(tempList[:])
    
        else: 
            for i, val in enumerate(nums):
                if val in tempList: continue 
                tempList.append(val)
                self.backtracking(res, tempList, nums)
                tempList.pop()
# @lc code=end

