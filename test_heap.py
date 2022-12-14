from unittest import TestCase

from heap import MaxHeap


class TestMaxHeap(TestCase):
    def test_up_heap(self):
        self.fail()

    def test_find_max_child_for_2(self):
        heapTrinary = MaxHeap(nodesAmount=2, heapListOfNodes=[8,7,6,4,2,9])

        max_child_idx = heapTrinary.findMaxChild(0)

        self.assertEquals(heapTrinary.get_value(max_child_idx), 9)
    def test_find_max_child_for_3(self):
        heapTrinary = MaxHeap(nodesAmount=3, heapListOfNodes=[8, 5,7,6, 1,1,1, 4,9,2, 1,5,1])

        max_child_idx = heapTrinary.findMaxChild(0)

        self.assertEquals(heapTrinary.get_value(max_child_idx), 9)

    def test_down_heap(self):
        self.fail()

    def test_add_to_heap(self):
        self.fail()

    def test_pop(self):
        self.fail()
