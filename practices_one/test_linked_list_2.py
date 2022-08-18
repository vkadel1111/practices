import unittest
from unittest import TestCase
import linked_list_2

class TestMyLinkedList(TestCase):

# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]
# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[0],[0]]
    def test_addAtHead(self):
        n_list = linked_list_2.MyLinkedList()
        n_list.addAtHead(1)
        n_list.addAtTail(3)
        n_list.addAtIndex(1,2)
        r = n_list.get(1)
        n_list.deleteAtIndex(0)
        r_2 = n_list.get(0)
        assert r == 2 and r_2 ==3

# ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
# [[],[0,10],[0,20],[1,30],[0]]

    def test_2(self):
        n_list = linked_list_2.MyLinkedList()
        n_list.addAtIndex(0,10)
        n_list.addAtIndex(0,20)
        n_list.addAtIndex(1,30)
        r = n_list.get(0)
        assert r == 20

# ["MyLinkedList","addAtTail","get"]
# [[],[1],[0]]
    def test_2(self):
        n_list = linked_list_2.MyLinkedList()
        n_list.addAtTail(1)
        r = n_list.get(0)
        assert r == 20

    # ["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
    # [[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]
    def test_2(self):
        n_list = linked_list_2.MyLinkedList()
        n_list.addAtHead(4)
        r = n_list.get(4)
        assert r == -1

# ["MyLinkedList","addAtHead","addAtIndex","get","addAtHead","addAtTail","get","addAtTail","get","addAtHead","get","addAtHead"]
# [[],[5],[1,2],[1],[6],[2],[3],[1],[5],[2],[2],[6]]

    def test_3(self):
        n_list = linked_list_2.MyLinkedList()
        n_list.addAtHead(5)
        n_list.addAtIndex(1,2)
        n_list.get(1)
        n_list.addAtHead(6)
        n_list.addAtTail(2)
        r = n_list.get(4)
        assert r == -1

    def test_4(self):
        commands = ["MyLinkedList","addAtHead","addAtTail","addAtTail","get","get","addAtTail","addAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","get","addAtHead","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","get","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","get","deleteAtIndex","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtHead","addAtTail","get","addAtHead","get","addAtTail","get","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","get","addAtHead","addAtIndex","addAtTail","get","addAtIndex","get","addAtIndex","get","addAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","addAtIndex","get","addAtHead","addAtTail","addAtTail","addAtHead","get","addAtTail","addAtHead","addAtTail","get","addAtIndex"]
        inputs = [[],[84],[2],[39],[3],[1],[42],[1,80],[14],[1],[53],[98],[19],[12],[2],[16],[33],[4,17],[6,8],[37],[43],[11],[80],[31],[13,23],[17],[4],[10,0],[21],[73],[22],[24,37],[14],[97],[8],[6],[17],[50],[28],[76],[79],[18],[30],[5],[9],[83],[3],[40],[26],[20,90],[30],[40],[56],[15,23],[51],[21],[26],[83],[30],[12],[8],[4],[20],[45],[10],[56],[18],[33],[2],[70],[57],[31,24],[16,92],[40],[23],[26],[1],[92],[3,78],[42],[18],[39,9],[13],[33,17],[51],[18,95],[18,33],[80],[21],[7],[17,46],[33],[60],[26],[4],[9],[45],[38],[95],[78],[54],[42,86]]
        outputs   = ['null','null','null','null',-1,2,'null','null','null','null','null','null','null','null',84,'null','null','null','null','null','null','null','null','null','null','null',16,'null','null','null','null','null','null','null','null',37,'null','null','null','null','null',23,'null','null','null','null','null','null','null','null','null','null','null','null','null','null',19,'null',17,'null','null',56,'null','null',31,'null',17,'null',12,'null','null','null','null','null','null','null',40,'null','null','null',37,'null',76,'null',70,'null','null','null','null','null','null',80,'null','null','null','null',43,'null','null','null',83,'null']
        expecteds = ['null','null','null','null',-1,2,'null','null','null','null','null','null','null','null',84,'null','null','null','null','null','null','null','null','null','null','null',16,'null','null','null','null','null','null','null','null',37,'null','null','null','null','null',23,'null','null','null','null','null','null','null','null','null','null','null','null','null','null',19,'null',17,'null','null',56,'null','null',31,'null',17,'null',12,'null','null','null','null','null','null','null',40,'null','null','null',37,'null',76,'null',42,'null','null','null','null','null','null',80,'null','null','null','null',43,'null','null','null',40,'null']

        self.sequential_test(commands,inputs)

    def test_5(self):
        commands= ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
        inputs =[[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]
        outputs   = ['null','null','null','null',2,'null',3,-1,'null','null',3,'null',None]
        expecteds = ['null','null','null','null',2,'null',3,-1,'null','null',3,'null',-1]
        self.sequential_test(commands,inputs)

    def sequential_test(self,commands, inputs):
        i = 0
        for command, input in zip(commands, inputs):
            i += 1
            if i == 10:
                print()
            if command == "MyLinkedList":
                n_list = linked_list_2.MyLinkedList()
            elif command == "addAtHead":
                n_list.addAtHead(input[0])
            elif command == "addAtTail":
                n_list.addAtTail(input[0])
            elif command == "get":
                n_list.get(input[0])
            elif command == "addAtIndex":
                n_list.addAtIndex(input[0], input[1])
            elif command == 'deleteAtIndex':
                n_list.deleteAtIndex(input[0])
            else:
                print('Done')


if __name__ == '__main__':
    unittest.main()