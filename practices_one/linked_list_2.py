class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while i <= index:
            if i == index:
                return curr.val ###check here
            else:
                if curr.next is None or curr is None:
                    return -1
                else:
                    i += 1
                    curr = curr.next

    def addAtHead(self, val: int) -> None:
        self.head = self.node(val, self.head)

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = self.node(val,None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = self.node(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            prev = self.head
            curr = self.head.next
            i = 0
            while i < index:
                if i == index-1:
                    prev.next = self.node(val, curr)
                    return
                prev = curr
                curr = curr.next
                i += 1

    def deleteAtIndex(self, index: int) -> None:
        prev = None
        curr = self.head
        n = self.head.next

        if index == 0 and n == None:
            self.head = None
        elif index == 0:
            self.head = self.head.next
        else:
            i = 0
            while i <= index and curr.next:
                if i == index:
                    prev.next = n
                    return
                else:
                    i += 1
                    prev = curr
                    curr = n
                    n = n.next

    class node:
        def __init__(self, val, n):
            self.val = val
            self.next = n

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
