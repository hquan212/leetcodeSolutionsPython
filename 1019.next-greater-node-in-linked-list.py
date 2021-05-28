#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1   2    3
# 2 -> 1 -> 5
# [5,  5,  0]


# 2 -> 7 -> 4 -> 3 -> 5
# [7, 0, 5, 5, 0]

# 1 -> 7 -> 5 -> 1 -> 9 -> 2 -> 5 -> 1 
# [7, 9, 9, 9, 0, 5, 0, 0]

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head == None: return 
        node_vals = [] 

        cur = head 
        while cur: 
            node_vals.append(cur.val)
            cur = cur.next 
        
        answers = [0]*len(node_vals)
        stack = [] 

        for i, val in enumerate(node_vals): 
            while stack != [] and node_vals[stack[-1]] < val:
                answers[stack.pop()] = val
            stack.append(i)

        return answers
# @lc code=end

