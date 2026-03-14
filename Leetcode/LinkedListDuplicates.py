#Example:
#You are given 2 linked lists without sorted elements, retrieve them without the duplicates
#Link List 1: 1->2->5->4->3
#Link List 2: 3->6->5->4->7
#Output: 1->2->3->4->5->6->7

class InsertDeduplicatonList:
    
     list = []
     index = 0

     def addItem(self, value):
        if (self.index==0 or self.list[self.index-1]!=value):
            self.list.append(value)
            self.index = self.index +1

     def getList(self):
        print(self.list)
        return self.list

class ListDeduplicatorAndMerged:
     
     def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

     def deduplicateAndMergeLists(self):
        result = InsertDeduplicatonList()               

        list.sort(self.list1)
        list.sort(self.list2)

        lS1 = self.list1
        lS2 = self.list2

        #Link List 1: 1->2->3->4->5
        #Link List 2: 3->4->5->6->7
        iL1 = 0
        iL2 = 0

        while (iL1 < len(lS1) and iL2 < len(lS2)):
            #print ('L1',iL1, ' value ', lS1[iL1] )
            #print ('L2',iL2, ' value ', lS2[iL2])

            if (lS1[iL1] < lS2[iL2]):
                result.addItem(lS1[iL1])
                iL1 = iL1 +1 
            else:
                if ((lS1[iL1] > lS2[iL2])):
                    result.addItem(lS2[iL2])
                    iL2 = iL2 +1 
                else:
                    result.addItem(lS1[iL1])
                    iL2 = iL2 +1 
                    iL1 = iL1 +1  

        while iL1 < len(lS1):
            result.addItem(lS1[iL1])
            iL1 = iL1 +1

        while iL2 < len(lS2):
            result.addItem(lS2[iL2])
            iL2 = iL2 +1
              
        return result.getList()  
     
l1 = [1,2,-80,6, 1, 0,3,4,5,80]
l2 = [3,4,5,6,7, 120, 4,9]
obj = ListDeduplicatorAndMerged(l1, l2)
obj.deduplicateAndMergeLists()