class heap:
    size = 0
    heap = []
    def __init__(self, _heap):
        self.heap = _heap
        self.size = len(self.heap)

    def hasLeftChild(self, index):
        if (self.getLeftChildIndex(index) < self.size):
            return True
        return False
    
    def hasRightChild(self, index):
        if (self.getRightChildIndex(index) < self.size):
            return True
        return False

    def getParentIndex(self, childIndex):
        return abs(round((childIndex -1) /2))
    
    def getLeftChildIndex(self, parentIndex):
        return abs(round((parentIndex *2) +1))
    
    def getRightChildIndex(self, parentIndex):
        return abs(round((parentIndex *2) +2))
    
    def returnLeftChildValue(self, index):
        return heap[self.getLeftChildIndex(index)]
    
    def returnRightChildValue(self, index):
        return heap[self.getRightChildIndex(index)]
    
    def peek(self):
        return self.heap[0]
    
    def swapItems (self, index1, index2):
        temp = self.heap [index1]
        self.heap [index1] = self.heap[index2]
        self.heap[index2] = temp

    def bubbleUp (self, currentIndex):
        parentIndex =self.getParentIndex(currentIndex)
        parentValue =  self.heap [parentIndex]
        print ("bubles: " , currentIndex)
        if (self.heap[currentIndex] < parentValue):
            self.swapItems(currentIndex, parentIndex)
            leftChildIndex = self.getLeftChildIndex(parentIndex)
            if (self.heap[currentIndex] < self.heap[leftChildIndex]):
                self.swapItems(currentIndex, leftChildIndex)
            self.bubbleUp(parentIndex)
        if (parentIndex == 0):
            return 

    def insert(self, value):
        print ("previous stack: " , self.heap)
        self.heap.append(value)
        #bubble up the value
        self.bubbleUp(self.size)
        self.size = self.size + 1
        print ("after inserting: ", self.heap)

    def bubbleDown(self, index):
        if (self.hasLeftChild(index) == False):
            return
        #If we have left child
        indexOfTheSmallestChilden = self.getLeftChildIndex(index)
        if (self.hasRightChild(index) == True):
            if (self.heap[self.getRightChildIndex(index)]< self.heap[self.getLeftChildIndex(index)]):
                indexOfTheSmallestChilden = self.getRightChildIndex(index)
        
        if (self.heap[index]< self.heap[indexOfTheSmallestChilden]):
            return
        else:
            self.swapItems(index, indexOfTheSmallestChilden)
            self.bubbleDown(indexOfTheSmallestChilden)

    def poll(self):
        if (self.size == 0):
            raise ValueError(f"No value to pull")
        returnValue = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size = self.size -1
        #Bubble down
        self.bubbleDown(0)
        print ("after polling: ", self.heap)
        return returnValue

        
original = [10, 15, 20, 17, 30, 50]
heap = heap (original)
heap.insert(18)
heap.insert(1) 
print(heap.poll())