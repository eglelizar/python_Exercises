#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

stack = []
max_stack = 0
answers_to_3 = []

def top(stack):
    if (stack != []):
        return (stack[-1])

def push(element):
    ele = int(element)
    global max_stack
    stack.append(ele)
    if (ele > max_stack):
        max_stack = ele

def delete():
    global max_stack
    deleted_element = stack[-1]
    del stack[-1]
    if (deleted_element == max_stack):
        max_stack = getMaxStack()

def getMaxStack():
    if (len(stack) == 0):
        return 0
    max = stack[0]
    for i in stack :
        if (max < i):
            max = i       
    return max

def getMax(operations):
    # Write your code here
    global max_stack
    global answers_to_3

    for s in operations :
        operation = s.split(" ")
        instruction = int(operation[0])
        if(instruction == 1):
            push(operation[1])
        elif(instruction== 2) :
            delete()   
        elif(instruction==3):
            answers_to_3.append(max_stack)
        else:
            return ""
    return answers_to_3



#Tests
#Should_AddElement_When1IsGivenWithX
#Should_DeleteTopElement_When2IsGiven
#Should_PrintMaximumElement_When3IsGiven
#Should_ReturnNull_WhenInputDoesNotMatchKnownConditions


n = int(input().strip())

ops = []

for _ in range(n):
    ops_item = input()
    ops.append(ops_item)

res = getMax(ops)

print (res)