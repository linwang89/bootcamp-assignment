# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = 0
        val2 = 0
        digit = 1
        while l1:
            val1 = val1 + l1.val * digit
            l1 = l1.next
            digit *= 10
        digit = 1
        while l2:
            val2 = val2 + l2.val * digit
            l2 = l2.next
            digit *= 10
        val3 = val1 + val2
        if val3 == 0:
            return ListNode(0)
        dummy = ListNode(0)
        cur = dummy
        digit = 10
        while val3:
            cur.next = ListNode((val3 % digit) / (digit / 10))
            cur = cur.next
            val3 = val3 - val3 % digit
            digit *= 10
        return dummy.next

