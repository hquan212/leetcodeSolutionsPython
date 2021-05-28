#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        sizeLL = 0 
        tmp = head
        while tmp: 
            sizeLL += 1 
            tmp = tmp.next 
        endK = sizeLL - k 

        first = head 
        for _ in range(k-1):
            first = first.next 
        
        second = head 
        for _ in range(endK):
            second = second.next
        
        first.val, second.val = second.val, first.val 

        return head 

# @lc code=end

