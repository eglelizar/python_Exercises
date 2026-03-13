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


stack1 = Stack()
stack2 = Stack()
stack3 = Stack()

def initialize (stack_to_Initialize, elements) :
    for element in elements :
        stack_to_Initialize.push(element)           

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

        #No taking off any stack1 possiblity

        #with, with, with
        if stack1Height == stack2Height and stack2Height == stack3Height :
            return stack1Height

        if (stack1.isEmpty() == False):
            stack1.pop() 
            print ("Stack 1 ----", stack1.print())
        else:
            not_found = -1
            break
        new_stack1_height = stack1.getHeight()

        if (stack2.isEmpty() == False):
            stack2.pop() 
            print ("Stack 2 ----", stack2.print())
        else:
            not_found = -1
            break
        new_stack2_height = stack2.getHeight()

        if (stack3.isEmpty() == False):
            stack3.pop() 
            print ("Stack 3 ----", stack3.print())            
        else:
            not_found = -1
            break
        new_stack3_height = stack3.getHeight()


        #with, with, without
        if stack1Height == stack2Height and stack2Height == new_stack3_height:
            return stack1Height

        #with, without, with
        if stack1Height == new_stack2_height and new_stack2_height == stack3Height:
            return stack1Height

        #with, without, without
        if stack1Height == new_stack2_height and new_stack2_height == new_stack3_height:
            return stack1Height
        

        #without, with, with
        if new_stack1_height == stack2Height and stack2Height == stack3Height :
            return new_stack1_height
                    
        #without, with, without
        if new_stack1_height == stack2Height and stack2Height == new_stack3_height:
            return new_stack1_height

        #without, without, with
        if new_stack1_height == new_stack2_height and new_stack2_height == stack3Height:
            return new_stack1_height

        #without, without, without
        if new_stack1_height == new_stack2_height and new_stack2_height == new_stack3_height:
            return new_stack1_height


first_multiple_input = input().rstrip().split()

n1 = int(first_multiple_input[0])

n2 = int(first_multiple_input[1])

n3 = int(first_multiple_input[2])

h1 = list(map(int, input().rstrip().split()))

h2 = list(map(int, input().rstrip().split()))

h3 = list(map(int, input().rstrip().split()))

result = equalStacks(h1, h2, h3)

print ('the result is ', result)
stack1.print()
stack2.print()
stack3.print()
