import linked_list
def hasCycle(self, head: linked_list.MyLinkedList) -> bool:
    if head != None:
        slow = head
        fast = head
        if head.next == None:
            return False
        while slow != fast and slow.next != None:
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            return True
        else:
            return False