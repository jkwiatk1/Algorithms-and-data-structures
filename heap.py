'''
Kopiec w ktorym korzen jest wiekszy od dzieci
'''

class MaxHeap:
    def __init__(self, nodesAmount = 2):
        self.heapListOfNodes = []
        self.nodesAmount = nodesAmount
        self.heapSize = 0

    def __init__(self, nodesAmount = 2,heapListOfNodes = []):
        self.heapListOfNodes = heapListOfNodes
        self.nodesAmount = nodesAmount
        self.heapSize = len(self.heapListOfNodes)

    def parent(self, index):
        '''
        Zwraca index parenta

        :param index indeks dziecka w liście [0...nodes_amount]
        :return: indeks parenta [0...nodes_amount]
        '''
        return (index-1)//self.nodesAmount
    def get_nodes(self):
        return self.heapListOfNodes

    def get_value(self,idx):
        return self.heapListOfNodes[idx]

    def child(self, index, child_of_parent_idx):
        '''
        Zwraca index w tablicy dziecka parenta o indeksie index [0...nodes_amount].
        :param index indeks parenta w tablicy [0...nodes_amount]
        :param child_of_parent_idx ideks dziecka w drzewie [1...(nodes_amount -1)]
        :return: indeks dziecka w liście
        '''
        return (self.nodesAmount * index + child_of_parent_idx)

    def upHeap(self, index):
        while (index != 0 and (self.heapListOfNodes[self.parent(index)]) < self.heapListOfNodes[index]):
            (self.heapListOfNodes[index], self.heapListOfNodes[self.parent(index)]) = (self.heapListOfNodes[self.parent(index)], self.heapListOfNodes[index] )
            index = self.parent(index)


    def findMaxChild(self, index):
        maxChild = self.heapListOfNodes[index]
        maxChildIndex = -1
        idx_child_of_parent = 1
        while self.child(index, idx_child_of_parent) < self.heapSize:
            if self.heapListOfNodes[self.child(index, idx_child_of_parent)] > maxChild:
                maxChild = self.heapListOfNodes[self.child(index, idx_child_of_parent)]
                maxChildIndex = self.child(index, idx_child_of_parent)
            if idx_child_of_parent >= self.nodesAmount:
                break
            idx_child_of_parent += 1
        return maxChildIndex

    def downHeap(self, parent_index):

        while (parent_index * self.nodesAmount) <= self.heapSize:
            childIndex = self.findMaxChild(parent_index)
            if childIndex == -1:
                break
            if self.heapListOfNodes[parent_index] < self.heapListOfNodes[childIndex]:
                # swap
                temp = self.heapListOfNodes[parent_index]
                self.heapListOfNodes[parent_index] = self.heapListOfNodes[childIndex]
                self.heapListOfNodes[childIndex] = temp
            parent_index = childIndex



    def add(self, data):
        self.heapListOfNodes.append(data)
        self.heapSize += 1
        self.upHeap(self.heapSize -1)

    def top(self):
        return self.heapListOfNodes[0]

    def pop(self):
        '''
        Usuwa i zwraca korzeń kopca.
        Nastepnie równowazy kopiec downheap.
        :return: korzeń kopca
        '''

        root = self.heapListOfNodes[0]
        self.heapListOfNodes[0] = self.heapListOfNodes[self.heapSize -1]
        self.heapSize -= 1
        self.downHeap(0)

        return root

