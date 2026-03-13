#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

class Stack:    
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if (len(self.stack) == 0):
            return
        value = self.stack[0]
        del (self.stack[0])
        return value
    
    def isEmpty(self):
        if (len(self.stack) ==0):
            return True
        return False
    
    def getHeight(self):
        sum = 0
        for node in self.stack :
            sum+= node
        return sum
    
    def print(self):
        print ("stack: ", self.stack)
    
    def getSize(self):        
        return len(self.stack)


stack1 = Stack()
stack2 = Stack()
stack3 = Stack()

def initialize (stack_to_Initialize, elements) :
    for element in elements :
        stack_to_Initialize.push(element)   

def checkStack(st1, st2, st3):

    #print("Comparing stacks ---> ")
    #st1.print()
    #st2.print()
    #st3.print()

    if (st1.getHeight() == st2.getHeight() and st2.getHeight() == st3.getHeight()):
        return st1.getHeight()
    return -1


def evaluateStacks(st1, st2, st3):

    global stack1
    global stack2
    global stack3
    #Lets Evaluate all options
    result = -1    

    stindex1 = 0
    stindex2 = 0
    stindex3 = 0

    newst1 = stack1    
    newst2 = stack2
    newst3 = stack3

    result = checkStack(newst1, newst2, newst3)

    while (stindex1 < st1.getSize() and result < 0):

        newst1.pop()
        newst2 = stack2     
        result = checkStack(newst1, newst2, newst3)

        while (stindex2 < st2.getSize() and result < 0):

            newst2.pop()
            newst3 = stack3
            result = checkStack(newst1, newst2, newst3)
        
            while (stindex3 < st3.getSize() and result < 0):

                newst3.pop()
                result = checkStack(newst1, newst2, newst3)
    
    return -1

            
def equalStacks(h1,h2,h3):
    print ("Initializing...")
    
    global stack1, stack2, stack3

    #Initialize stacks    
    initialize (stack1, h1)
    initialize (stack2, h2)
    initialize (stack3, h3)

    result = -1    

    stindex1 = 0
    stindex2 = 0
    stindex3 = 0

    newst1 = stack1    
    newst2 = stack2
    newst3 = stack3

    result = checkStack(newst1, newst2, newst3)

    while (stindex1 < newst1.getSize() and result < 0):

        newst1.pop()
        result = checkStack(newst1, newst2, newst3)

        while (stindex2 < newst2.getSize() and result < 0):

            newst2.pop()    
            result = checkStack(newst1, newst2, newst3)
        
            while (stindex3 < newst3.getSize() and result < 0):

                newst3.pop()
                result = checkStack(newst1, newst2, newst3)
        
            initialize (stack3, h3)

        initialize (stack2, h2)     
    
    return result
 
if __name__ == '__main__':
    f = open("OUTPUT_PATH_2.txt", 'r')

    lines = f.readline()

    first_multiple_input = lines.rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    lines = f.readline()

    h1 = list(map(int, lines.rstrip().split()))

    lines = f.readline()

    h2 = list(map(int, lines.rstrip().split()))

    lines = f.readline()

    h3 = list(map(int, lines.rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print ("result is--->", result)

    f.close()

