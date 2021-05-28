#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if b < a : return 
        cur = list1

        for _ in range(a-1):
            cur = cur.next 
        cura = cur 

        cur = list1
        for _ in range(b+1): 
            cur = cur.next 

        end2 = list2
        while end2.next: 
            end2 = end2.next
        
        cura.next = list2
        end2.next = cur 
        return list1


# @lc code=end

