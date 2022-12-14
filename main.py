from heap import MaxHeap


heapBinary = MaxHeap(2)
heapBinary.addToHeap(2)
heapBinary.addToHeap(3)
heapBinary.addToHeap(9)
heapBinary.addToHeap(4)
heapBinary.addToHeap(1)
heapBinary.addToHeap(8) #problem tu
heapBinary.addToHeap(7) #problem tu
heapBinary.addToHeap(15)
heapBinary.addToHeap(20)
heapBinary.addToHeap(41)
heapBinary.addToHeap(32)
heapBinary.addToHeap(5)
#print_k_ary_heap(heapBinary.heapListOfNodes, 3)
print(heapBinary.top())
print(heapBinary.pop())
print(heapBinary.top())