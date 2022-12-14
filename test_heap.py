from unittest import TestCase

from heap import MaxHeap


class TestMaxHeap(TestCase):


    def test_find_max_child_for_3(self):
        heapTrinary = MaxHeap(nodesAmount=3, heapListOfNodes=[1, 7,5,4, 3,2,0, 1,0,2, 3])

        max_child_idx = heapTrinary.findMaxChild(0)

        self.assertEquals(max_child_idx, 1)
        self.assertEquals(heapTrinary.get_value(max_child_idx), 7)


    def test_down_heap_3(self):

        heapTrinary = MaxHeap(nodesAmount=3, heapListOfNodes=[1, 5,7,4, 3,4,0, 0,6,2, 2])

        heapTrinary.downHeap(0)

        self.assertEquals(heapTrinary.get_nodes(), [7, 5,6,4, 3,4,0, 0,1,2, 2])

    def test_down_heap_four(self):

        heapTrinary = MaxHeap(nodesAmount=4, heapListOfNodes=[1, 5,10,4,9, 3,3,3,3, 4,5,6,0, 2,2,2,2])

        heapTrinary.downHeap(0)

        self.assertEquals(heapTrinary.get_nodes(), [10, 5,6,4,9, 3,3,3,3, 4,5,1,0,  2,2,2,2])



    def test_pop_3(self):
        heapTrinary = MaxHeap(nodesAmount=4, heapListOfNodes=[9,  5, 7, 2,3,  0,0,0,0,  3,4,0,1,  2,2,3,1])

        popped = heapTrinary.pop()

        self.assertEquals(popped,9)
        self.assertEquals(heapTrinary.get_nodes(),[7,  5,4,2,3, 0,0,0,0,  3,1,0,1, 2,2,3])

    def test_add_4(self):
        heapTrinary = MaxHeap(nodesAmount=4)

        heapTrinary.addToHeap(5)
        heapTrinary.addToHeap(7)
        heapTrinary.addToHeap(1)
        heapTrinary.addToHeap(9)
        heapTrinary.addToHeap(2)
        heapTrinary.addToHeap(4)
        heapTrinary.addToHeap(3)
        heapTrinary.addToHeap(0)
        heapTrinary.addToHeap(11)

        self.assertEquals(heapTrinary.get_nodes(),[11,  9,1,7,2, 4,3,0,5])