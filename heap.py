'''
Kopiec w ktorym korzen jest wiekszy od dzieci
'''

class MaxHeap:
    def __init__(self, nodesAmount = 2):
        self.heapListOfNodes = []
        self.nodesAmount = nodesAmount
        self.heapSize = 0

    def parent(self, index):
        return (index-1)//self.nodesAmount

    def child(self, index, i):
        return (self.nodesAmount * index + i-1)

    def upHeap(self, index):
        while (index != 0 and (self.heapListOfNodes[self.parent(index)]) < self.heapListOfNodes[index]):
            (self.heapListOfNodes[index], self.heapListOfNodes[self.parent(index)]) = (self.heapListOfNodes[self.parent(index)], self.heapListOfNodes[index] )
            index = self.parent(index)


    def findMaxChild(self, index):
        maxChild = self.heapListOfNodes[index]
        maxChildIndex = -1
        i = 1
        while self.child(index, i) < self.heapSize:
            if self.heapListOfNodes[self.child(index, i)] > maxChild:
                maxChild = self.heapListOfNodes[self.child(index, i)]
                maxChildIndex = self.child(index, i)
            if i >= self.nodesAmount:
                break
            i += 1
        return maxChildIndex

    def downHeap(self, index):
        while (index * self.nodesAmount) <= self.heapSize:
            childIndex = self.findMaxChild(index)
            if childIndex == -1:
                break
            if self.heapListOfNodes[index] < self.heapListOfNodes[childIndex]:
                # swap
                temp = self.heapListOfNodes[index]
                self.heapListOfNodes[index] = self.heapListOfNodes[childIndex]
                self.heapListOfNodes[childIndex] = temp
            index = childIndex


    def addToHeap(self, data):
        self.heapListOfNodes.append(data)
        self.heapSize += 1
        self.upHeap(self.heapSize -1)

    def top(self):
        return self.heapListOfNodes[0]

    def pop(self):
        root = self.heapListOfNodes[0]
        self.heapListOfNodes[0] = self.heapListOfNodes[self.heapSize -1]
        self.heapListOfNodes.pop()
        self.downHeap(0)

        return root

def print_k_ary_heap(heap, k, depth=0):
    if not heap:
        return

    for i in range(len(heap), 0, -1):

        print(" " * i, heap[-i], end = )

    #
    # for i in range(1, k + 1):
    #     if i <= len(heap):
    #         print_k_ary_heap(heap[i:], k, depth + 1)

# Example usage


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
print_k_ary_heap(heapBinary.heapListOfNodes, 3)
print(heapBinary.top())
print(heapBinary.pop())
print(heapBinary.top())