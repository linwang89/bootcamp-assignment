# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        stack = [head]
        while p.next:
            stack.append(p.next)
            p = p.next
        m = len(stack)
        if m == 1:
            return None
        if n == 1:
            stack[-2].next = None
        elif m == n:
            head = head.next
        else:
            stack[m - n - 1].next = stack[m - n + 1]
        return head
