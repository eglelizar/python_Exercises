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

    def _init_(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if (len(self.stack) == 0):
            return
        value = self.stack[-1]
        del (self.stack[-1])
        return value
    
    def isEmpty(self):
        if (len(self.stack) == 0):
            return True
        return False
    
    def getHeight(self):
        sum = 0
        for node in self.stack :
            sum+= node
        return sum


stack1 = Stack()
stack2 = Stack()
stack3 = Stack()

def initialize (stack_to_Initialize, elements) :
    for element in elements :
        stack_to_Initialize.push(element)


def checkingTakingOff(stackToEvaluate, secondStack, thirdStack):
    if (stack.isEmpty())
        return -1
    

def equalStacks(h1, h2, h3):

    global stack1, stack2, stack3

    #Initialize stacks    
    initialize (stack1, h1)
    initialize (stack2, h2)
    initialize (stack3, h3)

    not_found = 0

    while not_found == 0:

        stack1Height = stack1.getHeight()
        stack2Height = stack2.getHeight()
        stack3Height = stack3.getHeight()

        if stack1Height == stack2Height and stack2Height == stack3Height :
            return stack2Height

        #Taking off from stack1 possibility
        stack1Value = stack1.pop()        
        takingOff1Height = stack1.getHeight()






first_multiple_input = input().rstrip().split()

n1 = int(first_multiple_input[0])

n2 = int(first_multiple_input[1])

n3 = int(first_multiple_input[2])

h1 = list(map(int, input().rstrip().split()))

h2 = list(map(int, input().rstrip().split()))

h3 = list(map(int, input().rstrip().split()))

result = equalStacks(h1, h2, h3)
