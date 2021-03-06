
class Heap:


    def __init__(self):
        self.heap = list()
        self.size = 0

    def print(self):
        print(self.size)
        print(self.heap)


    def getLCI(self, index):
        return index * 2 + 1

    def getRCI(self, index):
        return index * 2 + 2

    def getPI(self, index):
        return (index - 1) // 2

    def hasLC(self, index):
        return self.getLCI(index) < self.size

    def hasRC(self, index):
        return self.getRCI(index) < self.size

    def hasP(self, index):
        return self.getPI(index) >= 0

    def getLC(self, index):
        return self.heap[self.getLCI(index)]

    def getRC(self, index):
        return self.heap[self.getRCI(index)]

    def getP(self, index):
        return self.heap[self.getPI(index)]

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def peek(self):
        return self.heap[0]

    def add(self, node):
        if self.size == len(self.heap):
            self.heap.append(node)
        else:
            self.heap[self.size] = node
        self.size += 1
        self.heapifyUp()

    def poll(self):
        curr = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        if self.size > 1:
            self.heapifyDown()
        return curr


class MinHeap(Heap):

    def heapifyUp(self):

        node_index = self.size - 1
        node = self.heap[node_index]

        while self.hasP(node_index) and self.getP(node_index) > node:
            self.swap(node_index, self.getPI(node_index))
            node_index = self.getPI(node_index)

    def heapifyDown(self):
        index = 0

        while (self.hasLC(index)):
            smallerCI = self.getLCI(index)
            if self.hasRC(index) and self.getRC(index) < self.getLC(index):
                smallerCI = self.getRCI(index)
            if self.heap[smallerCI] > self.heap[index]:
                return
            else:
                self.swap(index, smallerCI)
            index = smallerCI


class MaxHeap(Heap):

    def heapifyUp(self):

        node_index = self.size - 1
        node = self.heap[node_index]

        while self.hasP(node_index) and self.getP(node_index) < node:
            self.swap(node_index, self.getPI(node_index))
            node_index = self.getPI(node_index)

    def heapifyDown(self):
        index = 0

        while (self.hasLC(index)):
            biggerCI = self.getLCI(index)
            if self.hasRC(index) and self.getRC(index) > self.getLC(index):
                biggerCI = self.getRCI(index)
            if self.heap[biggerCI] < self.heap[index]:
                return
            else:
                self.swap(index, biggerCI)
            index = biggerCI

