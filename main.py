from heap import MaxHeap


heapBinary = MaxHeap(2)
heapBinary.add(2)
heapBinary.add(3)
heapBinary.add(9)
heapBinary.add(4)
heapBinary.add(1)
heapBinary.add(8) #problem tu
heapBinary.add(7) #problem tu
heapBinary.add(15)
heapBinary.add(20)
heapBinary.add(41)
heapBinary.add(32)
heapBinary.add(5)
#print_k_ary_heap(heapBinary.heapListOfNodes, 3)
print(heapBinary.top())
print(heapBinary.pop())
print(heapBinary.top())