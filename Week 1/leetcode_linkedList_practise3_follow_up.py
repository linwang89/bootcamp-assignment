# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        f = head
        s = head
        while True:
            try:
                f = f.next
                f = f.next
                s = s.next
                if f is s:
                    s = head
                    while f is not s:
                        s = s.next
                        f = f.next
                    return f
            except:
                return None

