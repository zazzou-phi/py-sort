from math import floor

class Heap:
    def __init__(self, array, min_max):
        self.data = array # set heap to the given data
        self.type = min_max # set type = 0 if min-heap or = 1 if max-heap
        self.heap_size = 0
        self.build_heap()

    def parent(self, i):
        return int(floor((i-1)/2))

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if self.type == 1:
            largest = i
            # check if left child is larger than i
            if l < self.heap_size and self.data[l] > self.data[i]:
                largest = l
            
            # check if right child is largest
            if r < self.heap_size and self.data[r] > self.data[largest]:
                largest = r

            # swap i with largest if i is not largest
            if largest != i:
                self.data[i], self.data[largest] = self.data[largest], self.data[i]
                self.heapify(largest)

        if self.type == 0:
            smallest = i
            # check if left child is smaller than i
            if l < self.heap_size and self.data[l] < self.data[i]:
                smallest = l
            
            # check if right child is smallest
            if r < self.heap_size and self.data[r] < self.data[smallest]:
                smallest = r

            # swap i with largest if i is not largest
            if smallest != i:
                self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
                self.heapify(smallest)
    
    def build_heap(self):
        self.heap_size = len(self.data)
        for i in range(int(floor(len(self.data)/2))-1, -1, -1):
            self.heapify(i)

    def heapsort(self):
        for i in range(len(self.data)-1, 0, -1):
            self.data[0], self.data[i] = self.data[i], self.data[0]
            self.heap_size -= 1
            self.heapify(0)

    def min_max(self):
        return self.data[0]

    def extract(self):
        if self.heap_size < 1:
            return "Heap underflow"

        minmax = self.data[0]
        self.data[0] = self.data[self.heap_size - 1]
        del self.data[self.heap_size-1]

        self.heap_size -= 1
        self.heapify(0)
        return minmax

    def change_key(self, i, key):
        if self.type == 1:
            if key < self.data[i]:
                return "new key too small"
            self.data[i] = key
            while i > 0 and self.data[self.parent(i)] < self.data[i]:
                self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
                i = self.parent(i)

        if self.type == 0:
            if key > self.data[i]:
                return "new key too large"
            self.data[i] = key
            while i > 0 and self.data[self.parent(i)] > self.data[i]:
                self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
                i = self.parent(i)

    def insert(self, key):
        self.heap_size +=1
        self.data.append(key)
        self.change_key(self.heap_size-1, key)
