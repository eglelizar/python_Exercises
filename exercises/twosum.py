""" <!-- 
Leetcode

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

dict = ()
result
for x in nums
    if x is in dict
    dict.add(target - x) //7

--> """

class Solution:
    
    def twoSum(self, nums, target):
        diffSet = {}
        result = []

        for x in range(0 ,len(nums)):

            substraction = target - nums[x]          #2  
            currentTarget = nums[x]

            if currentTarget in diffSet.keys():
                result.append(diffSet[currentTarget])
                result.append(x)
            else:
                diffSet[substraction] = x            #diffSet (7, 0)
            
        print (result)

        return result

nums = [3,3]
target = 6
a = Solution()
a.twoSum(nums, target)


            