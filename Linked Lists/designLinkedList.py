class MyLinkedList:

    class Node:
        def __init__(self, val=0):
            self.val = val
            self.next = None


    def __init__(self):
        self.head = self.Node()
        self.last = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        for _ in range(index):
            if not curr: return -1
            curr = curr.next
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        second = self.head.next
        new = self.Node(val)
        new.next = second
        self.head.next = new
        if self.last == self.head:
            self.last = new


    def addAtTail(self, val: int) -> None:
        new = self.Node(val)
        self.last.next = new
        self.last = new

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        for _ in range(index):
            if not curr: return
            curr = curr.next
        if not curr:
            return self.addAtTail(val)
        new = self.Node(val)
        next = curr.next
        curr.next = new
        if next:
            new.next = next
        else:
            self.last = new

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        for _ in range(index):
            if not curr: return
            curr = curr.next
        if not curr: return
        remove = curr.next
        if not remove: return
        if remove.next:
            curr.next = remove.next
        else:
            curr.next = None
            self.last = curr


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)