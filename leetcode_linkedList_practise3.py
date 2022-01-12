#Two Pointer Technique - Linked List Cycle II
#https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
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
        stackF = [f]
        stackS = [s]
        while True:
            try:
                f = f.next
                stackF.append(f)
                f = f.next
                stackF.append(f)
                s = s.next
                stackS.append(s)
                if f is s:
                    while stackS:
                        print
                        len(stackS)
                        f = stackF.pop()
                        s = stackS.pop()
                        if f is s:
                            res = s
                        else:
                            return res
                    return s
            except:
                return None
