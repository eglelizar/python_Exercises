# Defini87tion for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

# 6+6 = 12 = 12 mod 10 = 2
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = [i for i in range(len(l1))]
        reminder = 0
        for i in range(0, len(l1)):
            sum = l1[i] + l2[i]
            print("sum: " , sum)
            if (reminder> 0):
                sum = sum + reminder
                print("sum with reminder: " , sum)
            if (sum >= 10):
                newSum = sum % 10
                reminder = sum / 10 
                result[i] = int(newSum)
            else:
                result[i] = int(sum)
        return result

l1 = [2,4,3]
l2 = [5,6,4]
solution = Solution()
print(solution.addTwoNumbers(l1, l2))