#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = head = ListNode(0)
        carry = 0 
        while l1 or l2 or carry: 
            if l1: 
                carry += l1.val
                l1 = l1.next 
            if l2: 
                carry += l2.val 
                l2 = l2.next 
            temp = ListNode(carry%10)
            result.next = temp 
            result= result.next 
            carry //= 10 
        return head.next


# @lc code=end

