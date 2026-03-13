class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        currentNode1 = l1
        currentNode2 = l2
        finalResult = None
        carry =0
        previousNode = None
        while (currentNode1 or currentNode2):
            if (currentNode1 is None):
                value1 = 0
            else:
                 value1 = currentNode1.val
            if (currentNode2 is None):
                value2 = 0
            else:
                value2 = currentNode2.val 
            result = value1 + value2 + carry
            if (result >= 10):
                carry = int(result / 10)
                result = result % 10
            else:
                carry = 0
            finalNode = ListNode(result)
            if (previousNode is None):
                finalResult = finalNode
            else:
                previousNode.next = finalNode
            previousNode = finalNode
            if (currentNode1.next and currentNode2.next):
                currentNode1= currentNode1.next
                currentNode2 = currentNode2.next
        if (carry > 0):
            previousNode.next = ListNode(carry)
        return finalResult
listss =ListNode(2)
listss.next = ListNode(4)
listss.next = ListNode(3)
c = Solution()
a = c.addTwoNumbers(listss,listss);
print (a)