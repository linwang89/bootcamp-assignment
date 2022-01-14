# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is headB:
            return headA
        x=headA
        y=headB
        flagA=0
        flagB=0
        while True:
            if x.next==None and flagA==0:
                x=headB
                flagA=1
            elif x.next:
                x=x.next
            else:
                return None
            if y.next==None and flagB==0:
                y=headA
                flagB=1
            elif y.next:
                y=y.next
            if x is y:
                return x
