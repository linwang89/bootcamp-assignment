#Design Linked List
#https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/

class Node:
    # constructor
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if not self.head:
            return -1
        if index == 0:
            return self.head.val
        x = self.head
        while index:
            try:
                x = x.next
            except:
                return -1
            index -= 1
        if x:
            return x.val
        else:
            return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head:
            x = Node(val)
            x.next = self.head
            self.head = x
        else:
            self.head = Node(val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = Node(val)
        else:
            b = self.head
            while self.head.next:
                self.head = self.head.next
            a = Node(val)
            self.head.next = a
            self.head = b

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
        elif self.head:
            a = self.head
            b = self.head.next
            flag = True
            while index - 1:
                try:
                    a = a.next
                    b = b.next
                except:
                    flag = False
                    break
                index -= 1
            if flag:
                x = Node(val)
                x.next = b
                a.next = x

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index == 0:
            self.head = self.head.next
        else:
            a = self.head
            b = self.head.next
            flag = True
            while index - 1:
                try:
                    a = a.next
                    b = b.next
                except:
                    flag = False
                    break
                index -= 1
            if flag:
                if b:
                    a.next = b.next
                else:
                    a.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)