class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        nav = self.head
        depth = 0
        if index == 0:
            return self.head.val
        else:
            while nav.next != None and depth < index:
                nav = nav.next
                depth += 1
        return nav.val

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            # Easy path just initialize
            self.head = self.node(val, None)
        else:
            # need to move the head
            n_h = self.node(val, self.head)
            self.head = n_h
        print("")

    def addAtTail(self, val: int) -> None:
        # Create node
        if self.head == None:
            self.head = self.node(val, None)
        elif self.head.next == None:
            self.head.next = self.node(val, None)
        else:
            self.goDeeper(self.head, val)

    def goDeeper(self, ll: object, val) -> None:
        if ll.next == None:
            ll.next = self.node(val, None)
            return
        else:
            self.goDeeper(ll.next, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0 and self.head == None:
            self.head = self.node(val, None)
        else:
            self.go_add_at_index(index, val, self.head, self.head.next)

    def go_add_at_index(self, index: int, val: int, prev: object, next: object, lvl=0) -> None:
        if lvl > index:
            return
        elif index-1 == lvl:
            prev.next = self.node(val, next)
            return
        else:
            self.go_add_at_index(index, val, prev.next, next.next, lvl + 1)

    def addAtIndex_wo_rec(self, index: int, val: int) -> None:
        if index==0 and self.head == None:
            self.head = self.node(val,None)
        elif index>0:
            lvl = 0
            curr = self.head
            next = curr.next
            while lvl < index-1:
                if curr.next==None:
                    #reached end of list return
                    return
                curr = curr.next
                next = next.next
                lvl +=1
            curr.next = self.node(val,next)



    def deleteAtIndex(self, index: int) -> None:
        self.go_delete_at_index(index, None, self.head, self.head.next)

    def go_delete_at_index(self, i: int, prev_prev: object, prev: object, next: object, lvl=0):
        if i == 0 and prev.next == None:
            # single root node
            self.head = None
            return
        elif i == 0 and prev.next != None:
            # head is getting replaced
            self.head = self.head.next
            return
        elif i > 0 and i == lvl and next != None and prev_prev != None:
            # Front and tail exist
            prev_prev.next = next
            return
        elif i > 0 and i == lvl and next == None and prev_prev != None:
            # Deleting the tail
            prev.next = None
            return
        else:
            self.go_delete_at_index(i,prev,prev.next,next.next, lvl+1)

    def add_tail_no_recur(self, val: int):
        new = self.node(val, None)
        temp = self.head
        if self.head == None:
            self.head = new
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = new


    def delete_at_index_no_recur(self,index:int):
        prev = None
        curr = self.head
        after = self.head.next
        if self.head != None:
            lvl = 0
            while index >= lvl and curr != None:
                if lvl == index:
                    if prev == None:
                        # delete the head
                        self.head = after
                        return
                    elif prev != None:
                        ## cut the link
                        prev.next = after
                        return
                else:
                    prev = curr
                    curr = curr.next
                    after = curr.next
                    lvl +=1

    class node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
