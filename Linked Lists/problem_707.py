class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):        
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        current = self.left.next

        while current and index > 0:
            current = current.next
            index -= 1

        if current and current != self.right and index == 0:
            return current.val
        
        return -1
        
    def addAtHead(self, val):
        node, next, prev = ListNode(val), self.left.next, self.left
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev
        
    def addAtTail(self, val):
        node, next, prev = ListNode(val), self.right, self.right.prev
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev
        
    def addAtIndex(self, index, val):
        current = self.left.next

        while current and index > 0:
            current = current.next
            index -= 1

        if current and index == 0:
            node, next, prev = ListNode(val), current, current.prev
            next.prev = node
            prev.next = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index):
        current = self.left.next

        while current and index > 0:
            current = current.next
            index -= 1

        if current and current != self.right and index == 0:
            next, prev = current.next, current.prev
            next.prev = prev
            prev.next = next
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)