#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # recursive solution
        # if (l1 == None): return l2 
        # elif (l2 == None): return l1 
        # elif (l1.val <= l2.val): 
        #     l1.next = self.mergeTwoLists(l1.next, l2) 
        #     return l1 
        # else: 
        #     l2.next = self.mergeTwoLists(l1, l2.next) 
        #     return l2

        # =================== 
        # iterative solution 
        dummy = head = ListNode(-1)
        while (l1 is not None and l2 is not None):
            if(l1.val < l2.val) :
                dummy.next = l1 
                l1 = l1.next
            else:
                dummy.next = l2 
                l2 = l2.next 
            dummy = dummy.next
        
        if l1 is not None:
            dummy.next = l1
        elif l2 is not None:
            dummy.next = l2
            
        return head.next
# @lc code=end

