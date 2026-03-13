class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def printLeftNode(root, output):

    if root == None:
        return None    

    if (root.left):
        output.append(root.left.info)        
    if (root.right):
        output.append(root.right.info)        
    
    if (root.left):
        printLeftNode(root.left, output)
    if (root.right):
        printLeftNode(root.right, output)


def levelOrder(root):    
    leftOrder = []

    if (root):
        leftOrder.append(root.info)

    printLeftNode(root, leftOrder)    
    print(*leftOrder, sep = ' ')

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)