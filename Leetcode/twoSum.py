from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #
        #  2+7 =9
        # 9-2 = 7
        result = []
        numSets = {} # {2, 0}, {7, 1}, 

        for ind in range(0, len(nums)):
            numSets[nums[ind]] = ind
        
        #print ("current set ---> " , numSets)

        for i in  range(0, len(nums)):
            number = nums[i]
            numberToLookFor = target - number
            #print ("Number that you are looking for:  ", numberToLookFor)
            if (numSets.get(numberToLookFor) and numSets[numberToLookFor] != i):
                #print ("Numbers:  ", numberToLookFor, ",", number)
                result.append(i)
                result.append(numSets[numberToLookFor])
                return result

        return result
            


nums = [1,3,4,2]
target = 6
solution = Solution()
print("la solucion es", solution.twoSum(nums, target))