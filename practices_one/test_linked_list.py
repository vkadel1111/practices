import unittest
from unittest import TestCase
import linked_list

class TestMyLinkedList(TestCase):

    def test_addAtHead(self):
        n_list = linked_list.MyLinkedList()
        n_list.addAtHead(1)
        n_list.addAtHead(2)
        assert n_list.head.val == 2

    def test_get(self):
        n_list = linked_list.MyLinkedList()
        n_list.addAtHead(1)
        n_list.addAtHead(2)
        n_list.addAtHead(3)
        n_list.addAtHead(4)
        assert n_list.get(2) == 2

    def test_addAtTail(self):
        ll = linked_list.MyLinkedList()
        layers = 11
        self.create_list(ll,11)
        ll = ll.head
        for i in range(layers-1):
            ll = ll.next
        assert ll.val == layers

    def test_addAtTail_no_recur(self):
        ll = linked_list.MyLinkedList()
        layers = 10
        for i in range(layers):
            ll.add_tail_no_recur(i)
        temp = ll.head
        for i in range(layers-1):
            temp = temp.next
        assert temp.val == layers -1

    def create_list(self, n_list,layers = 10):
        for i in range(1, layers + 1):
            n_list.addAtTail(i)

    def test_add_at_index(self):
        ll = linked_list.MyLinkedList()
        ll.addAtIndex(0,1)
        ll.addAtTail(2)
        ll.addAtHead(0)
        ll.addAtHead(5)
        index = 3
        val = 3
        ll.addAtIndex(index,val)
        assert ll.get(index) == val


    def test_add_at_index_wo(self):
        ll = linked_list.MyLinkedList()
        ll.addAtIndex(0,1)
        ll.addAtTail(2)
        ll.addAtHead(0)
        ll.addAtHead(5)
        index = 3
        val = 3
        ll.addAtIndex_wo_rec(index,val)
        assert ll.get(index) == val

    def test_delete_at_index(self):
        ll = linked_list.MyLinkedList()
        self.create_list(ll)
        ## Insert deletions
        ll.deleteAtIndex(2)
        assert ll.get(2) == 4

    def test_delete_at_index_no_recur_front(self):
        ll = linked_list.MyLinkedList()
        self.create_list(ll)
        ## Insert deletions
        ll.delete_at_index_no_recur(0)
        assert ll.get(0) == 2

    def test_delete_at_index_no_recur_middle(self):
        ll = linked_list.MyLinkedList()
        self.create_list(ll)
        ## Insert deletions
        ll.deleteAtIndex(2)
        assert ll.get(2) == 4

    def test_delete_at_index_no_recur_tail(self):
        ll = linked_list.MyLinkedList()
        self.create_list(ll)
        ## Insert deletions
        ll.delete_at_index_no_recur(9)
        assert ll.get(9) == 9

    # def test_get_index(self):
    #
    #     self.assertEqual()
    #     param_1 = obj.get(index)
#
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
if __name__ == '__main__':
    unittest.main()