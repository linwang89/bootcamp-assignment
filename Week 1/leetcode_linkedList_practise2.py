#Two Pointer Technique - Linked List Cycle
#https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fastpointer=head
        slowpointer=head
        while True:
            try:
                fastpointer=fastpointer.next
                fastpointer=fastpointer.next
                slowpointer=slowpointer.next
                if fastpointer is slowpointer:
                    return True
            except:
                return False